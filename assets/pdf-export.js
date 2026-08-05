/* ============================================================
   ClinicusMed — Baixar PDF (via impressão do navegador)
   Reaproveita o Modo Leitura ja existente (esconde nav/sidebar/rodape)
   + garante que a aba "Guia de Estudo" (sempre a primeira) esteja
   ativa antes de imprimir + injeta uma folha de estilo @media print
   pra deixar tudo em preto sobre branco, sem gastar tinta com tema
   escuro.
   Autoinstalavel, injetado via <script defer> em toda pagina.
   ============================================================ */
(function(){
  'use strict';

  var toolbar = document.querySelector('.cmed-reading-toolbar');
  var extras = document.querySelector('.cmed-reading-extras');
  if(!toolbar || !extras) return; // pagina sem modo leitura (simulados antigos, home etc.)

  // ---------- CSS de impressao ----------
  var printCss = ""
  + "@media print{"
  + "  *{background:#fff !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important;}"
  + "  a{color:#000 !important;text-decoration:underline !important;}"
  + "  .cmed-nav-header,.cmed-nav-breadcrumb,.cmed-nav-progress-wrap,.cmed-nav-sidebar,"
  + "  .cmed-nav-prevnext,footer,.cmed-reading-toolbar,.cmed-reading-top,.cmed-reading-progress,"
  + "  nav.tabs,.tabs,.xpbar,.cmed-pomo-fab,.cmed-pomo-panel,.cmed-pwa-banner,.cmed-focus-bar,"
  + "  .cmed-complete-box,.cmed-pomo-toast,.cmed-item-checkbox,.fc-shuffle-row,"
  + "  .review-btns,.fc-controls,.reveal-btn,.check-btn,.quiz-progress{display:none !important;}"
  + "  .wrap,.cmed-nav-main{margin:0 !important;padding:0 !important;max-width:100% !important;}"
  + "  h1,h2,h3{page-break-after:avoid;}"
  + "  img{max-width:100% !important;}"
  + "  body{padding-top:0 !important;}"
  + "}";
  var styleTag = document.createElement('style');
  styleTag.textContent = printCss;
  document.head.appendChild(styleTag);

  // ---------- botao ----------
  var btn = document.createElement('button');
  btn.className = 'cmed-reading-theme-btn';
  btn.id = 'cmedPdfBtn';
  btn.title = 'Baixar o Guia de Estudo em PDF';
  btn.innerHTML = '🖨️';
  extras.appendChild(btn);

  btn.addEventListener('click', function(){
    // garante que a aba "Guia de Estudo" (sempre a primeira) esta ativa
    var firstTab = document.querySelector('nav.tabs button, .tabs button');
    if(firstTab && !firstTab.classList.contains('active')){
      firstTab.click();
    }
    setTimeout(function(){ window.print(); }, 150);
  });

})();
