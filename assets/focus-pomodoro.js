/* ============================================================
   ClinicusMed — Modo Foco + Pomodoro (widget global)
   Injetado em todas as páginas via <script src="/assets/focus-pomodoro.js" defer></script>
   Não depende de nenhum outro arquivo do site — se autoinstala.
   ============================================================ */
(function(){
  'use strict';

  var STATE_KEY = 'clinicus_pomodoro_state';
  var STATS_KEY = 'clinicus_pomodoro_stats';

  var DURATIONS = {
    foco: 25 * 60,
    pausa_curta: 5 * 60,
    pausa_longa: 15 * 60
  };
  var CYCLES_BEFORE_LONG_BREAK = 4;

  var PHASE_LABELS = {
    foco: '🍅 Foco',
    pausa_curta: '☕ Pausa Curta',
    pausa_longa: '🌿 Pausa Longa'
  };

  // ---------- estado persistente ----------
  function loadState(){
    try{
      var s = JSON.parse(localStorage.getItem(STATE_KEY));
      if(s && typeof s.remaining === 'number') return s;
    }catch(e){}
    return {
      phase: 'foco',
      remaining: DURATIONS.foco,
      running: false,
      lastTick: Date.now(),
      cyclesCompleted: 0,
      open: false
    };
  }
  function saveState(s){
    try{ localStorage.setItem(STATE_KEY, JSON.stringify(s)); }catch(e){}
  }

  function todayStr(){
    var d = new Date();
    return d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate();
  }
  function loadStats(){
    try{
      var s = JSON.parse(localStorage.getItem(STATS_KEY));
      if(s) return s;
    }catch(e){}
    return { totalCompleted:0, todayDate: todayStr(), todayCount:0, streakDays:0, lastStreakDate:null };
  }
  function saveStats(s){
    try{ localStorage.setItem(STATS_KEY, JSON.stringify(s)); }catch(e){}
  }

  var state = loadState();
  var stats = loadStats();

  // se mudou o dia, zera contagem de hoje
  if(stats.todayDate !== todayStr()){
    stats.todayDate = todayStr();
    stats.todayCount = 0;
    saveStats(stats);
  }

  // recalcula tempo decorrido desde a última página (se estava rodando)
  if(state.running){
    var elapsed = Math.floor((Date.now() - state.lastTick) / 1000);
    state.remaining -= elapsed;
    if(state.remaining < 0) state.remaining = 0;
  }
  state.lastTick = Date.now();

  // ---------- som simples (beep) via Web Audio, sem arquivo externo ----------
  function beep(){
    try{
      var ctx = new (window.AudioContext || window.webkitAudioContext)();
      var o = ctx.createOscillator();
      var g = ctx.createGain();
      o.connect(g); g.connect(ctx.destination);
      o.type = 'sine';
      o.frequency.value = 720;
      g.gain.setValueAtTime(0.001, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.15, ctx.currentTime + 0.02);
      g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
      o.start();
      o.stop(ctx.currentTime + 0.65);
    }catch(e){}
  }

  function notify(title, body){
    try{
      if('Notification' in window && Notification.permission === 'granted'){
        new Notification(title, {body: body, icon: '/assets/favicon-180.png'});
      }
    }catch(e){}
  }

  // ---------- CSS (injetado uma única vez) ----------
  var css = ""
  + ".cmed-pomo-fab{position:fixed;bottom:18px;right:18px;z-index:9998;width:52px;height:52px;border-radius:50%;"
  + "background:linear-gradient(135deg,#ff6b5b,#e0505f);color:#fff;border:none;box-shadow:0 4px 18px rgba(224,80,95,.45);"
  + "font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .15s;}"
  + ".cmed-pomo-fab:hover{transform:scale(1.06);}"
  + ".cmed-pomo-fab .cmed-pomo-badge{position:absolute;top:-4px;right:-4px;background:#1b2130;color:#ffd166;"
  + "font-size:10px;font-weight:700;border-radius:10px;padding:1px 5px;border:1px solid #ffd166;display:none;}"
  + ".cmed-pomo-panel{position:fixed;bottom:80px;right:18px;z-index:9999;width:230px;background:#161b26;"
  + "border:1px solid #2a3348;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.5);padding:16px;"
  + "font-family:'DM Sans','Segoe UI',Arial,sans-serif;color:#e6edf3;display:none;}"
  + ".cmed-pomo-panel.show{display:block;animation:cmedPomoFade .18s ease;}"
  + "@keyframes cmedPomoFade{from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:translateY(0);}}"
  + ".cmed-pomo-phase{font-size:.78em;font-weight:700;text-align:center;color:#ff8a7a;letter-spacing:.3px;margin-bottom:6px;}"
  + ".cmed-pomo-time{font-size:2.1em;font-weight:800;text-align:center;letter-spacing:1px;margin-bottom:10px;font-variant-numeric:tabular-nums;}"
  + ".cmed-pomo-cycles{text-align:center;font-size:.75em;color:#8b98ab;margin-bottom:12px;}"
  + ".cmed-pomo-btns{display:flex;gap:6px;margin-bottom:10px;}"
  + ".cmed-pomo-btns button{flex:1;background:#212940;border:1px solid #2a3348;color:#e6edf3;padding:7px 4px;"
  + "border-radius:8px;font-size:.78em;cursor:pointer;}"
  + ".cmed-pomo-btns button.primary{background:linear-gradient(135deg,#ff6b5b,#e0505f);border-color:transparent;color:#fff;font-weight:700;}"
  + ".cmed-pomo-btns button:hover{filter:brightness(1.1);}"
  + ".cmed-pomo-stats{border-top:1px solid #2a3348;padding-top:8px;font-size:.72em;color:#8b98ab;text-align:center;line-height:1.6;}"
  + ".cmed-pomo-stats b{color:#a3d84a;}"
  + ".cmed-pomo-close{position:absolute;top:8px;right:10px;background:none;border:none;color:#8b98ab;font-size:14px;cursor:pointer;}";

  var styleTag = document.createElement('style');
  styleTag.textContent = css;
  document.head.appendChild(styleTag);

  // ---------- HTML do widget ----------
  var fab = document.createElement('button');
  fab.className = 'cmed-pomo-fab';
  fab.title = 'Modo Foco (Pomodoro)';
  fab.innerHTML = '🍅<span class="cmed-pomo-badge" id="cmedPomoBadge"></span>';

  var panel = document.createElement('div');
  panel.className = 'cmed-pomo-panel';
  panel.innerHTML =
    '<button class="cmed-pomo-close" id="cmedPomoClose">✕</button>' +
    '<div class="cmed-pomo-phase" id="cmedPomoPhase"></div>' +
    '<div class="cmed-pomo-time" id="cmedPomoTime"></div>' +
    '<div class="cmed-pomo-cycles" id="cmedPomoCycles"></div>' +
    '<div class="cmed-pomo-btns">' +
      '<button id="cmedPomoStart" class="primary">Iniciar</button>' +
      '<button id="cmedPomoReset">Reiniciar</button>' +
    '</div>' +
    '<div class="cmed-pomo-stats" id="cmedPomoStats"></div>';

  document.addEventListener('DOMContentLoaded', mount);
  if(document.readyState === 'complete' || document.readyState === 'interactive'){ mount(); }

  function mount(){
    if(document.getElementById('cmedPomoFabMounted')) return;
    fab.id = 'cmedPomoFabMounted';
    document.body.appendChild(fab);
    document.body.appendChild(panel);

    fab.addEventListener('click', function(){
      state.open = !state.open;
      panel.classList.toggle('show', state.open);
      saveState(state);
      if(state.open && 'Notification' in window && Notification.permission === 'default'){
        Notification.requestPermission();
      }
    });
    document.getElementById('cmedPomoClose').addEventListener('click', function(){
      state.open = false;
      panel.classList.remove('show');
      saveState(state);
    });
    document.getElementById('cmedPomoStart').addEventListener('click', toggleRun);
    document.getElementById('cmedPomoReset').addEventListener('click', resetPhase);

    if(state.open) panel.classList.add('show');
    render();
    setInterval(tick, 1000);
  }

  function fmt(sec){
    if(sec < 0) sec = 0;
    var m = Math.floor(sec/60);
    var s = sec % 60;
    return (m<10?'0':'')+m + ':' + (s<10?'0':'')+s;
  }

  function render(){
    document.getElementById('cmedPomoPhase').textContent = PHASE_LABELS[state.phase];
    document.getElementById('cmedPomoTime').textContent = fmt(state.remaining);
    document.getElementById('cmedPomoCycles').textContent =
      '🍅 '.repeat(state.cyclesCompleted % CYCLES_BEFORE_LONG_BREAK) +
      '⬜'.repeat(CYCLES_BEFORE_LONG_BREAK - (state.cyclesCompleted % CYCLES_BEFORE_LONG_BREAK)) ;
    document.getElementById('cmedPomoStart').textContent = state.running ? 'Pausar' : 'Iniciar';
    document.getElementById('cmedPomoStats').innerHTML =
      'Hoje: <b>'+stats.todayCount+'</b> pomodoro(s) · Sequência: <b>'+stats.streakDays+'</b> dia(s)';

    var badge = document.getElementById('cmedPomoBadge');
    if(state.running){
      badge.style.display = 'block';
      badge.textContent = Math.max(0, Math.ceil(state.remaining/60));
    } else {
      badge.style.display = 'none';
    }
  }

  function toggleRun(){
    state.running = !state.running;
    state.lastTick = Date.now();
    saveState(state);
    render();
  }

  function resetPhase(){
    state.running = false;
    state.remaining = DURATIONS[state.phase];
    state.lastTick = Date.now();
    saveState(state);
    render();
  }

  function updateStreak(){
    var today = todayStr();
    if(stats.lastStreakDate === today) return; // ja contou hoje
    var yesterday = new Date();
    yesterday.setDate(yesterday.getDate()-1);
    var yStr = yesterday.getFullYear()+'-'+(yesterday.getMonth()+1)+'-'+yesterday.getDate();
    if(stats.lastStreakDate === yStr){
      stats.streakDays += 1;
    } else {
      stats.streakDays = 1;
    }
    stats.lastStreakDate = today;
  }

  function completePhase(){
    beep();
    var wasFoco = (state.phase === 'foco');
    if(wasFoco){
      state.cyclesCompleted += 1;
      stats.totalCompleted += 1;
      stats.todayCount += 1;
      updateStreak();
      saveStats(stats);
      notify('Pomodoro concluído! 🍅', 'Hora de uma pausa. Você já fez '+stats.todayCount+' hoje.');
      var isLong = (state.cyclesCompleted % CYCLES_BEFORE_LONG_BREAK === 0);
      state.phase = isLong ? 'pausa_longa' : 'pausa_curta';
    } else {
      notify('Pausa concluída ☕', 'Hora de voltar ao foco.');
      state.phase = 'foco';
    }
    state.remaining = DURATIONS[state.phase];
    state.running = false;
    state.lastTick = Date.now();
    saveState(state);
    render();
  }

  function tick(){
    if(state.running){
      var now = Date.now();
      var delta = Math.floor((now - state.lastTick)/1000);
      if(delta >= 1){
        state.remaining -= delta;
        state.lastTick = now;
        if(state.remaining <= 0){
          completePhase();
          return;
        }
        saveState(state);
      }
    }
    render();
  }

})();
