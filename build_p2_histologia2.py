# -*- coding: utf-8 -*-
"""
build_p2_histologia2.py — gera os capitulos 4, 5 e 6 de Histología II (P2):
Sistema Digestivo I (Cavidade Bucal e Glândulas Salivares), II (Esôfago/Estômago/
Intestinos) e III (Glândulas Anexas: Fígado, Pâncreas, Vesícula Biliar) — no
padrao visual ja estabelecido em Histología II P1 (paleta roxo/petroleo,
7 abas: Guia/Casos/Video/Flashcards/Banco/Quiz/Atlas).
"""
import json, os

REPO = '/home/claude/resumos-clinicus'
CHDIR = os.path.join(REPO, 'semestre-02', 'histologia2')

with open('/tmp/claude-0/-home-claude-resumos-clinicus/f990c82e-1273-5bd0-9652-b7c68dd81832/scratchpad/digestivo/style/style_histo2.css', encoding='utf-8') as f:
    STYLE_CSS = f.read()

CMED_VIDEO_STYLE = r"""
.cmed-video-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(79,209,161,.14);border:1px solid var(--ok);color:var(--ok);font-size:.72em;font-weight:700;padding:4px 10px;border-radius:20px;margin-bottom:10px;}
.cmed-video-sub{color:var(--text-dim);font-size:.85em;margin:-6px 0 14px 0;}
.cmed-video-card{background:var(--card2,#0f1726);border:1px solid var(--border);border-radius:14px;overflow:hidden;margin-bottom:16px;}
.cmed-video-thumb{position:relative;width:100%;aspect-ratio:16/9;background:#000 center/cover no-repeat;cursor:pointer;}
.cmed-video-thumb img{width:100%;height:100%;object-fit:cover;display:block;opacity:.85;}
.cmed-video-play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;}
.cmed-video-play span{width:64px;height:64px;border-radius:50%;background:rgba(0,0,0,.55);border:2px solid #fff;display:flex;align-items:center;justify-content:center;font-size:1.6em;color:#fff;transition:transform .15s;}
.cmed-video-thumb:hover .cmed-video-play span{transform:scale(1.08);background:var(--accent);}
.cmed-video-dur{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.75);color:#fff;font-size:.75em;padding:2px 8px;border-radius:5px;}
.cmed-video-body{padding:14px 16px;}
.cmed-video-tag{color:var(--gold);font-size:.72em;font-weight:700;letter-spacing:.03em;text-transform:uppercase;}
.cmed-video-title{color:var(--text);font-size:1.05em;font-weight:700;margin:4px 0 8px 0;}
.cmed-video-meta{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-size:.82em;color:var(--text-dim);margin-bottom:10px;}
.cmed-video-stars{color:var(--gold);}
.cmed-video-why{background:rgba(232,184,75,.10);border:1px solid var(--gold);border-radius:8px;padding:10px 12px;font-size:.85em;margin:10px 0;color:var(--text-dim);}
.cmed-video-why b{color:var(--gold);}
.cmed-video-btns{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.cmed-video-btn{background:var(--accent);color:#fff;border:none;padding:9px 18px;border-radius:20px;cursor:pointer;font-size:.82em;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:6px;}
.cmed-video-btn.secondary{background:transparent;border:1px solid var(--border);color:var(--text-dim);}
.cmed-video-btn:hover{opacity:.88;}
.cmed-video-note{color:var(--text-dim);font-size:.8em;text-align:center;margin-top:6px;}
.cmed-video-extra-label{font-size:.85em;color:var(--text-dim);margin:18px 0 8px 0;font-weight:700;}
@media (max-width:600px){.cmed-video-play span{width:52px;height:52px;font-size:1.3em;}}
"""

