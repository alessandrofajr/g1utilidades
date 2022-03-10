import requests
import re

import pandas as pd
import lxml
from bs4 import BeautifulSoup
from flask import Flask, request, redirect, render_template, url_for

from downdetector import infos_downdetector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/votos-camara")
def votos_camara():
    return render_template(
        "votos-camara.html",
    )

@app.route("/votos-camara", methods=['POST'])
def votos_camara_post():
    votacao_form = request.form['votacao_camara']
    url = votacao_form
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    votacao = soup.find('div', class_='titulares')

    votos = []
    for li in votacao.select('li'):
        votos.append({x.get('class')[0]: x.text for x in li.select('span')})

    df = pd.DataFrame(votos)

    df = df.drop('votou', 1)
    df['voto'] = df['voto'].fillna('Ausente')
    df = df.replace({'voto' : {'Art. 17':'Não votou'}})
    df['nomePartido'] = df['nomePartido'].str.replace(r"([()])","")
    df[['nomePartido', 'UF']] = df['nomePartido'].str.split('-', 1, expand=True)
    df = df.drop('UF', 1)
    df = df.replace({'nomePartido' : {'Republican':'Republicanos', 
                        'Podemos':'PODE', 
                        'PCdoB':'PC do B',
                        'Solidaried':'SOLIDARIEDADE', 
                        'S.Part.':'S/Partido'}})
    df = df.replace({'nome' : {'Alencar S. Braga':'Alencar Santana Braga', 
                        "AlexandreSerfiotis":"Alexandre Serfiotis", 
                        'Arthur O. Maia':'Arthur Oliveira Maia', 
                        'Cap. Alberto Neto':'Capitão Alberto Neto', 
                        'Carlos Gaguim': 'Carlos Henrique Gaguim', 
                        'Cezinha Madureira': 'Cezinha de Madureira',
                        'Charlles Evangelis':'Charlles Evangelista',
                        'Chico D´Angelo':"Chico D'Angelo",
                        'Christiane Yared':'Christiane de Souza Yared',
                        'CoronelChrisóstom':'Coronel Chrisóstomo',
                        'Daniela Waguinho':'Daniela do Waguinho',
                        'Danrlei':'Danrlei de Deus Hinterholz',
                        'DelAntônioFurtado':'Delegado Antônio Furtado',
                        'Deleg. Éder Mauro':'Delegado Éder Mauro',
                        'Delegado Marcelo':'Delegado Marcelo Freitas',
                        'Dr Zacharias Calil':'Dr. Zacharias Calil',
                        'Dr. Sinval':'Dr. Sinval Malheiros',
                        'Dr.Luiz Antonio Jr':'Dr. Luiz Antonio Teixeira Jr.',
                        'Dra.Soraya Manato':'Dra. Soraya Manato',
                        'EdmilsonRodrigues':'Edmilson Rodrigues',
                        'EduardoBolsonaro':'Eduardo Bolsonaro',
                        'Emanuel Pinheiro N':'Emanuel Pinheiro Neto',
                        'EuclydesPettersen':'Euclydes Pettersen',
                        'Evair de Melo':'Evair Vieira de Melo',
                        'FelipeFrancischini':'Felipe Francischini',
                        'Félix Mendonça Jr':'Félix Mendonça Júnior',
                        'FernandaMelchionna':'Fernanda Melchionna',
                        'Fernando Coelho':'Fernando Coelho Filho',
                        'FernandoMonteiro':'Fernando Monteiro',
                        'FernandoRodolfo':'Fernando Rodolfo',
                        'Frei Anastacio':'Frei Anastacio Ribeiro',
                        'GilbertoNasciment':'Gilberto Nascimento',
                        'Gildenemyr':'Pastor Gildenemyr',
                        'Hercílio Diniz':'Hercílio Coelho Diniz',
                        'HermesParcianello':'Hermes Parcianello',
                        'Isnaldo Bulhões Jr':'Isnaldo Bulhões Jr.',
                        'Israel Batista':'Professor Israel Batista',
                        'João C. Bacelar':'João Carlos Bacelar',
                        'João Marcelo S.':'João Marcelo Souza',
                        'JoaquimPassarinho':'Joaquim Passarinho',
                        'José Airton':'José Airton Cirilo',
                        'Jose Mario Schrein':'Jose Mario Schreiner',
                        'Julio Cesar Ribeir':'Julio Cesar Ribeiro',
                        'Junio Amaral':'Cabo Junio Amaral',
                        'Lafayette Andrada':'Lafayette de Andrada',
                        'Leur Lomanto Jr.':'Leur Lomanto Júnior',
                        'Luiz P. O.Bragança':'Luiz Philippe de Orleans e Bragança',
                        'LuizAntônioCorrêa':'Luiz Antônio Corrêa',
                        'Marcos A. Sampaio':'Marcos Aurélio Sampaio',
                        'MargaridaSalomão':'Margarida Salomão',
                        'MárioNegromonte Jr':'Mário Negromonte Jr.',
                        'Maurício Dziedrick':'Maurício Dziedricki',
                        'Mauro Benevides Fº':'Mauro Benevides Filho',
                        'Nivaldo Albuquerq':'Nivaldo Albuquerque',
                        'Ottaci Nascimento':'Otaci Nascimento',
                        'Otto Alencar':'Otto Alencar Filho',
                        'Pastor Isidório':'Pastor Sargento Isidório',
                        'Paulo Martins':'Paulo Eduardo Martins',
                        'Paulo Pereira':'Paulo Pereira da Silva',
                        'Pedro A Bezerra':'Pedro Augusto Bezerra',
                        'Pedro Lucas Fernan':'Pedro Lucas Fernandes',
                        'Policial Sastre':'Policial Katia Sastre',
                        'Pr Marco Feliciano':'Pr. Marco Feliciano',
                        'Prof Marcivania':'Professora Marcivania',
                        'Profª Dorinha':'Professora Dorinha Seabra Rezende',
                        'Profª Rosa Neide':'Professora Rosa Neide',
                        'Professora Dayane':'Professora Dayane Pimentel',
                        'Rogério Peninha':'Rogério Peninha Mendonça',
                        'Roman':'Evandro Roman',
                        'Rubens Pereira Jr.': 'Rubens Pereira Jr',
                        'SóstenesCavalcante':'Sóstenes Cavalcante',
                        'Stephanes Junior':'Reinhold Stephanes Junior',
                        'SubtenenteGonzaga':'Subtenente Gonzaga',
                        'ToninhoWandscheer':'Toninho Wandscheer',
                        'Vitor Hugo':'Major Vitor Hugo',
                        'Wellington':'Wellington Roberto',
                        'WladimirGarotinho':'Wladimir Garotinho',
                        'Cap. Fábio Abreu':'Capitão Fábio Abreu',
                        'JosimarMaranhãozi':'Josimar Maranhãozinho',
                        'Bozzella':'Júnior Bozzella',
                        'Tadeu  Filippelli':'Tadeu Filippelli',
                        'Glaustin da Fokus':'Glaustin Fokus',
                        'Pastor Gil':'Pastor Gildenemyr',
                        'Marcelo Álvaro':'Marcelo Álvaro Antônio',
                        'Pedro Augusto':'Pedro Augusto Palareti',
                        'Pedro A Bezerra':'Pedro Augusto Bezerra',
                        'Paulo V. Caleffi':'Paulo Vicente Caleffi',
                        'Henrique Paraíso':'Henrique do Paraíso'}})
    df = df.iloc[df['nome'].str.normalize('NFKD').argsort()]    

    return render_template(
        "votos-camara.html",
        tables=[df.to_html(header=None, index=False)]
    )    

