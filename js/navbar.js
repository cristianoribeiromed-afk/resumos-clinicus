/* ==========================================================================
   ClinicusMed — navbar.js
   Comportamento da navbar premium: muda de aparência ao rolar a página,
   e controla o menu mobile (hambúrguer).
   ========================================================================== */

window.CxNavbar = (function(){
  'use strict';

  function initScrollBehavior(){
    var nav = document.getElementById('cxNavbar');
    if (!nav) return;

    var SCROLL_THRESHOLD = 24;
    function onScroll(){
      if (window.scrollY > SCROLL_THRESHOLD) {
        nav.classList.add('cx-navbar--scrolled');
      } else {
        nav.classList.remove('cx-navbar--scrolled');
      }
    }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  function initMobileMenu(){
    var burger = document.getElementById('cxNavbarBurger');
    var panel = document.getElementById('cxNavbarMobilePanel');
    if (!burger || !panel) return;

    function closePanel(){
      panel.classList.remove('cx-navbar-mobile-panel--open');
    }

    burger.addEventListener('click', function(){
      panel.classList.toggle('cx-navbar-mobile-panel--open');
    });

    panel.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', closePanel);
    });
  }

  function init(){
    initScrollBehavior();
    initMobileMenu();
  }

  return { init: init };
})();