CMED_VIDEO_SECTION = r"""
<section class="panel" id="p2">
  <div class="card">
    <span class="cmed-video-badge">🩺 Recomendado pela ClinicusMed</span>
    <h2>🎥 Complemento em Vídeo</h2>
    <p class="cmed-video-sub">A Clinicus selecionou este conteúdo para complementar seu estudo. Não substitui a leitura do resumo — o resumo ensina, o vídeo reforça.</p>
    <div id="cmedVideoContainer">
      <p style="color:var(--text-dim);font-size:.9em;">Carregando recomendações...</p>
    </div>
  </div>
</section>
"""

CMED_VIDEO_SCRIPT = r"""
<script>
(function(){
  function ytThumb(id){ return 'https://img.youtube.com/vi/'+id+'/hqdefault.jpg'; }
  function ytWatch(id){ return 'https://www.youtube.com/watch?v='+id; }
  function stars(n){ n = n||5; return '★'.repeat(n) + '☆'.repeat(5-n); }

  function videoCard(v, isPrincipal){
    if(!v || !v.id) return '';
    var thumb = v.tipo === 'vimeo' ? '' : ytThumb(v.id);
    var watchUrl = v.tipo === 'vimeo' ? ('https://vimeo.com/'+v.id) : ytWatch(v.id);
    var embedUrl = v.tipo === 'vimeo' ? ('https://player.vimeo.com/video/'+v.id+'?autoplay=1') : ('https://www.youtube.com/embed/'+v.id+'?autoplay=1&rel=0');
    var tag = isPrincipal ? '🎥 Vídeo Principal' : '➕ Complementar';
    var card = document.createElement('div');
    card.className = 'cmed-video-card';
    card.innerHTML =
      '<div class="cmed-video-thumb" data-embed="'+embedUrl+'" style="background-image:url(\''+thumb+'\')">' +
        '<div class="cmed-video-play"><span>▶</span></div>' +
        (v.duracao ? '<div class="cmed-video-dur">⏱ '+v.duracao+'</div>' : '') +
      '</div>' +
      '<div class="cmed-video-body">' +
        '<div class="cmed-video-tag">'+tag+'</div>' +
        '<div class="cmed-video-title">'+(v.titulo||'')+'</div>' +
        '<div class="cmed-video-meta">' +
          (v.duracao ? '<span>⏱ '+v.duracao+'</span>' : '') +
          '<span class="cmed-video-stars">'+stars(v.estrelas)+'</span>' +
          (v.canal ? '<span>· '+v.canal+'</span>' : '') +
        '</div>' +
        (v.motivo ? '<div class="cmed-video-why"><b>📌 Por que recomendamos este vídeo?</b><br>'+v.motivo+'</div>' : '') +
        '<div class="cmed-video-btns">' +
          '<a class="cmed-video-btn" href="'+watchUrl+'" target="_blank" rel="noopener">↗ Abrir no site original</a>' +
          '<button class="cmed-video-btn secondary" data-copy="'+watchUrl+'">📋 Copiar link</button>' +
        '</div>' +
      '</div>';
    return card;
  }

  function render(data){
    var container = document.getElementById('cmedVideoContainer');
    if(!container) return;
    var entry = data && typeof CHAPTER_ID !== 'undefined' ? data[CHAPTER_ID] : null;

    if(!entry || !entry.principal){
      var section = document.getElementById('p2');
      if(section) section.style.display = 'none';
      var navBtn = document.querySelector('nav.tabs button[data-p="p2"]');
      if(navBtn) navBtn.style.display = 'none';
      return;
    }

    container.innerHTML = '';
    container.appendChild(videoCard(entry.principal, true));
    if(entry.extras && entry.extras.length){
      var label = document.createElement('div');
      label.className = 'cmed-video-extra-label';
      label.textContent = '📎 Vídeos complementares';
      container.appendChild(label);
      entry.extras.slice(0,3).forEach(function(ex){
        container.appendChild(videoCard(ex, false));
      });
    }
    var note = document.createElement('p');
    note.className = 'cmed-video-note';
    if(entry.verMaisEm && entry.verMaisEm.texto){
      note.innerHTML = entry.verMaisEm.texto;
    } else {
      note.textContent = 'Este vídeo complementa o conteúdo estudado neste capítulo.';
    }
    container.appendChild(note);

    container.addEventListener('click', function(e){
      var thumb = e.target.closest('.cmed-video-thumb');
      if(thumb){
        var embedUrl = thumb.dataset.embed;
        if(embedUrl && !thumb.querySelector('iframe')){
          thumb.innerHTML = '<iframe src="'+embedUrl+'" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"></iframe>';
          thumb.style.backgroundImage = 'none';
          thumb.style.cursor = 'default';
        }
        return;
      }
      var copyBtn = e.target.closest('[data-copy]');
      if(copyBtn){
        navigator.clipboard.writeText(copyBtn.dataset.copy).then(function(){
          var old = copyBtn.textContent;
          copyBtn.textContent = '✅ Copiado!';
          setTimeout(function(){ copyBtn.textContent = old; }, 1800);
        });
      }
    });
  }

  fetch('/videos.json').then(function(r){ return r.json(); }).then(render).catch(function(){
    var section = document.getElementById('p2');
    if(section) section.style.display = 'none';
    var navBtn = document.querySelector('nav.tabs button[data-p="p2"]');
    if(navBtn) navBtn.style.display = 'none';
  });
})();
</script>
"""

