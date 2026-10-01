# -*- coding: utf-8 -*-
"""Capítulo 5 — Sistema Digestivo II: Esôfago, Estômago e Intestinos (Histología II, P2)"""

chapter_id = 'histologia2_cap05_digestivo2_tubo_digestivo'

meta = {
    'chapter_id': chapter_id,
    'title_tag': 'Histología II — Cap. 5: Sistema Digestivo II — Tubo Digestivo | ClinicusMed',
    'eyebrow': 'Histología II · Cátedra · Sistema Digestivo',
    'h1': '🫃 Capítulo 5 — Sistema Digestivo II: Esôfago, Estômago, Intestino Delgado e Grosso',
    'h1_plain': 'Capítulo 5 — Sistema Digestivo II: Esôfago, Estômago, Intestino Delgado e Grosso',
    'atlas_titulo': 'Esôfago, Estômago e Intestinos',

    'objetivos': [
        'Descrever as 4 túnicas do tubo digestivo e suas subcamadas',
        'Reconhecer a histologia do esôfago e seus plexos nervosos',
        'Diferenciar as 3 regiões histológicas do estômago e os 4 tipos celulares das glândulas fúndicas',
        'Descrever a estrutura da mucosa do intestino delgado (vilosidades, criptas, tipos celulares)',
        'Diferenciar duodeno, jejuno e íleon histologicamente',
        'Descrever as características da mucosa do intestino grosso e do apêndice vermiforme',
        'Reconhecer os plexos nervosos entéricos (Meissner e Auerbach) e sua localização',
    ],

    'guia_extra_cards': """
  <div class="card">
    <h2>🧱 As 4 Túnicas do Tubo Digestivo</h2>
    <div class="cmed-fig"><img src="img/atlas_cap5/tunicas_tubo_digestivo_comparativo.jpg" alt="Túnicas comparativas"><div class="cmed-fig-cap">Camadas do tubo digestivo — do esôfago ao intestino grosso</div></div>
    <div class="criterio"><b>🟢 Do estômago até o canal anal</b>, o tubo digestivo apresenta sempre 4 túnicas básicas.</div>
    <table>
      <tr><th>Túnica</th><th>Subcamadas</th><th>Função</th></tr>
      <tr><td><b>Mucosa</b></td><td>Epitélio + Lâmina própria (T.C. com glândulas, vasos, GALT) + Muscular da mucosa</td><td>Absorção, secreção, proteção — movimenta a mucosa</td></tr>
      <tr><td><b>Submucosa</b></td><td>T.C. denso irregular com plexos (Meissner), vasos e, às vezes, glândulas</td><td>Suporte e nutrição</td></tr>
      <tr><td><b>Muscular Externa</b></td><td>Músculo liso — circular interna + longitudinal externa (± oblíqua)</td><td>Mistura e propulsão do conteúdo (peristalse)</td></tr>
      <tr><td><b>Serosa/Adventícia</b></td><td>Peritônio (mesotélio+TC) OU adventícia no retroperitônio (só TC)</td><td>Fixação e revestimento externo</td></tr>
    </table>
    <div class="mnemo">🧠 <b>Mnemônico MSMS:</b> Mucosa → Submucosa → Muscular → Serosa (de dentro pra fora).</div>
  </div>

  <div class="card">
    <h2>🧵 Esôfago</h2>
    <p>Órgão muscular hueco interposto entre faringe e estômago, função de conduzir o bolo alimentar.</p>
    <table>
      <tr><th>Túnica</th><th>Características</th></tr>
      <tr><td><b>Mucosa</b></td><td>Epitélio plano estratificado NÃO queratinizado + lâmina própria (T.C. laxo, tecido linfoide) + muscular da mucosa (1 camada de músculo liso)</td></tr>
      <tr><td><b>Submucosa</b></td><td>T.C. denso não modelado com vasos, linfáticos, fibras nervosas e corpos ganglionares formando o <b>Plexo de Meissner</b>. Possui glândulas esofágicas tubuloacinosas</td></tr>
      <tr><td><b>Muscular</b></td><td>Circular interna + longitudinal externa (LECI). No TERÇO SUPERIOR é músculo estriado esquelético; no resto, liso. Entre as camadas: <b>Plexo Mientérico de Auerbach</b></td></tr>
      <tr><td><b>Adventícia/Serosa</b></td><td>T.C. laxo na porção torácica (adventícia); na porção abdominal vira serosa</td></tr>
    </table>
    <div class="hot"><b>💡 Hot Spot:</b> só o esôfago tem porção de músculo ESTRIADO esquelético na túnica muscular (terço superior) — isso é único entre os órgãos do tubo digestivo.</div>
  </div>

  <div class="card">
    <h2>🫃 Estômago — As 3 Regiões</h2>
    <p>Órgão muscular onde se produz a mistura dos alimentos (quimo). Divide-se histologicamente em 3 regiões conforme o tipo de glândula:</p>
    <table>
      <tr><th>Região</th><th>Glândulas</th></tr>
      <tr><td>Cárdia</td><td>Glândulas cárdicas (secretoras de muco)</td></tr>
      <tr><td>Fundo/Corpo</td><td>Glândulas FÚNDICAS (as mais importantes pra prova)</td></tr>
      <tr><td>Pilórica (antro)</td><td>Glândulas pilóricas</td></tr>
    </table>
    <div class="cmed-fig"><img src="img/atlas_cap5/celulas_estomago_principais_parietais.jpg" alt="Células do estômago"><div class="cmed-fig-cap">Células principais e parietais da glândula fúndica</div></div>
    <table>
      <tr><th>Célula da Glândula Fúndica</th><th>Secreta</th></tr>
      <tr><td><b>Mucosas do colo</b></td><td>Muco solúvel (líquido)</td></tr>
      <tr><td><b>Principais (zimogênicas)</b></td><td>Pepsinogênio (enzima)</td></tr>
      <tr><td><b>Parietais (oxínticas)</b></td><td>Fator intrínseco + ácido clorídrico (HCl)</td></tr>
      <tr><td><b>Enteroendócrinas (G)</b></td><td>Gastrina e outros hormônios (estimula/inibe)</td></tr>
    </table>
    <div class="clinical"><b>🔴 Correlação Clínica:</b> a destruição autoimune das células parietais causa gastrite atrófica, levando à falta de fator intrínseco e, consequentemente, anemia perniciosa (deficiência de vitamina B12).</div>
    <table>
      <tr><th>Túnica Gástrica</th><th>Detalhe</th></tr>
      <tr><td>Mucosa</td><td>Epitélio cilíndrico simples secretor de muco (viscoso/turvo) + lâmina própria com glândulas + muscular da mucosa (circular interna/longitudinal externa)</td></tr>
      <tr><td>Submucosa</td><td>T.C. denso, adiposo, vasos, plexo de Meissner</td></tr>
      <tr><td>Muscular</td><td>3 camadas: longitudinal externa, circular MÉDIA e oblíqua interna (LECIDI) + plexo de Auerbach</td></tr>
      <tr><td>Serosa</td><td>T.C. laxo + mesotélio</td></tr>
    </table>
    <div class="prova">📌 Pergunta clássica: "quantas camadas tem a muscular do estômago?" — 3 (longitudinal externa, circular média, oblíqua interna) — diferente das outras regiões do tubo, que têm só 2!</div>
  </div>

  <div class="card">
    <h2>🌀 Intestino Delgado</h2>
    <div class="cmed-fig"><img src="img/atlas_cap5/vilosidades_intestinais.jpg" alt="Vilosidades intestinais"><div class="cmed-fig-cap">Vilosidades intestinais — mais numerosas no duodeno e jejuno proximal</div></div>
    <div class="criterio"><b>🟢 Função principal:</b> absorção. Mede cerca de 5 metros, dividido em duodeno, jejuno e íleon.</div>
    <table>
      <tr><th>Célula da mucosa do ID</th><th>Função</th></tr>
      <tr><td>Absortivas (enterócitos)</td><td>Absorção — epitélio cilíndrico com microvilosidades</td></tr>
      <tr><td>Caliciformes</td><td>Secretam muco</td></tr>
      <tr><td>Células de Paneth</td><td>Regulação da flora bacteriana</td></tr>
      <tr><td>Enteroendócrinas</td><td>Hormônios (parecidas com as do estômago)</td></tr>
      <tr><td>Células-tronco pluripotenciais</td><td>Renovação do epitélio</td></tr>
      <tr><td>Células M</td><td>Associadas às placas de Peyer — sistema imunitário</td></tr>
    </table>
    <div class="cmed-fig"><img src="img/atlas_cap5/celulas_paneth.jpg" alt="Células de Paneth"><div class="cmed-fig-cap">Células de Paneth — no fundo das criptas de Lieberkühn</div></div>
    <table>
      <tr><th>Estrutura</th><th>Detalhe</th></tr>
      <tr><td>Pregas circulares (válvulas de Kerckring)</td><td>Mais desenvolvidas no jejuno</td></tr>
      <tr><td>Vilosidades intestinais</td><td>Mais numerosas no duodeno e jejuno proximal</td></tr>
      <tr><td>Criptas de Lieberkühn</td><td>Contêm as células de Paneth</td></tr>
      <tr><td>Submucosa</td><td>T.C. denso, plexo de Meissner. SÓ no duodeno: <b>glândulas de Brunner</b></td></tr>
    </table>
    <table>
      <tr><th>Segmento</th><th>Diferencial histológico</th></tr>
      <tr><td><b>Duodeno</b></td><td>ÚNICO com glândulas de Brunner na submucosa</td></tr>
      <tr><td><b>Jejuno</b></td><td>Válvulas de Kerckring, vilosidades e criptas AUMENTADAS. Muito vascularizado, abundante tecido linfoide</td></tr>
      <tr><td><b>Íleon</b></td><td>Vilosidades mais escassas, curtas e estreitas. Folículos linfoides = <b>placas de Peyer</b>, na parede oposta ao mesentério</td></tr>
    </table>
  </div>

  <div class="card">
    <h2>🌀 Intestino Grosso e Apêndice Vermiforme</h2>
    <div class="cmed-fig"><img src="img/atlas_cap5/tunicas_colon_numeradas.jpg" alt="Túnicas do colo"><div class="cmed-fig-cap">Túnicas do intestino grosso</div></div>
    <p>Última porção do tubo digestivo, da válvula ileocecal até o ânus. Rico em tecido linfoide pela grande população bacteriana.</p>
    <table>
      <tr><th>Túnica</th><th>Características</th></tr>
      <tr><td>Mucosa</td><td>Lisa, SEM vilosidades. Criptas de Lieberkühn mais longas e retas, SEM células de Paneth. Epitélio cilíndrico alto, muitas células caliciformes</td></tr>
      <tr><td>Lâmina própria</td><td>T.C. reticular rico em tecido linfoide (mas escasso devido às glândulas muito próximas). Folículos linfáticos frequentes, podendo invadir a submucosa</td></tr>
      <tr><td>Submucosa</td><td>T.C. laxo, tecido adiposo, plexo de Meissner</td></tr>
      <tr><td>Muscular</td><td>Circular interna COMPLETA; a longitudinal externa forma 3 faixas = <b>TÊNIAS do colo</b>. Plexo de Auerbach por fora da circular interna</td></tr>
      <tr><td>Serosa</td><td>Mesotélio + T.C. subseroso, com apêndices epiploicos</td></tr>
    </table>
    <div class="cmed-fig"><img src="img/atlas_cap5/apendice_vermiforme_foliculo.jpg" alt="Apêndice vermiforme"><div class="cmed-fig-cap">Apêndice vermiforme — folículos linfoides em camada quase contínua</div></div>
    <div class="criterio"><b>🟢 Apêndice vermiforme:</b> estrutura similar ao intestino grosso, mas com NOTÁVEL espessamento da parede por abundantes folículos linfoides, formando uma camada quase contínua de nódulos. Luz com contorno anguloso irregular, sem vilosidades, poucas glândulas de Lieberkühn e poucas células caliciformes.</div>
    <div class="cmed-fig"><img src="img/atlas_cap5/foliculo_linfatico_lamina_propria.jpg" alt="Folículo linfático"><div class="cmed-fig-cap">Folículo linfático na lâmina própria — MALT</div></div>
  </div>
""",

    'fixacao_lembrar': 'As 4 túnicas (de dentro pra fora): Mucosa → Submucosa → Muscular → Serosa/Adventícia. Esôfago: terço superior = músculo estriado. Estômago: 3 camadas musculares (LECIDI) e 4 tipos celulares nas glândulas fúndicas (mucosas do colo, principais, parietais, enteroendócrinas). Duodeno = único com glândulas de Brunner. Íleon = placas de Peyer. Intestino grosso = sem vilosidades, sem células de Paneth, tênias do colo. Plexo de Meissner = submucosa. Plexo de Auerbach = entre as camadas musculares.',
    'fixacao_erro': 'Trocar plexo de Meissner (submucoso) com plexo de Auerbach (mientérico, entre as camadas musculares). Confundir glândulas de Brunner (só duodeno) com as placas de Peyer (só íleon). Esquecer que o intestino grosso NÃO tem vilosidades nem células de Paneth — diferente do delgado. Achar que o estômago tem só 2 camadas musculares como o resto do tubo (na verdade tem 3: LECIDI).',

    'caso_titulo': 'Dor Abdominal e Má Absorção Progressiva',
    'caso_intro': 'Vamos acompanhar um paciente com queixas digestivas progressivas, relacionando o caso à histologia do esôfago, estômago e intestinos. O caso evolui em 3 níveis — clica em cada um pra ver como as coisas vão se desenrolando.',

    'cases': [
        {
            'nivel': '🟢 Nível 1 — Refluxo e esofagite',
            'hist': 'Paciente de 50 anos relata queimação retroesternal frequente, principalmente após refeições e ao deitar, há vários meses.',
            'dados': 'Endoscopia mostra hiperemia da mucosa esofágica distal, compatível com esofagite de refluxo.',
            'perguntas': [
                {'q': 'Por que a exposição crônica do esôfago ao conteúdo ácido do estômago causa inflamação, levando em conta a histologia da mucosa esofágica?', 'a': 'A mucosa do esôfago é revestida por epitélio plano estratificado NÃO queratinizado — um tipo de epitélio adaptado principalmente para resistir ao atrito mecânico da passagem do bolo alimentar, mas que não tem as mesmas defesas químicas especializadas que a mucosa gástrica desenvolveu pra se proteger do próprio ácido que ela produz (como a camada espessa de muco e bicarbonato do estômago). Quando o conteúdo ácido do estômago reflui cronicamente pro esôfago (por insuficiência do esfíncter esofágico inferior, por exemplo), esse epitélio esofágico fica exposto a um pH muito mais baixo do que o qual está fisiologicamente preparado para tolerar de forma repetida e prolongada. O resultado é dano direto às células epiteliais superficiais, gerando um processo inflamatório local (esofagite) que, se persistir cronicamente, pode até levar a alterações adaptativas do próprio epitélio (como a metaplasia intestinal observada no esôfago de Barrett, uma condição pré-maligna).'},
                {'q': 'O paciente também relata uma sensação de "globo" na garganta e episódios ocasionais de tosse seca. Como isso pode se relacionar à anatomia do esôfago?', 'a': 'O terço superior do esôfago é composto por músculo ESTRIADO esquelético (diferente do restante do órgão, que é músculo liso) — essa é uma característica histológica única do esôfago entre os órgãos do tubo digestivo. Essa musculatura estriada permite controle voluntário inicial da deglutição e também está intimamente relacionada, anatomicamente, à região da faringe e da laringe. Em quadros de refluxo mais pronunciado, o conteúdo ácido pode ascender além do esôfago distal e alcançar até essa porção superior e até estruturas laríngeas adjacentes (refluxo laringofaríngeo) — irritando a mucosa dessa região e gerando sintomas atípicos como a sensação de "globo" (globus faríngeo) e tosse crônica, que nem sempre são reconhecidos de imediato como relacionados ao refluxo gastroesofágico, mas que fazem sentido justamente pela proximidade anatômica entre o esôfago superior (com sua musculatura estriada) e as estruturas faringolaríngeas.'},
            ],
        },
        {
            'nivel': '🟡 Nível 2 — Gastrite atrófica e anemia perniciosa',
            'hist': 'Meses depois, o mesmo paciente retorna com fadiga progressiva, palidez e parestesias (formigamento) nas extremidades.',
            'dados': 'Exames laboratoriais mostram anemia macrocítica e deficiência de vitamina B12. Endoscopia revela atrofia da mucosa fúndica gástrica, com biópsia confirmando perda extensa de um tipo celular específico das glândulas fúndicas.',
            'perguntas': [
                {'q': 'Qual tipo celular das glândulas fúndicas está sendo destruído nesse quadro, e por que sua perda causa especificamente deficiência de vitamina B12?', 'a': 'O tipo celular destruído são as CÉLULAS PARIETAIS (também chamadas de oxínticas), que têm 2 funções secretoras principais na glândula fúndica: secretam ácido clorídrico (HCl) E secretam o FATOR INTRÍNSECO — uma glicoproteína indispensável para a absorção de vitamina B12 (cobalamina) no íleon terminal. Sem fator intrínseco suficiente, a vitamina B12 ingerida na dieta não consegue ser absorvida adequadamente pelo intestino delgado, mesmo que a ingestão alimentar esteja normal — é um problema de ABSORÇÃO, não de ingestão. Com o tempo, essa deficiência de B12 (um cofator essencial para a síntese de DNA, especialmente nas células de divisão rápida como as da medula óssea) leva à produção de hemácias anormalmente grandes e disfuncionais, causando a anemia macrocítica caracteristicamente chamada de anemia perniciosa. A deficiência de B12 também afeta a mielina dos nervos periféricos, explicando os sintomas neurológicos (parestesias) relatados pelo paciente.'},
                {'q': 'Por que esse quadro é chamado de gastrite "atrófica", e o que isso significa em termos da espessura/estrutura da mucosa gástrica observada na biópsia?', 'a': '"Atrófica" se refere à perda progressiva e extensa de tecido glandular funcional da mucosa gástrica (nesse caso, de origem autoimune — anticorpos atacando as células parietais e/ou o fator intrínseco). Como as glândulas fúndicas são responsáveis por boa parte da espessura e celularidade da mucosa do corpo/fundo gástrico, a destruição extensa e progressiva das células parietais (e frequentemente também das células principais) leva a um afinamento visível da mucosa na biópsia, com redução do número e da profundidade das glândulas — daí o termo "atrofia". Esse processo é diferente, por exemplo, de uma gastrite aguda (como por H. pylori ou AINEs), que tipicamente causa inflamação e dano agudo sem necessariamente o mesmo grau de perda estrutural glandular a longo prazo. A atrofia extensa das glândulas fúndicas também reduz a secreção de ácido (hipocloridria/acloridria), o que pode, inclusive, alterar o pH gástrico de forma a facilitar outras alterações da mucosa a longo prazo.'},
            ],
        },
        {
            'nivel': '🔴 Nível 3 — Doença de Crohn e diferenciação intestinal',
            'hist': 'Em um terceiro momento, o mesmo paciente — agora em investigação por diarreia crônica e perda de peso — é submetido a colonoscopia com ileoscopia e biópsias seriadas de diferentes segmentos do tubo digestivo.',
            'dados': 'O patologista recebe amostras de duodeno, jejuno, íleon e cólon, e precisa relatar os achados esperados em CADA segmento normal como controle comparativo antes de avaliar as áreas inflamadas.',
            'perguntas': [
                {'q': 'Que achado histológico, presente SOMENTE no duodeno entre todos os segmentos do intestino delgado, o patologista deve usar para confirmar que a biópsia realmente veio do duodeno e não de outro segmento?', 'a': 'A presença de GLÂNDULAS DE BRUNNER na submucosa é o achado histológico exclusivo e definidor do duodeno — nenhum outro segmento do intestino delgado (jejuno ou íleon) apresenta essas glândulas. As glândulas de Brunner são glândulas mucosas localizadas na submucosa (diferente das demais glândulas intestinais, que ficam na mucosa) e sua função é secretar um muco alcalino rico em bicarbonato, que ajuda a neutralizar o quimo ácido vindo do estômago assim que ele entra no duodeno — fazendo sentido anatomicamente, já que o duodeno é justamente o primeiro segmento do intestino delgado a receber esse conteúdo ácido gástrico, antes que ele siga para o jejuno e o íleon. Por isso, encontrar glândulas de Brunner na submucosa de uma biópsia é a forma mais confiável de identificar definitivamente que o tecido é do duodeno.'},
                {'q': 'E no caso do íleon, qual achado da lâmina própria/submucosa ajuda a diferenciá-lo do jejuno, e por que essa característica faz sentido funcionalmente nessa localização específica?', 'a': 'O achado característico do íleon são as PLACAS DE PEYER — grandes agregados de folículos linfoides que se estendem da lâmina própria até a submucosa, localizados preferencialmente na parede do intestino oposta à inserção do mesentério. Embora folículos linfoides isolados possam ser encontrados ao longo de todo o intestino delgado, é no íleon que eles se tornam especialmente proeminentes e organizados nessas estruturas maiores chamadas placas de Peyer. Isso faz sentido funcionalmente porque o íleon é o segmento final do intestino delgado, imediatamente antes da válvula ileocecal e da enorme população bacteriana do intestino grosso — posicionar uma vigilância imunológica intensificada (através dessas placas, que contêm células M especializadas em capturar antígenos e apresentá-los ao sistema imune) justamente nessa transição é uma estratégia que ajuda a monitorar e responder a patógenos antes que o conteúdo intestinal passe para o cólon, rico em bactérias comensais que precisam ser toleradas, mas também vigiadas quanto a potenciais invasores patogênicos.'},
            ],
        },
    ],

    'bank': [
        {
            'n': 1, 'tema': 'Túnicas do Tubo Digestivo', 'nivel': '🟢 Nível 1 — Essencial',
            'objetivo': 'Descrever as 4 túnicas do tubo digestivo',
            'q': 'Quais são as 4 túnicas do tubo digestivo, de dentro pra fora?',
            'opts': ['Mucosa, Submucosa, Muscular, Serosa/Adventícia', 'Epitélio, Lâmina própria, Muscular, Adventícia', 'Mucosa, Muscular, Submucosa, Serosa', 'Endotélio, Mesotélio, Muscular, Serosa'],
            'correct': 0,
            'justificativa': 'De dentro pra fora: Mucosa (epitélio+lâmina própria+muscular da mucosa) → Submucosa → Muscular Externa → Serosa/Adventícia.',
            'analise': ['Incorreto — epitélio e lâmina própria são subcamadas DA mucosa, não túnicas independentes.', 'Incorreto — a ordem está errada; a submucosa vem ANTES da muscular, não depois.', 'Incorreto — endotélio e mesotélio são tipos de epitélio específicos, não túnicas do tubo digestivo.'],
            'analise_letters': ['B', 'C', 'D'],
            'conceito': 'MSMS: Mucosa → Submucosa → Muscular → Serosa/Adventícia.',
            'pegadinha': 'É a base estrutural de todo o capítulo — decore a ordem exata e as subcamadas de cada túnica.',
            'dica': 'Pensa de dentro (luz) pra fora (cavidade abdominal): M-S-M-S.',
        },
        {
            'n': 2, 'tema': 'Esôfago', 'nivel': '🟢 Nível 1 — Essencial',
            'objetivo': 'Reconhecer a histologia do esôfago',
            'q': 'Qual tipo de epitélio reveste a mucosa do esôfago?',
            'opts': ['Cilíndrico simples', 'Plano estratificado não queratinizado', 'Cúbico simples', 'Pseudoestratificado ciliado'],
            'correct': 1,
            'justificativa': 'A mucosa esofágica tem epitélio de revestimento plano estratificado NÃO queratinizado — adaptado ao atrito da passagem do bolo alimentar.',
            'analise': ['Incorreto — epitélio cilíndrico simples é típico do estômago e intestinos, não do esôfago.', 'Incorreto — epitélio cúbico simples é encontrado em conductos glandulares, não na mucosa esofágica.', 'Incorreto — pseudoestratificado ciliado é típico das vias respiratórias, não do esôfago.'],
            'analise_letters': ['A', 'C', 'D'],
            'conceito': 'Esôfago: epitélio plano estratificado NÃO queratinizado.',
            'pegadinha': 'Não confundir com a pele ou mucosa masticatória bucal, que SÃO queratinizadas — o esôfago não é.',
            'dica': 'O esôfago sofre atrito, mas não precisa de queratina como a pele (ambiente úmido/lubrificado).',
        },
        {
            'n': 3, 'tema': 'Esôfago — Musculatura', 'nivel': '🟡 Nível 2 — Aprofundamento',
            'objetivo': 'Reconhecer a particularidade muscular do esôfago',
            'q': 'Qual característica da túnica muscular é ÚNICA do esôfago entre os órgãos do tubo digestivo?',
            'opts': ['Tem 3 camadas musculares como o estômago', 'O terço superior é composto por músculo ESTRIADO esquelético', 'Não tem plexo mientérico', 'É o único sem muscular da mucosa'],
            'correct': 1,
            'justificativa': 'O esôfago é o único órgão do tubo digestivo cujo terço superior da túnica muscular é composto por músculo ESTRIADO esquelético (o restante é músculo liso, como no resto do tubo).',
            'analise': ['Incorreto — o esôfago tem só 2 camadas musculares (circular interna + longitudinal externa/LECI), diferente do estômago que tem 3.', 'Incorreto — o esôfago TEM plexo mientérico de Auerbach, entre as camadas musculares.', 'Incorreto — o esôfago TEM muscular da mucosa, como os demais órgãos do tubo.'],
            'analise_letters': ['A', 'C', 'D'],
            'conceito': 'Esôfago: terço superior = músculo estriado esquelético (permite controle voluntário inicial da deglutição).',
            'pegadinha': 'É um detalhe MUITO cobrado em prova — associe "esôfago = único com músculo estriado no tubo digestivo".',
            'dica': 'Começo da deglutição é voluntário → precisa de músculo estriado no início do esôfago.',
        },
        {
            'n': 4, 'tema': 'Glândulas Fúndicas', 'nivel': '🟢 Nível 1 — Essencial',
            'objetivo': 'Identificar os 4 tipos celulares das glândulas fúndicas',
            'q': 'Qual célula da glândula fúndica gástrica secreta fator intrínseco e ácido clorídrico?',
            'opts': ['Células principais', 'Células mucosas do colo', 'Células parietais (oxínticas)', 'Células enteroendócrinas'],
            'correct': 2,
            'justificativa': 'As células parietais (oxínticas) secretam fator intrínseco (essencial pra absorção de B12) e ácido clorídrico (HCl).',
            'analise': ['Incorreto — as células principais secretam pepsinogênio (enzima), não ácido nem fator intrínseco.', 'Incorreto — as células mucosas do colo secretam muco solúvel.', 'Incorreto — as enteroendócrinas (células G) secretam gastrina e outros hormônios.'],
            'analise_letters': ['A', 'B', 'D'],
            'conceito': 'Células parietais = HCl + fator intrínseco.',
            'pegadinha': 'A destruição autoimune das parietais causa anemia perniciosa por falta de fator intrínseco (não por falta de ácido).',
            'dica': 'Parietal = Produz ácido (lembra "P" de parietal e "P" de prótons/H+).',
        },
        {
            'n': 5, 'tema': 'Estômago — Musculatura', 'nivel': '🟡 Nível 2 — Aprofundamento',
            'objetivo': 'Reconhecer a particularidade muscular do estômago',
            'q': 'Quantas camadas tem a túnica muscular do estômago, e como se chamam?',
            'opts': ['2 camadas: circular interna e longitudinal externa', '3 camadas: longitudinal externa, circular média e oblíqua interna (LECIDI)', '4 camadas incluindo uma transversal', '1 camada única de músculo liso'],
            'correct': 1,
            'justificativa': 'O estômago tem 3 camadas musculares (diferente do resto do tubo, que tem 2): longitudinal externa, circular MÉDIA (intermediária) e oblíqua/diagonal interna — mnemônico LECIDI.',
            'analise': ['Incorreto — 2 camadas é o padrão do resto do tubo digestivo (esôfago, intestinos), não do estômago.', 'Incorreto — não existe uma 4ª camada transversal descrita classicamente.', 'Incorreto — o estômago definitivamente tem mais de uma camada muscular, essenciais pra função de mistura do quimo.'],
            'analise_letters': ['A', 'C', 'D'],
            'conceito': 'Estômago = 3 camadas musculares (LECIDI) — exceção às 2 camadas do resto do tubo.',
            'pegadinha': 'É a exceção mais cobrada: o estômago tem uma camada muscular A MAIS que o resto do tubo digestivo.',
            'dica': 'O estômago precisa "amassar" bem o alimento (quimo) — por isso tem uma 3ª camada oblíqua.',
        },
        {
            'n': 6, 'tema': 'Plexos Nervosos Entéricos', 'nivel': '🟡 Nível 2 — Aprofundamento',
            'objetivo': 'Localizar os plexos de Meissner e Auerbach',
            'q': 'Onde se localizam, respectivamente, o plexo de Meissner e o plexo de Auerbach?',
            'opts': ['Meissner na mucosa; Auerbach na serosa', 'Meissner na submucosa; Auerbach entre as camadas musculares (mientérico)', 'Ambos ficam na submucosa', 'Meissner na muscular; Auerbach na mucosa'],
            'correct': 1,
            'justificativa': 'O plexo de Meissner (submucoso) fica na túnica submucosa. O plexo de Auerbach (mientérico) fica ENTRE as camadas circular interna e longitudinal externa da túnica muscular.',
            'analise': ['Incorreto — Meissner não fica na mucosa propriamente, e Auerbach não fica na serosa.', 'Incorreto — só o Meissner fica na submucosa; o Auerbach fica na muscular (entre suas camadas).', 'Incorreto — a localização está trocada entre os dois plexos.'],
            'analise_letters': ['A', 'C', 'D'],
            'conceito': 'Meissner = submucoso. Auerbach = mientérico (entre as camadas musculares).',
            'pegadinha': 'Confusão clássica de prova — decore: "Meissner-Submucoso" (ambos com S), "Auerbach-Músculo/mientérico" (entre as 2 camadas).',
            'dica': 'MeiSSner = SubmucoSo (letra S em comum). Auerbach = entre os músculos (mio=músculo).',
        },
        {
            'n': 7, 'tema': 'Intestino Delgado — Duodeno', 'nivel': '🟡 Nível 2 — Aprofundamento',
            'objetivo': 'Diferenciar duodeno de jejuno e íleon',
            'q': 'Qual estrutura histológica está presente EXCLUSIVAMENTE na submucosa do duodeno, entre os 3 segmentos do intestino delgado?',
            'opts': ['Glândulas de Brunner', 'Placas de Peyer', 'Válvulas de Kerckring', 'Criptas de Lieberkühn'],
            'correct': 0,
            'justificativa': 'As glândulas de Brunner, na submucosa, são exclusivas do duodeno — secretam muco alcalino rico em bicarbonato pra neutralizar o quimo ácido vindo do estômago.',
            'analise': ['Incorreto — placas de Peyer são características do ÍLEON, não do duodeno.', 'Incorreto — válvulas de Kerckring (pregas circulares) estão mais desenvolvidas no JEJUNO, mas existem em vários segmentos.', 'Incorreto — criptas de Lieberkühn existem em TODO o intestino delgado (e grosso), não são exclusivas do duodeno.'],
            'analise_letters': ['B', 'C', 'D'],
            'conceito': 'Duodeno = ÚNICO segmento com glândulas de Brunner na submucosa.',
            'pegadinha': 'É O achado histológico definidor do duodeno — se aparecer na prova, é duodeno com certeza.',
            'dica': 'Brunner = primeiro a receber o ácido → precisa neutralizar rápido (bicarbonato).',
        },
        {
            'n': 8, 'tema': 'Intestino Delgado — Íleon', 'nivel': '🟡 Nível 2 — Aprofundamento',
            'objetivo': 'Reconhecer as placas de Peyer',
            'q': 'Onde se localizam preferencialmente as placas de Peyer no íleon?',
            'opts': ['Na parede oposta à inserção do mesentério', 'Exclusivamente na submucosa duodenal', 'Apenas no epitélio de revestimento', 'Na túnica serosa'],
            'correct': 0,
            'justificativa': 'As placas de Peyer (agregados de folículos linfoides) se localizam preferencialmente na parede do íleon OPOSTA à inserção do mesentério.',
            'analise': ['Incorreto — placas de Peyer são do íleon, não do duodeno (que tem glândulas de Brunner).', 'Incorreto — placas de Peyer se estendem da lâmina própria até a submucosa, não ficam restritas ao epitélio.', 'Incorreto — a serosa é a camada mais externa, não é onde ficam as placas de Peyer.'],
            'analise_letters': ['B', 'C', 'D'],
            'conceito': 'Placas de Peyer = folículos linfoides agregados, íleon, parede antimesentérica.',
            'pegadinha': 'Localização específica (antimesentérica) é frequentemente cobrada — não é em qualquer lugar da parede.',
            'dica': 'Peyer no íleon = vigilância imune antes do cólon (rico em bactérias).',
        },
        {
            'n': 9, 'tema': 'Intestino Grosso', 'nivel': '🟠 Nível 3 — Excelência',
            'objetivo': 'Diferenciar a mucosa do intestino grosso da do delgado',
            'q': 'Quais 2 características da mucosa do intestino delgado estão AUSENTES no intestino grosso?',
            'opts': ['Epitélio cilíndrico e células caliciformes', 'Vilosidades intestinais e células de Paneth', 'Criptas de Lieberkühn e lâmina própria', 'Muscular da mucosa e submucosa'],
            'correct': 1,
            'justificativa': 'O intestino grosso NÃO tem vilosidades intestinais (mucosa lisa) nem células de Paneth nas suas criptas de Lieberkühn (que são mais longas e retas que as do delgado).',
            'analise': ['Incorreto — o intestino grosso TEM epitélio cilíndrico e TEM (até mais) células caliciformes do que o delgado.', 'Incorreto — o intestino grosso TEM criptas de Lieberkühn (só que sem Paneth) e TEM lâmina própria.', 'Incorreto — o intestino grosso tem as 4 túnicas normalmente, incluindo muscular da mucosa e submucosa.'],
            'analise_letters': ['A', 'C', 'D'],
            'conceito': 'Intestino grosso: SEM vilosidades + SEM células de Paneth (diferente do delgado).',
            'pegadinha': 'É um erro clássico achar que o intestino grosso também tem vilosidades — ele NÃO tem (mucosa lisa).',
            'dica': 'Grosso = liso por fora (sem vilosidades) mas "grosso" de muco (muitas caliciformes).',
        },
        {
            'n': 10, 'tema': 'Apêndice Vermiforme', 'nivel': '🟠 Nível 3 — Excelência',
            'objetivo': 'Reconhecer a histologia do apêndice vermiforme',
            'q': 'Qual é a característica histológica MAIS marcante do apêndice vermiforme, que causa notável espessamento de sua parede?',
            'opts': ['Grande quantidade de glândulas de Brunner', 'Presença de placas de Peyer gigantes', 'Abundantes folículos linfoides formando camada quase contínua', 'Ausência completa de muscular externa'],
            'correct': 2,
            'justificativa': 'O apêndice tem estrutura similar ao intestino grosso, mas com notável espessamento da parede por abundantes folículos linfoides, formando uma camada quase contínua de pequenos a grandes nódulos linfoides.',
            'analise': ['Incorreto — glândulas de Brunner são exclusivas do duodeno, não do apêndice.', 'Incorreto — placas de Peyer são do íleon; o apêndice tem folículos linfoides abundantes, mas não é descrito como "placas de Peyer gigantes".', 'Incorreto — o apêndice TEM muscular externa, como o resto do intestino grosso.'],
            'analise_letters': ['A', 'B', 'D'],
            'conceito': 'Apêndice vermiforme = tecido linfoide MUITO abundante (quase contínuo) espessando a parede.',
            'pegadinha': 'A luz do apêndice tem contorno anguloso irregular, sem vilosidades, com poucas glândulas de Lieberkühn e poucas caliciformes — mas MUITO tecido linfoide.',
            'dica': 'Apêndice = "órgão linfoide disfarçado de intestino" — por isso é tão suscetível a inflamação/apendicite quando obstrui.',
        },
    ],

    'flashcards': [
        {'n': 1, 'cat': 'Túnicas', 'f': 'Quais são as 4 túnicas do tubo digestivo?', 'b': 'Mucosa, Submucosa, Muscular Externa, Serosa/Adventícia (de dentro pra fora).'},
        {'n': 2, 'cat': 'Túnicas', 'f': 'Quais as 3 subcamadas da túnica mucosa?', 'b': 'Epitélio, Lâmina própria (T.C. com glândulas/vasos/GALT) e Muscular da mucosa.'},
        {'n': 3, 'cat': 'Esôfago', 'f': 'Que tipo de epitélio reveste o esôfago?', 'b': 'Plano estratificado NÃO queratinizado.'},
        {'n': 4, 'cat': 'Esôfago', 'f': 'Qual parte do esôfago tem músculo estriado esquelético?', 'b': 'O terço superior — único segmento do tubo digestivo com essa característica.'},
        {'n': 5, 'cat': 'Estômago', 'f': 'Quais os 4 tipos celulares das glândulas fúndicas e o que secretam?', 'b': 'Mucosas do colo (muco), Principais (pepsinogênio), Parietais (HCl + fator intrínseco), Enteroendócrinas/G (gastrina).'},
        {'n': 6, 'cat': 'Estômago', 'f': 'Quantas e quais são as camadas musculares do estômago?', 'b': '3 camadas: Longitudinal externa, Circular média, Oblíqua/diagonal interna (LECIDI).'},
        {'n': 7, 'cat': 'Plexos Nervosos', 'f': 'Onde ficam os plexos de Meissner e Auerbach?', 'b': 'Meissner = submucosa. Auerbach = mientérico, entre as camadas musculares.'},
        {'n': 8, 'cat': 'Intestino Delgado', 'f': 'O que é exclusivo da submucosa do duodeno?', 'b': 'Glândulas de Brunner — secretam muco alcalino rico em bicarbonato.'},
        {'n': 9, 'cat': 'Intestino Delgado', 'f': 'O que caracteriza o íleon histologicamente?', 'b': 'Vilosidades mais escassas/curtas + Placas de Peyer na parede oposta ao mesentério.'},
        {'n': 10, 'cat': 'Intestino Delgado', 'f': 'Quais células ficam no fundo das criptas de Lieberkühn e regulam a flora bacteriana?', 'b': 'Células de Paneth.'},
        {'n': 11, 'cat': 'Intestino Grosso', 'f': 'Quais 2 características do delgado estão AUSENTES no intestino grosso?', 'b': 'Vilosidades intestinais e células de Paneth.'},
        {'n': 12, 'cat': 'Intestino Grosso', 'f': 'O que forma as tênias do colo?', 'b': 'A camada longitudinal externa da muscular, que se organiza em 3 faixas (ao invés de circundar toda a circunferência).'},
    ],

    'atlas': [
        {'src': 'img/atlas_cap5/tunicas_tubo_digestivo_comparativo.jpg', 'alt': 'Túnicas comparativas', 'cap': 'Túnicas do Tubo Digestivo — Visão Comparativa'},
        {'src': 'img/atlas_cap5/celulas_estomago_principais_parietais.jpg', 'alt': 'Células do estômago', 'cap': 'Células Principais e Parietais'},
        {'src': 'img/atlas_cap5/vilosidades_intestinais.jpg', 'alt': 'Vilosidades intestinais', 'cap': 'Vilosidades Intestinais'},
        {'src': 'img/atlas_cap5/celulas_paneth.jpg', 'alt': 'Células de Paneth', 'cap': 'Células de Paneth'},
        {'src': 'img/atlas_cap5/tunicas_colon_numeradas.jpg', 'alt': 'Túnicas do colo', 'cap': 'Túnicas do Intestino Grosso'},
        {'src': 'img/atlas_cap5/apendice_vermiforme_foliculo.jpg', 'alt': 'Apêndice vermiforme', 'cap': 'Apêndice Vermiforme — Folículos Linfoides'},
        {'src': 'img/atlas_cap5/foliculo_linfatico_lamina_propria.jpg', 'alt': 'Folículo linfático', 'cap': 'Folículo Linfático na Lâmina Própria'},
    ],
}
