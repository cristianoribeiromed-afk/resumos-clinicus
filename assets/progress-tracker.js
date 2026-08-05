/* ============================================================
   ClinicusMed — Progresso da Jornada (Fase 1)
   Reaproveita o shell de navegação (idêntico em todas as páginas,
   gerado por inject_shell.py) como ponto de leitura/escrita:
   - .cmed-nav-sidebar-list > .cmed-nav-item[href]  → lista de capítulos
     da matéria atual (já vem pronta do catalogo.json, não precisa
     buscar de novo)
   - .cmed-nav-progress-wrap → reaproveitado pra virar progresso REAL
     (hoje só mostra posição na lista, ex: "2 de 11")
   Autoinstalável, injetado via <script defer> em toda página.
   ============================================================ */
(function(){
  'use strict';

  if(!window.ClinicusStorage) return;
  var DB = window.ClinicusStorage;

  function currentPath(){
    return window.location.pathname;
  }

  function mount(){
    var sidebarList = document.querySelector('.cmed-nav-sidebar-list');
    var progressWrap = document.querySelector('.cmed-nav-progress-wrap');
    if(!sidebarList) return; // pagina sem shell (home, demo etc.) -- nao faz nada

    var items = Array.prototype.slice.call(sidebarList.querySelectorAll('.cmed-nav-item[href]'));
    if(!items.length) return;

    DB.getCompletedChapters().then(function(done){
      renderChecklist(items, done);
      if(progressWrap) renderProgressBar(progressWrap, items, done);
      renderToggleButton(done);
    });
  }

  function normalizePath(href){
    // hrefs sao absolutos ("/semestre-01/....html") -- mantem como esta,
    // so garante que bate com location.pathname (sem host)
    try{
      var u = new URL(href, window.location.origin);
      return u.pathname;
    }catch(e){ return href; }
  }

  function renderChecklist(items, done){
    items.forEach(function(a){
      var path = normalizePath(a.getAttribute('href'));
      var isDone = !!done[path];

      a.classList.toggle('cmed-nav-item-done', isDone);

      var box = a.querySelector('.cmed-item-checkbox');
      if(!box){
        box = document.createElement('span');
        box.className = 'cmed-item-checkbox';
        a.insertBefore(box, a.firstChild);
        box.addEventListener('click', function(e){
          e.preventDefault();
          e.stopPropagation();
          DB.isChapterComplete(path).then(function(nowDone){
            DB.setChapterComplete(path, !nowDone).then(function(){ mount(); });
          });
        });
      }
      box.textContent = isDone ? '✅' : '☐';
      box.title = isDone ? 'Marcado como concluído — clique pra desmarcar' : 'Marcar como concluído';
    });
  }

  function renderProgressBar(wrap, items, done){
    var total = items.length;
    var completedCount = items.filter(function(a){
      var path = normalizePath(a.getAttribute('href'));
      return !!done[path];
    }).length;
    var pct = total>0 ? Math.round((completedCount/total)*100) : 0;

    var label = wrap.querySelector('.cmed-nav-progress-label');
    var fill = wrap.querySelector('.cmed-nav-progress-fill');
    if(label){
      var spans = label.querySelectorAll('span');
      if(spans[1]) spans[1].textContent = completedCount + ' de ' + total + ' concluídos (' + pct + '%)';
    }
    if(fill){ fill.style.width = pct + '%'; fill.style.transition = 'width .3s'; }
  }

  function renderToggleButton(done){
    var breadcrumb = document.querySelector('.cmed-nav-breadcrumb');
    if(!breadcrumb) return;
    if(document.getElementById('cmedCompleteToggle')) return; // ja montado

    var path = currentPath();
    var isDone = !!done[path];

    var box = document.createElement('div');
    box.className = 'cmed-complete-box';
    box.id = 'cmedCompleteToggle';
    box.innerHTML =
      '<button id="cmedCompleteBtn" class="cmed-complete-btn ' + (isDone ? 'is-done' : '') + '">' +
        (isDone ? '✅ Concluído' : '☐ Marcar como concluído') +
      '</button>';

    breadcrumb.parentNode.insertBefore(box, breadcrumb.nextSibling);

    document.getElementById('cmedCompleteBtn').addEventListener('click', function(){
      var btn = this;
      DB.isChapterComplete(path).then(function(nowDone){
        var next = !nowDone;
        DB.setChapterComplete(path, next).then(function(){
          btn.classList.toggle('is-done', next);
          btn.textContent = next ? '✅ Concluído' : '☐ Marcar como concluído';
          if(next && window.ClinicusStorage){
            // pequeno reforco de XP, mesmo sistema ja usado no Pomodoro
            try{
              DB.getStudyStats().then(function(){}); // no-op, so garante storage aquecido
            }catch(e){}
          }
          // recalcula a barra de progresso e o checklist da sidebar
          mount();
        });
      });
    });
  }

  var css = ""
  + ".cmed-complete-box{padding:10px 20px 0;max-width:900px;margin:0 auto;}"
  + ".cmed-complete-btn{background:var(--surface,#161b26);border:1px solid var(--border,#2a3348);color:var(--text,#e6edf3);"
  + "padding:8px 16px;border-radius:8px;font-size:.82em;cursor:pointer;font-family:inherit;transition:.15s;}"
  + ".cmed-complete-btn:hover{border-color:#6bbf59;}"
  + ".cmed-complete-btn.is-done{background:rgba(107,191,89,.15);border-color:#6bbf59;color:#a3d84a;font-weight:700;}"
  + ".cmed-nav-item-done{opacity:.75;}"
  + ".cmed-nav-item-done span:last-child{text-decoration:none;}"
  + ".cmed-item-checkbox{cursor:pointer;margin-right:6px;font-size:.95em;flex-shrink:0;display:inline-block;"
  + "transition:transform .12s;}"
  + ".cmed-item-checkbox:hover{transform:scale(1.2);}";
  var styleTag = document.createElement('style');
  styleTag.textContent = css;
  document.head.appendChild(styleTag);

  if(document.readyState !== 'loading'){ mount(); }
  else { document.addEventListener('DOMContentLoaded', mount); }

})();