LETTERS = ['A','B','C','D','E']

def render_engine_script(chapter_id, titulo, bank, flashcards, cases):
    return f"""
<script>
const bank = {json.dumps(bank, ensure_ascii=False)};
const flashcards = {json.dumps(flashcards, ensure_ascii=False)};

let xp = 0;
function addXP(v){{
  xp += v;
  const lvl = Math.floor(xp/50)+1;
  document.getElementById('lvlLabel').textContent = 'Nv. '+lvl;
  const pct = Math.min(100,((xp%50)/50)*100);
  document.getElementById('xpFill').style.width = pct+'%';
  document.getElementById('xpText').textContent = xp+' XP';
}}

document.getElementById('tabs').addEventListener('click',(e)=>{{
  if(e.target.tagName==='BUTTON'){{
    document.querySelectorAll('nav.tabs button').forEach(b=>b.classList.remove('active'));
    document.querySelectorAll('section.panel').forEach(p=>p.classList.remove('active'));
    e.target.classList.add('active');
    document.getElementById(e.target.dataset.p).classList.add('active');
  }}
}});

const list = document.getElementById('gabaritoList');
const letters = ['A','B','C','D','E'];
bank.forEach((item, idx)=>{{
  const div = document.createElement('div');
  div.className='qitem';
  div.innerHTML = `
    <div class="qmeta"><span>${{item.tema}}</span><span>${{item.nivel}}</span></div>
    <div class="qtxt">${{item.n}}. ${{item.q}}</div>
    <ul class="opts">${{item.opts.map((o,i)=>`<li data-i="${{i}}" data-qi="${{idx}}">${{letters[i]}}) ${{o}}</li>`).join('')}}</ul>
    <button class="reveal-btn" data-qi="${{idx}}">Ver comentário completo</button>
    <div class="comment" id="comment-${{idx}}">
      <p><b>✅ Resposta correta: ${{letters[item.correct]}}</b></p>
      <p><b>Justificativa:</b> ${{item.justificativa}}</p>
      <p><b>Análise das alternativas incorretas:</b></p>
      ${{item.analise_letters.map((l,i)=>`<p>&nbsp;&nbsp;<b>${{l}})</b> ${{item.analise[i]}}</p>`).join('')}}
      <p><b>🔑 Conceito-chave:</b> ${{item.conceito}}</p>
      <p><b>⚠️ Pegadinha:</b> ${{item.pegadinha}}</p>
      <p><b>💡 Dica Clinicus:</b> ${{item.dica}}</p>
    </div>`;
  list.appendChild(div);
}});

list.addEventListener('click', (e)=>{{
  if(e.target.tagName==='LI'){{
    if(window.ClinicusStorage) window.ClinicusStorage.logQuestionAnswered();
    const qi = e.target.dataset.qi;
    const i = parseInt(e.target.dataset.i);
    const item = bank[qi];
    const opts = e.target.parentElement.querySelectorAll('li');
    opts.forEach(o=>o.classList.remove('correct','wrong'));
    if(i===item.correct){{ e.target.classList.add('correct'); addXP(5); }}
    else {{ e.target.classList.add('wrong'); opts[item.correct].classList.add('correct'); }}
  }}
  if(e.target.classList.contains('reveal-btn')){{
    const qi = e.target.dataset.qi;
    document.getElementById('comment-'+qi).classList.toggle('show');
  }}
}});

const CHAPTER_ID = '{chapter_id}';
const SRS_KEY = 'clinicus_srs_' + CHAPTER_ID;
const DAY_MS = 24*60*60*1000;

function loadSRS(){{ try{{ return JSON.parse(localStorage.getItem(SRS_KEY)) || {{}}; }}catch(e){{ return {{}}; }} }}
function saveSRS(data){{ localStorage.setItem(SRS_KEY, JSON.stringify(data)); }}
function getCardState(data, id){{ return data[id] || {{ ef:2.5, interval:0, reps:0, due:Date.now() }}; }}

function computeNextState(s, quality){{
  let ns = Object.assign({{}}, s);
  if(quality === 0){{
    ns.reps = 0; ns.interval = 1; ns.ef = Math.max(1.3, ns.ef - 0.20);
  }} else {{
    ns.reps += 1;
    if(quality === 1){{
      ns.interval = ns.reps === 1 ? 1 : Math.max(1, Math.round(ns.interval * 1.2));
      ns.ef = Math.max(1.3, ns.ef - 0.15);
    }} else if(quality === 2){{
      ns.interval = ns.reps === 1 ? 1 : (ns.reps === 2 ? 3 : Math.round(ns.interval * ns.ef));
    }} else if(quality === 3){{
      ns.interval = ns.reps === 1 ? 2 : Math.round(ns.interval * ns.ef * 1.3);
      ns.ef = ns.ef + 0.15;
    }}
  }}
  return ns;
}}
function reviewCard(cardId, quality){{
  const data = loadSRS();
  const s = getCardState(data, cardId);
  const ns = computeNextState(s, quality);
  ns.due = Date.now() + ns.interval * DAY_MS;
  ns.lastReview = Date.now();
  data[cardId] = ns;
  saveSRS(data);
  return ns;
}}
function isDue(data, id){{
  const s = data[id];
  if(!s) return true;
  return s.due <= Date.now();
}}
function updateSrsStatus(){{
  const data = loadSRS();
  const dueCount = flashcards.filter(c => isDue(data, 'fc'+c.n)).length;
  const totalReviewed = Object.keys(data).length;
  document.getElementById('srsStatus').innerHTML =
    `<span>📅 <b>${{dueCount}}</b> card${{dueCount===1?'':'s'}} pra revisar hoje</span>
     <span>✅ <b>${{totalReviewed}}</b>/${{flashcards.length}} já iniciados no sistema</span>`;
}}

let fcMode = 'due';
let fcSet = [];
let fcIdx = 0;
let mastered = 0;
const fcCard = document.getElementById('fcCard');

function buildFcSet(){{
  const data = loadSRS();
  let pool = flashcards.slice();
  if(fcMode === 'due'){{
    pool = pool.filter(c => isDue(data, 'fc'+c.n));
    pool.sort((a,b)=>{{
      const sa = data['fc'+a.n], sb = data['fc'+b.n];
      const da = sa ? sa.due : Date.now();
      const db = sb ? sb.due : Date.now();
      return da - db;
    }});
  }}
  fcSet = pool;
  fcIdx = 0;
  mastered = flashcards.filter(c => {{ const s = data['fc'+c.n]; return s && s.reps >= 2 && s.ef >= 2.5; }}).length;
}}

function renderFc(){{
  updateSrsStatus();
  document.getElementById('fcMastered').textContent = mastered;
  document.getElementById('fcTotal').textContent = fcSet.length;
  const navControls = document.getElementById('fcNavControls');
  const reviewBtns = document.getElementById('reviewBtns');
  fcCard.classList.remove('flipped');
  reviewBtns.style.display = 'none';

  if(fcSet.length===0){{
    document.getElementById('fcTagFront').textContent = '🎉';
    document.getElementById('fcFront').textContent = fcMode==='due'
      ? 'Você revisou tudo que estava pendente por hoje!'
      : 'Nenhum card nessa categoria';
    document.getElementById('fcBack').textContent = fcMode==='due' ? 'Volta amanhã pra continuar a revisão espaçada, ou muda pra "Todos os Cards" se quiser praticar mais.' : '';
    document.getElementById('fcIndex').textContent = '0';
    navControls.style.display = 'flex';
    return;
  }}
  const c = fcSet[fcIdx];
  document.getElementById('fcTagFront').textContent = c.cat;
  document.getElementById('fcFront').textContent = c.f;
  document.getElementById('fcBack').textContent = c.b;
  document.getElementById('fcIndex').textContent = fcIdx+1;
  navControls.style.display = 'flex';
}}

function showReviewPreview(){{
  const data = loadSRS();
  const s = getCardState(data, 'fc'+fcSet[fcIdx].n);
  const ids = ['prevAgain','prevHard','prevGood','prevEasy'];
  [0,1,2,3].forEach((q,i)=>{{
    const ns = computeNextState(s, q);
    document.getElementById(ids[i]).textContent = ns.interval + 'd';
  }});
  document.getElementById('reviewBtns').style.display = 'grid';
}}

fcCard.addEventListener('click', ()=>{{
  fcCard.classList.toggle('flipped');
  if(fcCard.classList.contains('flipped') && fcSet.length){{ showReviewPreview(); }}
  else {{ document.getElementById('reviewBtns').style.display = 'none'; }}
}});
document.getElementById('fcFlip').addEventListener('click', ()=>{{
  fcCard.classList.toggle('flipped');
  if(fcCard.classList.contains('flipped') && fcSet.length){{ showReviewPreview(); }}
  else {{ document.getElementById('reviewBtns').style.display = 'none'; }}
}});
document.getElementById('fcNext').addEventListener('click', ()=>{{ if(fcSet.length){{fcIdx=(fcIdx+1)%fcSet.length; renderFc(); addXP(1);}} }});
document.getElementById('fcPrev').addEventListener('click', ()=>{{ if(fcSet.length){{fcIdx=(fcIdx-1+fcSet.length)%fcSet.length; renderFc();}} }});
document.getElementById('fcShuffle').addEventListener('click', ()=>{{
  for(let i=fcSet.length-1;i>0;i--){{ const j=Math.floor(Math.random()*(i+1)); [fcSet[i],fcSet[j]]=[fcSet[j],fcSet[i]]; }}
  fcIdx = 0; renderFc();
}});

function handleSrsReview(quality){{
  if(window.ClinicusStorage) window.ClinicusStorage.logFlashcardReviewed();
  if(!fcSet.length) return;
  const cardId = 'fc' + fcSet[fcIdx].n;
  reviewCard(cardId, quality);
  addXP(quality === 3 ? 6 : quality === 2 ? 4 : quality === 1 ? 2 : 1);
  buildFcSet();
  renderFc();
}}
document.getElementById('srsAgain').addEventListener('click', ()=> handleSrsReview(0));
document.getElementById('srsHard').addEventListener('click', ()=> handleSrsReview(1));
document.getElementById('srsGood').addEventListener('click', ()=> handleSrsReview(2));
document.getElementById('srsEasy').addEventListener('click', ()=> handleSrsReview(3));

document.getElementById('fcModeFilters').addEventListener('click',(e)=>{{
  if(e.target.tagName==='BUTTON'){{
    document.querySelectorAll('#fcModeFilters button').forEach(b=>b.classList.remove('active'));
    e.target.classList.add('active');
    fcMode = e.target.dataset.mode;
    buildFcSet();
    renderFc();
  }}
}});
buildFcSet();
renderFc();

function shuffle(arr){{for(let i=arr.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[arr[i],arr[j]]=[arr[j],arr[i]];}}return arr;}}
let quizSet=[], quizIdx=0, quizScore=0;
function startQuiz(){{
  quizSet = shuffle([...bank]);
  quizIdx=0; quizScore=0;
  document.getElementById('quizResult').style.display='none';
  renderQuiz();
}}
function renderQuiz(){{
  const area = document.getElementById('quizArea');
  if(quizIdx>=quizSet.length){{
    area.innerHTML='';
    const res = document.getElementById('quizResult');
    res.style.display='block';
    res.innerHTML = `🏆 Resultado: ${{quizScore}}/${{quizSet.length}} corretas<br><button class="reveal-btn" onclick="startQuiz()">Repetir Quiz</button>`;
    addXP(quizScore*3);
    return;
  }}
  const item = quizSet[quizIdx];
  area.innerHTML = `<p class="progresslabel">Pergunta ${{quizIdx+1}}/${{quizSet.length}} · ${{item.nivel}}</p>
    <p class="qtxt" style="font-weight:600;">${{item.q}}</p>
    ${{item.opts.map((o,i)=>`<button class="qz-btn" data-i="${{i}}">${{letters[i]}}) ${{o}}</button>`).join('')}}`;
  area.querySelectorAll('.qz-btn').forEach(btn=>{{
    btn.onclick = ()=>{{
      const i = parseInt(btn.dataset.i);
      if(i===item.correct){{ btn.style.borderColor='var(--ok)'; btn.style.color='var(--ok)'; quizScore++; }}
      else {{ btn.style.borderColor='var(--bad)'; btn.style.color='var(--bad)'; }}
      area.querySelectorAll('.qz-btn').forEach(b=>b.disabled=true);
      setTimeout(()=>{{quizIdx++;renderQuiz();}},900);
    }};
  }});
}}
startQuiz();

const cases = {json.dumps(cases, ensure_ascii=False)};

const casesArea = document.getElementById('casesArea');
cases.forEach((c, ci)=>{{
  const div = document.createElement('div');
  div.className = 'case-level';
  let qHtml = '';
  c.perguntas.forEach((p, pi)=>{{
    qHtml += `<div class="case-q">
      <b>${{pi+1}})</b> ${{p.q}}
      <br><button class="case-answer-btn" data-ci="${{ci}}" data-pi="${{pi}}">Ver resposta comentada</button>
      <div class="case-answer" id="case-answer-${{ci}}-${{pi}}">${{p.a}}</div>
    </div>`;
  }});
  div.innerHTML = `
    <div class="case-level-head" data-ci="${{ci}}">
      <span>${{c.nivel}}</span><span>▼</span>
    </div>
    <div class="case-level-body" id="case-body-${{ci}}">
      <div class="case-hist"><b>História Clínica:</b> ${{c.hist}}</div>
      <div class="case-hist"><b>Dados:</b> ${{c.dados}}</div>
      ${{qHtml}}
    </div>`;
  casesArea.appendChild(div);
}});

casesArea.addEventListener('click', (e)=>{{
  if(e.target.classList.contains('case-level-head') || e.target.closest('.case-level-head')){{
    const head = e.target.closest('.case-level-head');
    const ci = head.dataset.ci;
    document.getElementById('case-body-'+ci).classList.toggle('show');
  }}
  if(e.target.classList.contains('case-answer-btn')){{
    const ci = e.target.dataset.ci, pi = e.target.dataset.pi;
    document.getElementById(`case-answer-${{ci}}-${{pi}}`).classList.toggle('show');
  }}
}});
document.getElementById('case-body-0').classList.add('show');
</script>

<script>
try{{
  var jornadaItem = {{
    materia: 'Histología II',
    titulo: '{titulo}',
    url: location.pathname,
    tipo: 'Guia de Estudo',
    etapa: 'P2',
    timestamp: Date.now()
  }};
  localStorage.setItem('clinicus_jornada_last_visited', JSON.stringify(jornadaItem));
}}catch(e){{}}
</script>
<script>
try{{
  if(typeof CHAPTER_ID !== 'undefined'){{
    var srsReg = JSON.parse(localStorage.getItem('clinicus_jornada_srs_registry') || '[]');
    var srsKey = 'clinicus_srs_' + CHAPTER_ID;
    var entry = {{ materia: 'Histología II', titulo: '{titulo}', url: location.pathname, srsKey: srsKey }};
    srsReg = srsReg.filter(function(e){{ return e.srsKey !== srsKey; }});
    srsReg.push(entry);
    localStorage.setItem('clinicus_jornada_srs_registry', JSON.stringify(srsReg));
  }}
}}catch(e){{}}
</script>
"""

