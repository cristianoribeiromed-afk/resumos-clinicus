/* ============================================================
   ClinicusMed — Modo Foco + Pomodoro Inteligente
   Depende de /assets/clinicus-storage.js (deve carregar ANTES deste).
   Autoinstalável — não requer nenhuma edição na página onde é injetado.
   ============================================================ */
(function(){
  'use strict';

  // Corrige o comportamento padrão do navegador de restaurar a rolagem.
  try{
    if('scrollRestoration' in history){ history.scrollRestoration = 'manual'; }
    if(!window.location.hash){ window.scrollTo(0, 0); }
  }catch(e){}

  if(!window.ClinicusStorage){ return; } // storage-service precisa ter carregado antes
  var DB = window.ClinicusStorage;

  var PHASE_LABELS = { foco: '🍅 Foco', pausa_curta: '☕ Pausa Curta', pausa_longa: '🌿 Pausa Longa' };

  var ACHIEVEMENTS = [
    {id:'first_pomodoro', icon:'🥉', label:'Primeiro Pomodoro', check:function(s){ return s.totalPomodoros>=1; }},
    {id:'pomodoros_10',   icon:'🥈', label:'10 Pomodoros',      check:function(s){ return s.totalPomodoros>=10; }},
    {id:'pomodoros_100',  icon:'🥇', label:'100 Pomodoros',     check:function(s){ return s.totalPomodoros>=100; }},
    {id:'master_foco',    icon:'👑', label:'Mestre do Foco',    check:function(s){ return s.totalPomodoros>=100 && s.streakDays>=30; }},
    {id:'questoes_1000',  icon:'📚', label:'1000 Questões Respondidas', check:function(s){ return s.questionsAnswered>=1000; }},
    {id:'flashcards_500', icon:'🧠', label:'500 Flashcards Revisados',  check:function(s){ return s.flashcardsReviewed>=500; }},
    {id:'streak_30',      icon:'🎯', label:'30 Dias Consecutivos',      check:function(s){ return s.streakDays>=30; }}
  ];

  var settings = { focus:25, shortBreak:5, longBreak:15, cyclesBeforeLong:4, dailyGoal:4, sound:'silence', notifyEnabled:true };
  var state = { phase:'foco', remaining:25*60, running:false, lastTick:Date.now(), cyclesCompleted:0, open:false, warnedOneMin:false };
  var stats = null;
  var sessionStart = Date.now();
  var sessionPomodoros = 0;
  var sessionSeconds = 0;
  var focusModeActive = false;

  function durationOf(phase){
    if(phase==='foco') return settings.focus*60;
    if(phase==='pausa_curta') return settings.shortBreak*60;
    return settings.longBreak*60;
  }

  function subjectName(){
    var eyebrow = document.querySelector('.eyebrow');
    if(eyebrow) return eyebrow.textContent.split('·')[0].trim();
    var h1 = document.querySelector('h1');
    return h1 ? h1.textContent.trim() : 'ClinicusMed';
  }

  // ---------- som (beep simples, Web Audio, sem arquivo externo) ----------
  function beep(freq){
    try{
      var ctx = new (window.AudioContext || window.webkitAudioContext)();
      var o = ctx.createOscillator(); var g = ctx.createGain();
      o.connect(g); g.connect(ctx.destination);
      o.type='sine'; o.frequency.value = freq || 720;
      g.gain.setValueAtTime(0.001, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.15, ctx.currentTime+0.02);
      g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime+0.6);
      o.start(); o.stop(ctx.currentTime+0.65);
    }catch(e){}
  }
  function notify(title, body){
    if(!settings.notifyEnabled) return;
    try{
      if('Notification' in window && Notification.permission==='granted'){
        new Notification(title, {body:body, icon:'/assets/favicon-180.png'});
      }
    }catch(e){}
  }
  function toast(msg){
    var t = document.createElement('div');
    t.className = 'cmed-pomo-toast';
    t.textContent = msg;
    document.body.appendChild(t);
    requestAnimationFrame(function(){ t.classList.add('show'); });
    setTimeout(function(){
      t.classList.remove('show');
      setTimeout(function(){ t.remove(); }, 300);
    }, 3200);
  }

  // ---------- CSS ----------
  var css = ""
  + ".cmed-pomo-fab{position:fixed;bottom:18px;right:18px;z-index:9998;width:52px;height:52px;border-radius:50%;"
  + "background:linear-gradient(135deg,#ff6b5b,#e0505f);color:#fff;border:none;box-shadow:0 4px 18px rgba(224,80,95,.45);"
  + "font-size:22px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .15s;}"
  + ".cmed-pomo-fab:hover{transform:scale(1.06);}"
  + ".cmed-pomo-fab .cmed-pomo-badge{position:absolute;top:-4px;right:-4px;background:#1b2130;color:#ffd166;"
  + "font-size:10px;font-weight:700;border-radius:10px;padding:1px 5px;border:1px solid #ffd166;display:none;}"
  + ".cmed-pomo-panel{position:fixed;bottom:80px;right:18px;z-index:9999;width:250px;background:#161b26;"
  + "border:1px solid #2a3348;border-radius:14px;box-shadow:0 10px 30px rgba(0,0,0,.5);padding:16px;"
  + "font-family:'DM Sans','Segoe UI',Arial,sans-serif;color:#e6edf3;display:none;}"
  + ".cmed-pomo-panel.show{display:block;animation:cmedPomoFade .18s ease;}"
  + "@keyframes cmedPomoFade{from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:translateY(0);}}"
  + ".cmed-pomo-phase{font-size:.78em;font-weight:700;text-align:center;color:#ff8a7a;letter-spacing:.3px;margin-bottom:6px;}"
  + ".cmed-pomo-time{font-size:2.1em;font-weight:800;text-align:center;letter-spacing:1px;margin-bottom:10px;font-variant-numeric:tabular-nums;}"
  + ".cmed-pomo-cycles{text-align:center;font-size:.75em;color:#8b98ab;margin-bottom:8px;}"
  + ".cmed-pomo-goal{text-align:center;font-size:.72em;color:#8b98ab;margin-bottom:10px;}"
  + ".cmed-pomo-goal-track{width:100%;height:5px;background:#0e1118;border-radius:4px;overflow:hidden;margin-top:4px;}"
  + ".cmed-pomo-goal-fill{height:100%;background:linear-gradient(90deg,#ff6b5b,#ffd166);width:0%;transition:width .3s;}"
  + ".cmed-pomo-btns{display:flex;gap:6px;margin-bottom:8px;}"
  + ".cmed-pomo-btns button{flex:1;background:#212940;border:1px solid #2a3348;color:#e6edf3;padding:7px 4px;"
  + "border-radius:8px;font-size:.78em;cursor:pointer;}"
  + ".cmed-pomo-btns button.primary{background:linear-gradient(135deg,#ff6b5b,#e0505f);border-color:transparent;color:#fff;font-weight:700;}"
  + ".cmed-pomo-btns button:hover{filter:brightness(1.1);}"
  + ".cmed-pomo-focus-btn{width:100%;background:linear-gradient(135deg,#4d9fff,#2a7ade);border:none;color:#fff;"
  + "padding:8px;border-radius:8px;font-size:.8em;font-weight:700;cursor:pointer;margin-bottom:8px;}"
  + ".cmed-pomo-focus-btn:hover{filter:brightness(1.1);}"
  + ".cmed-pomo-settings-toggle{background:none;border:none;color:#8b98ab;font-size:12px;cursor:pointer;"
  + "display:block;margin:0 auto 8px;text-decoration:underline;}"
  + ".cmed-pomo-settings{display:none;border-top:1px solid #2a3348;padding-top:8px;margin-bottom:8px;}"
  + ".cmed-pomo-settings.show{display:block;}"
  + ".cmed-pomo-settings label{display:block;font-size:.72em;color:#8b98ab;margin-bottom:4px;}"
  + ".cmed-pomo-settings select,.cmed-pomo-settings input{width:100%;background:#0e1118;border:1px solid #2a3348;"
  + "color:#e6edf3;padding:5px 6px;border-radius:6px;font-size:.75em;margin-bottom:8px;}"
  + ".cmed-pomo-stats{border-top:1px solid #2a3348;padding-top:8px;font-size:.72em;color:#8b98ab;text-align:center;line-height:1.6;}"
  + ".cmed-pomo-stats b{color:#a3d84a;}"
  + ".cmed-pomo-close{position:absolute;top:8px;right:10px;background:none;border:none;color:#8b98ab;font-size:14px;cursor:pointer;}"
  // ---- toast de conquista ----
  + ".cmed-pomo-toast{position:fixed;top:18px;left:50%;transform:translateX(-50%) translateY(-20px);z-index:10001;"
  + "background:#161b26;border:1px solid #ffd166;color:#ffd166;padding:12px 20px;border-radius:12px;font-family:'DM Sans',sans-serif;"
  + "font-size:.9em;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,.5);opacity:0;transition:.3s;text-align:center;}"
  + ".cmed-pomo-toast.show{opacity:1;transform:translateX(-50%) translateY(0);}"
  // ---- MODO FOCO overlay ----
  + "body.cmed-focus-active .cmed-nav-header,body.cmed-focus-active .cmed-nav-sidebar,"
  + "body.cmed-focus-active .cmed-nav-prevnext,body.cmed-focus-active .cmed-reading-toolbar,"
  + "body.cmed-focus-active nav.tabs,body.cmed-focus-active footer,"
  + "body.cmed-focus-active .cmed-pomo-fab{display:none !important;}"
  + "body.cmed-focus-active .cmed-nav-main{margin:0 !important;padding:0 !important;}"
  + "body.cmed-focus-active .wrap{max-width:720px !important;margin:0 auto !important;padding:20px 16px 120px !important;}"
  + ".cmed-focus-bar{position:fixed;top:0;left:0;right:0;z-index:10000;background:#0d0f16;border-bottom:1px solid #2a3348;"
  + "padding:12px 20px;display:none;align-items:center;justify-content:space-between;font-family:'DM Sans',sans-serif;color:#e6edf3;gap:12px;flex-wrap:wrap;}"
  + ".cmed-focus-bar.show{display:flex;}"
  + ".cmed-focus-bar .cmed-fb-subject{font-size:.85em;color:#8b98ab;font-weight:600;}"
  + ".cmed-focus-bar .cmed-fb-time{font-size:1.4em;font-weight:800;color:#ff8a7a;font-variant-numeric:tabular-nums;}"
  + ".cmed-focus-bar .cmed-fb-progress{flex:1;min-width:120px;height:6px;background:#1b2130;border-radius:4px;overflow:hidden;margin:0 12px;}"
  + ".cmed-focus-bar .cmed-fb-progress-fill{height:100%;background:linear-gradient(90deg,#ff6b5b,#ffd166);transition:width 1s linear;}"
  + ".cmed-focus-bar .cmed-fb-exit{background:#212940;border:1px solid #2a3348;color:#e6edf3;padding:7px 14px;"
  + "border-radius:8px;font-size:.8em;cursor:pointer;white-space:nowrap;}"
  + ".cmed-focus-bar .cmed-fb-exit:hover{background:#2a3348;}"
  + "body.cmed-focus-active{padding-top:64px;}"
  // ---- relatório de sessão ----
  + ".cmed-pomo-report-bg{position:fixed;inset:0;background:rgba(4,6,10,.75);z-index:10002;display:flex;"
  + "align-items:center;justify-content:center;padding:20px;}"
  + ".cmed-pomo-report{background:#161b26;border:1px solid #2a3348;border-radius:16px;padding:26px;max-width:340px;"
  + "width:100%;font-family:'DM Sans',sans-serif;color:#e6edf3;text-align:center;}"
  + ".cmed-pomo-report h3{font-family:'Lora',serif;color:#ffd166;margin-bottom:14px;font-size:1.2em;}"
  + ".cmed-pomo-report .row{display:flex;justify-content:space-between;font-size:.85em;padding:6px 0;border-bottom:1px solid #212940;}"
  + ".cmed-pomo-report .row b{color:#a3d84a;}"
  + ".cmed-pomo-report button{margin-top:16px;background:linear-gradient(135deg,#ff6b5b,#e0505f);border:none;color:#fff;"
  + "padding:10px 20px;border-radius:8px;font-weight:700;cursor:pointer;width:100%;}";

  var styleTag = document.createElement('style');
  styleTag.textContent = css;
  document.head.appendChild(styleTag);

  // ---------- HTML ----------
  var fab = document.createElement('button');
  fab.className = 'cmed-pomo-fab';
  fab.title = 'Modo Foco (Pomodoro)';
  fab.innerHTML = '🍅<span class="cmed-pomo-badge" id="cmedPomoBadge"></span>';

  var panel = document.createElement('div');
  panel.className = 'cmed-pomo-panel';
  panel.innerHTML =
    '<button class="cmed-pomo-close" id="cmedPomoClose">✕</button>' +
    '<button class="cmed-pomo-focus-btn" id="cmedPomoEnterFocus">🎯 Entrar em Modo Foco</button>' +
    '<div class="cmed-pomo-phase" id="cmedPomoPhase"></div>' +
    '<div class="cmed-pomo-time" id="cmedPomoTime"></div>' +
    '<div class="cmed-pomo-cycles" id="cmedPomoCycles"></div>' +
    '<div class="cmed-pomo-goal" id="cmedPomoGoalWrap">' +
      '<span id="cmedPomoGoalLabel"></span>' +
      '<div class="cmed-pomo-goal-track"><div class="cmed-pomo-goal-fill" id="cmedPomoGoalFill"></div></div>' +
    '</div>' +
    '<div class="cmed-pomo-btns">' +
      '<button id="cmedPomoStart" class="primary">Iniciar</button>' +
      '<button id="cmedPomoReset">Reiniciar</button>' +
    '</div>' +
    '<button class="cmed-pomo-settings-toggle" id="cmedPomoSettingsToggle">⚙ Configurar ciclos</button>' +
    '<div class="cmed-pomo-settings" id="cmedPomoSettings">' +
      '<label>Duração dos ciclos</label>' +
      '<select id="cmedPomoPreset">' +
        '<option value="25-5">Clássico — 25min foco / 5min pausa</option>' +
        '<option value="50-10">Longo — 50min foco / 10min pausa</option>' +
        '<option value="custom">Personalizado</option>' +
      '</select>' +
      '<div id="cmedPomoCustomWrap" style="display:none;">' +
        '<label>Foco (min)</label><input type="number" id="cmedPomoCustomFocus" min="1" max="120">' +
        '<label>Pausa (min)</label><input type="number" id="cmedPomoCustomBreak" min="1" max="60">' +
      '</div>' +
      '<label>Meta diária (pomodoros)</label>' +
      '<input type="number" id="cmedPomoDailyGoal" min="1" max="20">' +
    '</div>' +
    '<div class="cmed-pomo-stats" id="cmedPomoStats"></div>';

  var focusBar = document.createElement('div');
  focusBar.className = 'cmed-focus-bar';
  focusBar.innerHTML =
    '<span class="cmed-fb-subject" id="cmedFbSubject"></span>' +
    '<span class="cmed-fb-time" id="cmedFbTime"></span>' +
    '<div class="cmed-fb-progress"><div class="cmed-fb-progress-fill" id="cmedFbProgressFill"></div></div>' +
    '<button class="cmed-fb-exit" id="cmedFbExit">Finalizar Sessão</button>';

  document.addEventListener('DOMContentLoaded', mount);
  if(document.readyState==='complete' || document.readyState==='interactive'){ mount(); }

  function mount(){
    if(document.getElementById('cmedPomoFabMounted')) return;
    fab.id = 'cmedPomoFabMounted';

    Promise.all([DB.getPomodoroSettings(), DB.getPomodoroState(), DB.getStudyStats()]).then(function(res){
      settings = res[0] || settings;
      var savedState = res[1];
      stats = res[2];

      if(savedState){
        state = savedState;
        if(state.running){
          var elapsed = Math.floor((Date.now()-state.lastTick)/1000);
          state.remaining -= elapsed;
          if(state.remaining<0) state.remaining = 0;
        }
      } else {
        state.remaining = durationOf('foco');
      }
      state.lastTick = Date.now();

      document.body.appendChild(fab);
      document.body.appendChild(panel);
      document.body.appendChild(focusBar);

      wireEvents();
      loadSettingsIntoUI();
      if(state.open) panel.classList.add('show');
      render();
      setInterval(tick, 1000);
    });
  }

  function wireEvents(){
    fab.addEventListener('click', function(){
      state.open = !state.open;
      panel.classList.toggle('show', state.open);
      DB.savePomodoroState(state);
      if(state.open && 'Notification' in window && Notification.permission==='default'){
        Notification.requestPermission();
      }
    });
    document.getElementById('cmedPomoClose').addEventListener('click', function(){
      state.open = false; panel.classList.remove('show'); DB.savePomodoroState(state);
    });
    document.getElementById('cmedPomoStart').addEventListener('click', toggleRun);
    document.getElementById('cmedPomoReset').addEventListener('click', resetPhase);
    document.getElementById('cmedPomoEnterFocus').addEventListener('click', enterFocusMode);
    document.getElementById('cmedFbExit').addEventListener('click', finishSession);

    document.getElementById('cmedPomoSettingsToggle').addEventListener('click', function(){
      document.getElementById('cmedPomoSettings').classList.toggle('show');
    });
    document.getElementById('cmedPomoPreset').addEventListener('change', function(e){
      var v = e.target.value;
      document.getElementById('cmedPomoCustomWrap').style.display = (v==='custom') ? 'block' : 'none';
      if(v==='25-5'){ settings.focus=25; settings.shortBreak=5; settings.longBreak=15; }
      if(v==='50-10'){ settings.focus=50; settings.shortBreak=10; settings.longBreak=20; }
      persistSettingsAndSync();
    });
    document.getElementById('cmedPomoCustomFocus').addEventListener('change', function(e){
      settings.focus = Math.max(1, parseInt(e.target.value)||25);
      persistSettingsAndSync();
    });
    document.getElementById('cmedPomoCustomBreak').addEventListener('change', function(e){
      settings.shortBreak = Math.max(1, parseInt(e.target.value)||5);
      persistSettingsAndSync();
    });
    document.getElementById('cmedPomoDailyGoal').addEventListener('change', function(e){
      settings.dailyGoal = Math.max(1, parseInt(e.target.value)||4);
      DB.savePomodoroSettings(settings);
      render();
    });
  }

  function persistSettingsAndSync(){
    DB.savePomodoroSettings(settings);
    if(!state.running){
      state.remaining = durationOf(state.phase);
      DB.savePomodoroState(state);
    }
    render();
  }

  function loadSettingsIntoUI(){
    var preset = document.getElementById('cmedPomoPreset');
    if(settings.focus===25 && settings.shortBreak===5) preset.value='25-5';
    else if(settings.focus===50 && settings.shortBreak===10) preset.value='50-10';
    else { preset.value='custom'; document.getElementById('cmedPomoCustomWrap').style.display='block'; }
    document.getElementById('cmedPomoCustomFocus').value = settings.focus;
    document.getElementById('cmedPomoCustomBreak').value = settings.shortBreak;
    document.getElementById('cmedPomoDailyGoal').value = settings.dailyGoal;
  }

  function fmt(sec){
    if(sec<0) sec=0;
    var m = Math.floor(sec/60), s = sec%60;
    return (m<10?'0':'')+m+':'+(s<10?'0':'')+s;
  }

  function render(){
    document.getElementById('cmedPomoPhase').textContent = PHASE_LABELS[state.phase];
    document.getElementById('cmedPomoTime').textContent = fmt(state.remaining);
    document.getElementById('cmedPomoCycles').textContent =
      '🍅 '.repeat(state.cyclesCompleted % settings.cyclesBeforeLong) +
      '⬜ '.repeat(settings.cyclesBeforeLong - (state.cyclesCompleted % settings.cyclesBeforeLong));
    document.getElementById('cmedPomoStart').textContent = state.running ? 'Pausar' : 'Iniciar';

    var todayCount = (stats && stats.dayLog[window.ClinicusStorageUtils.todayStr()]) ? stats.dayLog[window.ClinicusStorageUtils.todayStr()].pomodoros : 0;
    var goalPct = Math.min(100, (todayCount/settings.dailyGoal)*100);
    document.getElementById('cmedPomoGoalLabel').textContent = 'Meta de hoje: '+todayCount+' / '+settings.dailyGoal+' 🍅';
    document.getElementById('cmedPomoGoalFill').style.width = goalPct+'%';

    document.getElementById('cmedPomoStats').innerHTML =
      'Sequência: <b>'+(stats?stats.streakDays:0)+'</b> dia(s) · Total: <b>'+(stats?stats.totalPomodoros:0)+'</b> pomodoros';

    var badge = document.getElementById('cmedPomoBadge');
    if(state.running){ badge.style.display='block'; badge.textContent = Math.max(0, Math.ceil(state.remaining/60)); }
    else { badge.style.display='none'; }

    if(focusModeActive){
      document.getElementById('cmedFbTime').textContent = fmt(state.remaining);
      var total = durationOf(state.phase);
      var pct = total>0 ? ((total-state.remaining)/total)*100 : 0;
      document.getElementById('cmedFbProgressFill').style.width = pct+'%';
      document.getElementById('cmedFbSubject').textContent = PHASE_LABELS[state.phase] + ' · ' + subjectName();
    }
  }

  function toggleRun(){
    state.running = !state.running;
    state.lastTick = Date.now();
    DB.savePomodoroState(state);
    render();
  }
  function resetPhase(){
    state.running = false;
    state.remaining = durationOf(state.phase);
    state.lastTick = Date.now();
    DB.savePomodoroState(state);
    render();
  }

  function enterFocusMode(){
    focusModeActive = true;
    document.body.classList.add('cmed-focus-active');
    focusBar.classList.add('show');
    panel.classList.remove('show');
    state.open = false;
    if(!state.running){ toggleRun(); }
    sessionStart = Date.now();
    sessionPomodoros = 0;
    sessionSeconds = 0;
    render();
  }

  function exitFocusModeVisualOnly(){
    focusModeActive = false;
    document.body.classList.remove('cmed-focus-active');
    focusBar.classList.remove('show');
  }

  function finishSession(){
    exitFocusModeVisualOnly();
    var totalMin = Math.round(sessionSeconds/60);
    var xp = sessionPomodoros * 15;
    var bg = document.createElement('div');
    bg.className = 'cmed-pomo-report-bg';
    bg.innerHTML =
      '<div class="cmed-pomo-report">' +
        '<h3>🏁 Sessão Finalizada</h3>' +
        '<div class="row"><span>Ciclos completos</span><b>'+sessionPomodoros+' 🍅</b></div>' +
        '<div class="row"><span>Tempo total de foco</span><b>'+totalMin+' min</b></div>' +
        '<div class="row"><span>XP ganho</span><b>+'+xp+' XP</b></div>' +
        '<button id="cmedPomoReportClose">Fechar</button>' +
      '</div>';
    document.body.appendChild(bg);
    document.getElementById('cmedPomoReportClose').addEventListener('click', function(){ bg.remove(); });
  }

  function checkAchievements(){
    ACHIEVEMENTS.forEach(function(a){
      if(a.check(stats)){
        DB.unlockAchievement(a.id).then(function(res){
          if(res.isNew){ toast(a.icon+' Conquista desbloqueada: '+a.label); }
        });
      }
    });
  }

  function completePhase(){
    beep(state.phase==='foco' ? 620 : 480);
    var wasFoco = (state.phase==='foco');
    if(wasFoco){
      state.cyclesCompleted += 1;
      sessionPomodoros += 1;
      sessionSeconds += durationOf('foco');
      DB.logCompletedPomodoro(durationOf('foco'), subjectName()).then(function(newStats){
        stats = newStats;
        checkAchievements();
        render();
      });
      notify('Excelente! Hora da pausa. ☕', 'Você completou um ciclo de foco.');
      var isLong = (state.cyclesCompleted % settings.cyclesBeforeLong === 0);
      state.phase = isLong ? 'pausa_longa' : 'pausa_curta';
    } else {
      notify('Vamos continuar! 🍅', 'A pausa acabou, hora de focar de novo.');
      state.phase = 'foco';
    }
    state.remaining = durationOf(state.phase);
    state.running = false;
    state.warnedOneMin = false;
    state.lastTick = Date.now();
    DB.savePomodoroState(state);
    render();
  }

  function tick(){
    if(state.running){
      var now = Date.now();
      var delta = Math.floor((now-state.lastTick)/1000);
      if(delta>=1){
        state.remaining -= delta;
        state.lastTick = now;

        if(state.remaining===60 && !state.warnedOneMin){
          state.warnedOneMin = true;
          notify('Quase lá! ⏳', 'A sessão está quase terminando (1 minuto).');
        }
        if(focusModeActive) sessionSeconds += (state.phase==='foco' ? delta : 0);

        if(state.remaining<=0){ completePhase(); return; }
        DB.savePomodoroState(state);
      }
    }
    render();
  }

})();
