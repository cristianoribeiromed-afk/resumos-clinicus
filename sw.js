/* ============================================================
   ClinicusMed — Service Worker
   Estratégia:
   - App shell (CSS/JS/ícones/manifest) → cacheado no install, sempre
     servido do cache primeiro (rápido, funciona offline desde já).
   - Páginas de conteúdo (capítulos, simulados etc.) → "stale-while-
     revalidate": mostra a versão em cache na hora (se existir) E busca
     uma atualização em segundo plano pra próxima vez. Só fica disponível
     offline DEPOIS que o aluno visitou a página com internet — não
     tenta baixar o site inteiro de uma vez.
   - Nunca intercepta chamadas pra fora do domínio (Mercado Pago,
     Google Sheets, fontes) — essas sempre vão direto pra rede.

   Pra forçar os navegadores a pegarem uma versão nova deste arquivo
   (e por consequência invalidar caches antigos), basta mudar o
   CACHE_VERSION abaixo a cada atualização importante do site.
   ============================================================ */

var CACHE_VERSION = 'clinicus-v7';
var SHELL_CACHE = CACHE_VERSION + '-shell';
var PAGES_CACHE = CACHE_VERSION + '-pages';

var SHELL_ASSETS = [
  '/assets/shell-nav.css',
  '/assets/clinicus-storage.js',
  '/assets/focus-pomodoro.js',
  '/assets/favicon-32.png',
  '/assets/favicon-180.png',
  '/assets/pwa/icon-192.png',
  '/assets/pwa/icon-512.png',
  '/manifest.json',
  '/offline.html'
];

self.addEventListener('install', function(event){
  event.waitUntil(
    caches.open(SHELL_CACHE).then(function(cache){
      return cache.addAll(SHELL_ASSETS).catch(function(){
        // se algum asset individual falhar, nao derruba a instalacao inteira
      });
    }).then(function(){ return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function(event){
  event.waitUntil(
    caches.keys().then(function(keys){
      return Promise.all(
        keys.filter(function(k){ return k.indexOf(CACHE_VERSION) !== 0; })
            .map(function(k){ return caches.delete(k); })
      );
    }).then(function(){ return self.clients.claim(); })
  );
});

function isSameOrigin(url){
  try{ return new URL(url).origin === self.location.origin; }catch(e){ return false; }
}

self.addEventListener('fetch', function(event){
  var req = event.request;

  // so GET, so mesma origem -- nunca mexe em POST (checkout, formularios) nem em dominios externos
  if(req.method !== 'GET' || !isSameOrigin(req.url)){
    return;
  }

  var url = new URL(req.url);

  // App shell: cache-first
  if(SHELL_ASSETS.indexOf(url.pathname) !== -1){
    event.respondWith(
      caches.match(req).then(function(cached){
        return cached || fetch(req);
      })
    );
    return;
  }

  // Paginas HTML (navegacao) e imagens do conteudo: stale-while-revalidate
  var isNavigation = req.mode === 'navigate' || (req.headers.get('accept')||'').indexOf('text/html') !== -1;
  var isContentImage = /\.(png|jpe?g|webp|gif|svg)$/i.test(url.pathname);

  if(isNavigation || isContentImage){
    event.respondWith(
      caches.open(PAGES_CACHE).then(function(cache){
        return cache.match(req).then(function(cached){
          var networkFetch = fetch(req).then(function(response){
            if(response && response.status === 200){
              cache.put(req, response.clone());
            }
            return response;
          }).catch(function(){
            // offline e sem cache: pra navegacao, mostra a pagina de offline
            if(isNavigation){
              return caches.match('/offline.html');
            }
          });
          return cached || networkFetch;
        });
      })
    );
    return;
  }

  // Todo o resto (CSS/JS de paginas especificas, fontes etc.): so deixa passar
});