def render_chapter_html(meta):
    objetivos_html = "".join(f"      <li>{o}</li>\n" for o in meta['objetivos'])
    atlas_html = "".join(
        f'      <div class="cmed-fig"><img src="{img["src"]}" alt="{img["alt"]}"><div class="cmed-fig-cap">{img["cap"]}</div></div>\n'
        for img in meta['atlas']
    )
    body = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title_tag']}</title>
<style>
{STYLE_CSS}
</style>
</head>
<body>
<div class="wrap">
<header>
  <span class="eyebrow">{meta['eyebrow']}</span>
  <h1>{meta['h1']}</h1>
  <p>ClinicusMed · Dossiê Clinicus — Padrão de Excelência</p>
</header>

<div class="xpbar">
  <span class="lvl" id="lvlLabel">Nv. 1</span>
  <div class="xpouter"><div class="xpinner" id="xpFill"></div></div>
  <span class="xptext" id="xpText">0 XP</span>
</div>

<nav class="tabs" id="tabs">
  <button data-p="p0" class="active">📋 Guia de Estudo</button>
  <button data-p="p1">🩺 Casos Clínicos</button>
  <button data-p="p2">🎥 Vídeo</button>
  <button data-p="p3">🃏 Flashcards</button>
  <button data-p="p4">✅ Banco de Questões</button>
  <button data-p="p5">🎮 Quiz Rápido</button>
  <button data-p="p6">🖼️ Atlas de Imagens</button>
