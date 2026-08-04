/* ============================================================
   ClinicusMed — StorageService
   Camada única de persistência. HOJE: localStorage.
   AMANHÃ: trocar o corpo dos métodos por chamadas Supabase (ou
   qualquer outro backend) sem mudar a assinatura de nenhum método
   — toda a interface (widgets, UI) chama SÓ esses métodos, nunca
   localStorage diretamente.

   Todo método retorna Promise, mesmo sendo síncrono hoje — assim o
   código que já usa .then()/await já está pronto pra um backend
   assíncrono de verdade, no dia que precisar.
   ============================================================ */
(function(global){
  'use strict';

  var PREFIX = 'clinicus_';

  function _read(key, fallback){
    try{
      var raw = localStorage.getItem(PREFIX + key);
      return raw !== null ? JSON.parse(raw) : fallback;
    }catch(e){ return fallback; }
  }
  function _write(key, value){
    try{
      localStorage.setItem(PREFIX + key, JSON.stringify(value));
      return true;
    }catch(e){ return false; }
  }
  function _remove(key){
    try{ localStorage.removeItem(PREFIX + key); }catch(e){}
    return true;
  }

  function todayStr(){
    var d = new Date();
    return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
  }
  function isoWeekKey(){
    var d = new Date();
    var target = new Date(d.valueOf());
    var dayNr = (d.getDay()+6)%7;
    target.setDate(target.getDate()-dayNr+3);
    var firstThursday = new Date(target.getFullYear(),0,4);
    var diff = target - firstThursday;
    var week = 1 + Math.round(diff/(7*24*60*60*1000));
    return target.getFullYear()+'-W'+String(week).padStart(2,'0');
  }
  function monthKey(){
    var d = new Date();
    return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0');
  }

  // ---------------------------------------------------------
  // API genérica (baixo nível) — get/set/remove de qualquer chave
  // ---------------------------------------------------------
  var Storage = {
    get: function(key, fallback){ return Promise.resolve(_read(key, fallback)); },
    set: function(key, value){ return Promise.resolve(_write(key, value)); },
    remove: function(key){ return Promise.resolve(_remove(key)); },

    // -------------------------------------------------------
    // Domínio: Configurações do Pomodoro
    // -------------------------------------------------------
    getPomodoroSettings: function(){
      return this.get('pomodoro_settings', {
        focus: 25, shortBreak: 5, longBreak: 15,
        cyclesBeforeLong: 4, dailyGoal: 4,
        sound: 'silence', notifyEnabled: true
      });
    },
    savePomodoroSettings: function(settings){
      return this.set('pomodoro_settings', settings);
    },

    // -------------------------------------------------------
    // Domínio: Estado corrente do timer (persiste entre páginas)
    // -------------------------------------------------------
    getPomodoroState: function(){
      return this.get('pomodoro_state', null);
    },
    savePomodoroState: function(state){
      return this.set('pomodoro_state', state);
    },

    // -------------------------------------------------------
    // Domínio: Estatísticas de estudo (hoje / semana / mês / streak)
    // -------------------------------------------------------
    getStudyStats: function(){
      return this.get('study_stats', {
        totalPomodoros: 0,
        totalFocusSeconds: 0,
        dayLog: {},     // { "2026-08-04": {pomodoros: N, seconds: N} }
        weekLog: {},    // { "2026-W31": {pomodoros: N, seconds: N} }
        monthLog: {},   // { "2026-08": {pomodoros: N, seconds: N} }
        streakDays: 0,
        lastStreakDate: null,
        questionsAnswered: 0,
        flashcardsReviewed: 0,
        subjectsStudied: {}   // { "Bioquímica II": N sessions }
      });
    },
    saveStudyStats: function(stats){
      return this.set('study_stats', stats);
    },
    // registra 1 pomodoro de foco concluído (chamado pelo widget)
    logCompletedPomodoro: function(seconds, subjectName){
      var self = this;
      return this.getStudyStats().then(function(stats){
        var today = todayStr();
        var week = isoWeekKey();
        var month = monthKey();

        stats.totalPomodoros += 1;
        stats.totalFocusSeconds += seconds;

        if(!stats.dayLog[today]) stats.dayLog[today] = {pomodoros:0, seconds:0};
        stats.dayLog[today].pomodoros += 1;
        stats.dayLog[today].seconds += seconds;

        if(!stats.weekLog[week]) stats.weekLog[week] = {pomodoros:0, seconds:0};
        stats.weekLog[week].pomodoros += 1;
        stats.weekLog[week].seconds += seconds;

        if(!stats.monthLog[month]) stats.monthLog[month] = {pomodoros:0, seconds:0};
        stats.monthLog[month].pomodoros += 1;
        stats.monthLog[month].seconds += seconds;

        if(subjectName){
          stats.subjectsStudied[subjectName] = (stats.subjectsStudied[subjectName]||0) + 1;
        }

        // streak
        if(stats.lastStreakDate !== today){
          var yesterday = new Date();
          yesterday.setDate(yesterday.getDate()-1);
          var yStr = yesterday.getFullYear()+'-'+String(yesterday.getMonth()+1).padStart(2,'0')+'-'+String(yesterday.getDate()).padStart(2,'0');
          stats.streakDays = (stats.lastStreakDate === yStr) ? stats.streakDays+1 : 1;
          stats.lastStreakDate = today;
        }

        return self.saveStudyStats(stats).then(function(){ return stats; });
      });
    },
    logQuestionAnswered: function(){
      var self = this;
      return this.getStudyStats().then(function(stats){
        stats.questionsAnswered += 1;
        return self.saveStudyStats(stats).then(function(){ return stats; });
      });
    },
    logFlashcardReviewed: function(){
      var self = this;
      return this.getStudyStats().then(function(stats){
        stats.flashcardsReviewed += 1;
        return self.saveStudyStats(stats).then(function(){ return stats; });
      });
    },

    // -------------------------------------------------------
    // Domínio: Conquistas
    // -------------------------------------------------------
    getAchievements: function(){
      return this.get('achievements', {});   // { "first_pomodoro": "2026-08-04T..." }
    },
    unlockAchievement: function(id){
      var self = this;
      return this.getAchievements().then(function(ach){
        if(ach[id]) return {achievements: ach, isNew: false};
        ach[id] = new Date().toISOString();
        return self.set('achievements', ach).then(function(){
          return {achievements: ach, isNew: true};
        });
      });
    },

    // -------------------------------------------------------
    // Domínio: Progresso — capítulos marcados como concluídos
    // Chave: caminho da página (ex: "/semestre-01/anatomia1/Capitulo_01_...")
    // -------------------------------------------------------
    getCompletedChapters: function(){
      return this.get('completed_chapters', {});   // { "/caminho.html": "2026-08-05T..." }
    },
    isChapterComplete: function(path){
      return this.getCompletedChapters().then(function(done){
        return !!done[path];
      });
    },
    setChapterComplete: function(path, completed){
      var self = this;
      return this.getCompletedChapters().then(function(done){
        if(completed){ done[path] = new Date().toISOString(); }
        else { delete done[path]; }
        return self.set('completed_chapters', done).then(function(){ return done; });
      });
    }
  };

  global.ClinicusStorage = Storage;
  global.ClinicusStorageUtils = { todayStr: todayStr, isoWeekKey: isoWeekKey, monthKey: monthKey };

})(window);
