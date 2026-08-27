/* ==========================================================================
   ClinicusMed — main.js
   Ponto de entrada do novo Design System. Cada módulo (navbar, counters,
   progress, animations) se registra aqui — main.js só orquestra a
   inicialização, não contém lógica de UI própria.
   ==========================================================================
   Etapa 1: scaffolding. Os módulos importados ainda não fazem nada visível
   (arquivos vazios/stub) — passam a ganhar comportamento real nas etapas
   em que o componente correspondente é construído:
     navbar.js     -> Etapa 2 (Navbar premium)
     counters.js   -> Etapa 5 (Estatísticas animadas)
     progress.js   -> Etapa 3 (Dashboard demonstrativo / Jornada Médica)
     animations.js -> Etapa 6 (scroll reveal, microanimações)
   ========================================================================== */

(function(){
  'use strict';

  function init(){
    if (window.CxNavbar && typeof window.CxNavbar.init === 'function') window.CxNavbar.init();
    if (window.CxCounters && typeof window.CxCounters.init === 'function') window.CxCounters.init();
    if (window.CxProgress && typeof window.CxProgress.init === 'function') window.CxProgress.init();
    if (window.CxAnimations && typeof window.CxAnimations.init === 'function') window.CxAnimations.init();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