</nav>

<!-- ============ GUIA DE ESTUDO ============ -->
<section class="panel active" id="p0">

  <div class="card">
    <h2>🎯 O que você vai conseguir fazer depois desse capítulo</h2>
    <ul>
{objetivos_html}    </ul>
  </div>

{meta['guia_extra_cards']}

  <div class="card">
    <h2>💪 Fixação rápida</h2>
    <div class="al-grid">
      <div class="al-box remember"><div class="al-title">✅ O que você deve lembrar</div>{meta['fixacao_lembrar']}</div>
      <div class="al-box errors"><div class="al-title">⚠️ Erro comum</div>{meta['fixacao_erro']}</div>
    </div>
  </div>

</section>

<!-- ============ CASOS CLÍNICOS ============ -->
<section class="panel" id="p1">
<div class="card">
    <h2>🩺 Caso Clínico Progressivo — {meta['caso_titulo']}</h2>
    <p style="color:var(--text-dim);font-size:.88em;">{meta['caso_intro']}</p>
  </div>
  <div id="casesArea"></div>
</section>

<!-- CMED-VIDEO-STYLE -->
<style>
{CMED_VIDEO_STYLE}
</style>
<!-- /CMED-VIDEO-STYLE -->

<!-- CMED-VIDEO-SECTION -->
{CMED_VIDEO_SECTION}
<!-- /CMED-VIDEO-SECTION -->

