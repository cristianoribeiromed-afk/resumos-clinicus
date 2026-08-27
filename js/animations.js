/* ==========================================================================
   ClinicusMed — animations.js
   Scroll reveal (.cx-reveal -> .cx-in-view). Versão inicial habilitada já
   na Etapa 2 (o Mockup do Hero usa .cx-reveal) — o polimento completo de
   microanimações adicionais chega na Etapa 6.
   Respeita prefers-reduced-motion: nesse caso, os elementos já aparecem
   visíveis via CSS (ver animations.css), então aqui simplesmente não
   precisamos observar nada.
   ========================================================================== */

window.CxAnimations = (function(){
  'use strict';

  function prefersReducedMotion(){
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function initScrollReveal(){
    if (prefersReducedMotion()) return;
    var els = document.querySelectorAll('.cx-reveal');
    if (!els.length) return;

    if (!('IntersectionObserver' in window)) {
      els.forEach(function(el){ el.classList.add('cx-in-view'); });
      return;
    }

    var observer = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting) {
          entry.target.classList.add('cx-in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    els.forEach(function(el){ observer.observe(el); });
  }

  function init(){
    initScrollReveal();
  }

  return { init: init };
})();