@app.route("/votos-senadores-1turno")
def votos_senadores_1turno():
    return render_template(
        "votos-senadores-1turno.html",
    )

@app.route("/votos-senadores-1turno", methods=['POST'])
def votos_senadores_1turno_post():
    
    partidos = pd.read_html('https://www25.senado.leg.br/web/senadores/em-exercicio/-/e/por-nome', encoding='utf-8')
    partidos_sen = partidos[0]
    partidos_sen.drop(['UF', 'Período', 'Telefones', 'Correio Eletrônico'], axis=1, inplace=True)
    
    url = request.form['votacao_senado_1turno']
    dfs = pd.read_html(url, encoding='utf-8')

    df_1turno = pd.concat([dfs[1], dfs[2], dfs[3]])
    df_1turno['Obs.'] = df_1turno['Obs.'].fillna('')
    df_1turno['voto'] = df_1turno[['Voto', 'Obs.']].agg(''.join, axis=1)
    df_1turno.drop(['#','Voto', 'Obs.'], axis=1, inplace=True)
    df_1turno = df_1turno.replace({'voto' : {'-art. 13, caput - Atividade parlamentar':'Ausente', 
                                             '-Presente (art. 40 - em Missão)':'Ausente',
                                             'art. 43, II - Licença particular':'Ausente',
                                             'art. 13, caput - Atividade parlamentar':'Ausente',
                                             'art. 43, I - Licença saúde':'Ausente',
                                             '-Presente (art. 40 - em Missão)': 'Ausente',
                                             '-Presente (art. 40 - em Missão)': 'Ausente',
                                             '-Não Compareceu':'Ausente',
                                             '-Não registrou voto':'Ausente', 
                                             '-Presidente (art. 51 RISF)':'Não votou'}})
    df_1turno = df_1turno.merge(partidos_sen.rename(columns={'Nome':'Parlamentar'}),how='outer')
    df_1turno = df_1turno.replace({'Partido' : {'PODEMOS':'PODE'}})
    df_1turno = df_1turno[['Parlamentar', 'Partido', 'voto']]

    return render_template(
        "votos-senadores-1turno.html",
        tables=[df_1turno.to_html(header=None, index=False)]
    )