<!-- CMED-VIDEO-SCRIPT -->
{CMED_VIDEO_SCRIPT}
<!-- /CMED-VIDEO-SCRIPT -->

<!-- ============ FLASHCARDS ============ -->
<section class="panel" id="p3">
  <div class="card">
    <h2>🃏 Flashcards — SM-2 real + interface Anki</h2>
    <p style="font-size:.85em;color:var(--text-dim);">O sistema guarda, no seu navegador, quais cards você já sabe bem e quais precisam voltar mais cedo — cada vez que você avalia um card, ele recalcula quando ele deve voltar.</p>
    <div class="srs-status" id="srsStatus"></div>
    <div class="fc-filters" id="fcModeFilters">
      <button class="active" data-mode="due">📅 Revisão de Hoje</button>
      <button data-mode="all">📚 Todos os Cards</button>
    </div>
    <div class="fc-topbar">
      <span>Cartão <b id="fcIndex">1</b> / <b id="fcTotal">0</b></span>
      <span>Dominados: <b id="fcMastered">0</b></span>
    </div>
    <div class="fc-wrap">
      <div class="fc-card" id="fcCard">
        <div class="fc-inner">
          <div class="fc-face fc-front"><span class="fc-tag" id="fcTagFront">PERGUNTA</span><div id="fcFront"></div></div>
          <div class="fc-face fc-back"><span class="fc-tag">RESPOSTA</span><div id="fcBack"></div></div>
        </div>
      </div>
      <div class="fc-controls" id="fcNavControls">
        <button class="fc-btn" id="fcPrev">← Anterior</button>
        <button class="fc-btn primary" id="fcFlip">Virar</button>
        <button class="fc-btn" id="fcNext">Próxima →</button>
      </div>
      <div class="review-btns" id="reviewBtns" style="display:none;">
        <button class="btn-again" id="srsAgain">De novo<span class="interval-preview" id="prevAgain"></span></button>
        <button class="btn-hard" id="srsHard">Difícil<span class="interval-preview" id="prevHard"></span></button>
        <button class="btn-good" id="srsGood">Bem<span class="interval-preview" id="prevGood"></span></button>
        <button class="btn-easy" id="srsEasy">Fácil<span class="interval-preview" id="prevEasy"></span></button>
      </div>
      <div class="fc-shuffle-row">
        <button class="fc-btn" id="fcShuffle">🔀 Misturar</button>
      </div>
    </div>
  </div>
