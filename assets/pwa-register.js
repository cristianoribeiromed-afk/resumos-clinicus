/* ============================================================
   ClinicusMed — Registro do PWA (Service Worker + botão de instalar)
   Autoinstalável, injetado em toda página via <script defer>.
   ============================================================ */
(function(){
  'use strict';

  // ---------- registra o service worker ----------
  if('serviceWorker' in navigator && navigator.serviceWorker){
    // Guarda se já havia um Service Worker controlando a página ANTES de
    // qualquer coisa acontecer -- se não havia (aluno novo, primeira visita),
    // não faz sentido recarregar quando o primeiro SW assumir o controle.
    var jaTinhaControlador = !!navigator.serviceWorker.controller;

    window.addEventListener('load', function(){
      navigator.serviceWorker.register('/sw.js').then(function(reg){
        // Verifica ativamente se existe uma versão nova (não espera o navegador
        // decidir sozinho quando checar — isso podia demorar horas/dias).
        try{ reg.update(); }catch(e){}
      }).catch(function(){
        // navegador sem suporte ou falha silenciosa -- site continua
        // funcionando normal, so sem cache offline
      });

      // Quando um Service Worker NOVO assume o controle da página (depois de
      // um skipWaiting()), recarrega automaticamente uma única vez -- mas só
      // se já existia um controlador antes (ou seja, é atualização de verdade,
      // não a primeira instalação de um aluno novo).
      var jaRecarregou = false;
      navigator.serviceWorker.addEventListener('controllerchange', function(){
        if(jaRecarregou || !jaTinhaControlador) return;
        jaRecarregou = true;
        window.location.reload();
      });
    });
  }

  function isStandalone(){
    return window.matchMedia('(display-mode: standalone)').matches ||
           window.navigator.standalone === true; // iOS
  }
  if(isStandalone()) return; // ja instalado, nao mostra nada

  var DISMISS_KEY = 'clinicus_pwa_install_dismissed';
  try{ if(localStorage.getItem(DISMISS_KEY) === '1') return; }catch(e){}

  var css = ""
  + ".cmed-pwa-banner{position:fixed;left:16px;right:16px;bottom:16px;z-index:9997;"
  + "max-width:380px;margin:0 auto;background:#161b26;border:1px solid #2a3348;border-radius:14px;"
  + "padding:14px 16px;display:none;align-items:center;gap:12px;box-shadow:0 10px 30px rgba(0,0,0,.5);"
  + "font-family:'DM Sans','Segoe UI',Arial,sans-serif;color:#e6edf3;}"
  + ".cmed-pwa-banner.show{display:flex;animation:cmedPwaFade .2s ease;}"
  + "@keyframes cmedPwaFade{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}"
  + ".cmed-pwa-banner img{width:38px;height:38px;border-radius:9px;flex-shrink:0;}"
  + ".cmed-pwa-banner .txt{flex:1;font-size:.8em;line-height:1.35;}"
  + ".cmed-pwa-banner .txt b{display:block;color:#ffd166;font-size:1.02em;margin-bottom:2px;}"
  + ".cmed-pwa-banner button{background:linear-gradient(135deg,#6bbf59,#a3d84a);border:none;color:#04150c;"
  + "font-weight:700;padding:8px 12px;border-radius:8px;font-size:.78em;cursor:pointer;white-space:nowrap;}"
  + ".cmed-pwa-banner .close{background:none;border:none;color:#8b98ab;font-size:.78em;cursor:pointer;padding:8px 6px;font-weight:600;white-space:nowrap;text-decoration:underline;}";
  var styleTag = document.createElement('style');
  styleTag.textContent = css;
  document.head.appendChild(styleTag);

  var banner = document.createElement('div');
  banner.className = 'cmed-pwa-banner';
  var bannerMounted = false;
  function mountBanner(){
    if(bannerMounted) return;
    bannerMounted = true;
    document.body.appendChild(banner);
  }
  document.addEventListener('DOMContentLoaded', mountBanner);
  if(document.readyState !== 'loading'){ mountBanner(); }

  function dismiss(){
    banner.classList.remove('show');
    try{ localStorage.setItem(DISMISS_KEY, '1'); }catch(e){}
  }

  // ---------- Android/Desktop (Chrome/Edge) — evento nativo ----------
  var deferredPrompt = null;
  window.addEventListener('beforeinstallprompt', function(e){
    e.preventDefault();
    deferredPrompt = e;
    banner.innerHTML =
      '<img src="/assets/pwa/icon-192.png" alt="Clinicus">' +
      '<div class="txt"><b>📲 Instale a Clinicus no seu dispositivo!</b>Estude com mais rapidez, receba notificações e tenha uma experiência semelhante à de um aplicativo.</div>' +
      '<button id="cmedPwaInstallBtn">Instalar agora</button>' +
      '<button class="close" id="cmedPwaCloseBtn">Mais tarde</button>';
    banner.classList.add('show');
    banner.querySelector('#cmedPwaInstallBtn').addEventListener('click', function(){
      banner.classList.remove('show');
      deferredPrompt.prompt();
      deferredPrompt.userChoice.then(function(){ deferredPrompt = null; });
    });
    banner.querySelector('#cmedPwaCloseBtn').addEventListener('click', dismiss);
  });

  window.addEventListener('appinstalled', function(){
    try{ localStorage.setItem(DISMISS_KEY, '1'); }catch(e){}
  });

  // ---------- iOS Safari — nao existe beforeinstallprompt, precisa de instrucao manual ----------
  var ua = navigator.userAgent || '';
  var isIOS = /iPad|iPhone|iPod/.test(ua) && !window.MSStream;
  var isSafari = /Safari/.test(ua) && !/CriOS|FxiOS|EdgiOS/.test(ua);
  if(isIOS && isSafari){
    banner.innerHTML =
      '<img src="/assets/pwa/icon-192.png" alt="Clinicus">' +
      '<div class="txt"><b>📲 Instale a Clinicus no seu dispositivo!</b>Toque em <b>Compartilhar</b> (□↑) e depois em <b>"Adicionar à Tela de Início"</b> — estude com mais rapidez e uma experiência de aplicativo.</div>' +
      '<button class="close" id="cmedPwaCloseBtnIos">Mais tarde</button>';
    banner.classList.add('show');
    banner.querySelector('#cmedPwaCloseBtnIos').addEventListener('click', dismiss);
  }

})();