@app.route("/votos-senadores-2turno")
def votos_senadores_2turno():
    return render_template(
        "votos-senadores-2turno.html",
    )

@app.route("/votos-senadores-2turno", methods=['POST'])
def votos_senadores_2turno_post():
    
    partidos = pd.read_html('https://www25.senado.leg.br/web/senadores/em-exercicio/-/e/por-nome', encoding='utf-8')
    partidos_sen = partidos[0]
    partidos_sen.drop(['UF', 'Período', 'Telefones', 'Correio Eletrônico'], axis=1, inplace=True)
    
    url = request.form['votacao_senado_2turno']
    dfs = pd.read_html(url, encoding='utf-8')

    df_2turno = pd.concat([dfs[5], dfs[6], dfs[7]])
    df_2turno['Obs.'] = df_2turno['Obs.'].fillna('')
    df_2turno['voto'] = df_2turno[['Voto', 'Obs.']].agg(''.join, axis=1)
    df_2turno.drop(['#','Voto', 'Obs.'], axis=1, inplace=True)
    df_2turno = df_2turno.replace({'voto' : {'-art. 13, caput - Atividade parlamentar':'Ausente', 
                                             '-Presente (art. 40 - em Missão)':'Ausente',
                                             'art. 43, II - Licença particular':'Ausente',
                                             'art. 13, caput - Atividade parlamentar':'Ausente',
                                             'art. 43, I - Licença saúde':'Ausente',
                                             '-Presente (art. 40 - em Missão)': 'Ausente',
                                             '-Presente (art. 40 - em Missão)': 'Ausente',
                                             '-Não Compareceu':'Ausente',
                                             '-Não registrou voto':'Ausente', 
                                             '-Presidente (art. 51 RISF)':'Não votou'}})
    df_2turno = df_2turno.merge(partidos_sen.rename(columns={'Nome':'Parlamentar'}),how='outer')
    df_2turno = df_2turno.replace({'Partido' : {'PODEMOS':'PODE'}})
    df_2turno = df_2turno[['Parlamentar', 'Partido', 'voto']]

    return render_template(
        "votos-senadores-2turno.html",
        tables=[df_2turno.to_html(header=None, index=False)]
    )  

@app.route("/downdetector")
def down():
    return render_template(
        "downdetector.html",
    )