</section>

<!-- ============ BANCO DE QUESTÕES ============ -->
<section class="panel" id="p4">
  <div class="card">
    <h2>✅ Banco de Questões Comentadas</h2>
    <p style="font-size:.85em;color:var(--text-dim);">{len(meta['bank'])} questões, do mais básico ao mais puxado. Escolhe uma alternativa, depois clica em "Ver comentário completo" — vale a pena ler até quando você acerta, porque o comentário explica cada alternativa, não só a certa.</p>
    <div id="gabaritoList"></div>
  </div>
</section>

<!-- ============ QUIZ RÁPIDO ============ -->
<section class="panel" id="p5">
  <div class="card">
    <h2>🎮 Quiz Rápido</h2>
    <div id="quizArea"></div>
    <div class="quiz-result" id="quizResult"></div>
  </div>
</section>

<!-- ============ ATLAS DE IMAGENS ============ -->
<section class="panel" id="p6">
  <div class="card">
    <h2>🖼️ Atlas de Imagens — {meta['atlas_titulo']}</h2>
    <p style="font-size:.85em;color:var(--text-dim);">Todas as imagens desse capítulo, reunidas num só lugar pra revisão rápida.</p>
    <div class="cmed-gallery">
{atlas_html}    </div>
  </div>
</section>

<footer>ClinicusMed · Não basta ler. É preciso aprender, revisar e provar que sabe.</footer>
</div>
"""
    body += render_engine_script(meta['chapter_id'], meta['h1_plain'], meta['bank'], meta['flashcards'], meta['cases'])
    body += "\n</body></html>\n"
    return body

def write_chapter(filename, meta):
    path = os.path.join(CHDIR, filename)
    html = render_chapter_html(meta)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('OK:', filename, len(html), 'bytes')
