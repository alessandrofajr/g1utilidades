import requests
import re

from datetime import date
from datetime import datetime
from flask import Flask, request, redirect, render_template, url_for
from pytz import timezone

from downdetector import infos_downdetector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

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
        return render_template("downdetector.html",titulo = titulo_1, linha_fina = linha_fina_1, texto = texto_1)
    elif world_form == 'N' and dia_t in ['sábado','domingo']:
        return render_template("downdetector.html", titulo = titulo_2, linha_fina = linha_fina_2, texto = texto_2)
    elif world_form == 'S' and dia_t not in ['sábado','domingo']:
        return render_template("downdetector.html", titulo = titulo_3, linha_fina = linha_fina_3, texto = texto_3)
    else:
        return render_template("downdetector.html", titulo = titulo_4, linha_fina = linha_fina_4, texto = texto_4)

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