@app.route("/downdetector", methods=['POST'])
def down_post():
    service_form = request.form['service']
    reports_form = request.form['reports']
    world_form = request.form['world']
    hoje, dia_t, dia_c, hora_c, hora_c_sub = infos_downdetector()

    titulo_1 = f"{service_form} apresenta instabilidade ao redor do mundo neste {dia_t}"
    linha_fina_1 = f'Plataforma ficou fora do ar para algumas pessoas por volta das {hora_c_sub}.'
    texto_1 = f'''Usuários ao redor do mundo relataram dificuldades para acessar o {service_form} neste {dia_c} ({hoje.strftime("%-d")}).
    O site Downdetector, que reúne relatos de instabilidade, registrou problemas por voltas das {hora_c_sub} com mais de {reports_form} reclamações.
    O g1 procurou o {service_form} e não teve retorno até a última atualização desta reportagem.'''

    titulo_2 = f'{service_form} apresenta instabilidade neste {dia_t}'
    linha_fina_2 = f'Plataforma ficou fora do ar para algumas pessoas por volta das {hora_c_sub}.'
    texto_2 = f'''Usuários no Brasil relataram dificuldades para acessar o {service_form} neste {dia_c} ({hoje.strftime("%-d")}).
    O site Downdetector, que reúne relatos de instabilidade, registrou problemas por voltas das {hora_c_sub} com mais de {reports_form} reclamações.
    O g1 procurou o {service_form} e não teve retorno até a última atualização desta reportagem.'''

    titulo_3 = f'{service_form} apresenta instabilidade nesta {dia_t}'
    linha_fina_3 = f'Plataforma ficou fora do ar para algumas pessoas por volta das {hora_c_sub}.'
    texto_3 = f'''Usuários ao redor do mundo relataram dificuldades para acessar o {service_form} nesta {dia_c} ({hoje.strftime("%-d")}).
    O site Downdetector, que reúne relatos de instabilidade, registrou problemas por voltas das {hora_c_sub} com mais de {reports_form} reclamações.
    O g1 procurou o {service_form} e não teve retorno até a última atualização desta reportagem.'''

    titulo_4 = f'{service_form} apresenta instabilidade nesta {dia_t}'
    linha_fina_4 = f'Plataforma ficou fora do ar para algumas pessoas por volta das {hora_c_sub}.'
    texto_4 = f'''Usuários no Brasil relataram dificuldades para acessar o {service_form} nesta {dia_c} ({hoje.strftime("%-d")}).
    O site Downdetector, que reúne relatos de instabilidade, registrou problemas por voltas das {hora_c_sub} com mais de {reports_form} reclamações.
    O g1 procurou o {service_form} e não teve retorno até a última atualização desta reportagem.'''

    if world_form == 'S' and dia_t in ['sábado','domingo']:
        titulo_return, linha_fina_return, texto_return = titulo_1, linha_fina_1, texto_1
    elif world_form == 'N' and dia_t in ['sábado','domingo']:
        titulo_return, linha_fina_return, texto_return = titulo_2, linha_fina_2, texto_2
    elif world_form == 'S' and dia_t not in ['sábado','domingo']:
        titulo_return, linha_fina_return, texto_return = titulo_3, linha_fina_3, texto_3
    else:
        titulo_return, linha_fina_return, texto_return = titulo_3, linha_fina_3, texto_3

    return render_template("downdetector.html", titulo = titulo_return, linha_fina = linha_fina_return, texto = texto_return)

@app.route("/compartilhar")
def my_form():
    return render_template(
        "compartilhar.html",
    )

@app.route("/compartilhar", methods=['POST'])
def my_form_post():
    text = request.form['text']
    link_whatsapp = f"https://api.whatsapp.com/send?text={text}?utm_source%3Dwhatsapp%26utm_medium%3Dshare-engagement%26utm_campaign%3Dte-materias"
    link_telegram = f"https://telegram.me/share/url?url={text}?utm_source%3Dtelegram%26utm_medium%3Dshare-engagement%26utm_campaign%3Dte-materias"
    return render_template(
        "compartilhar.html",
        whatsapp=link_whatsapp,
        telegram=link_telegram
    )
