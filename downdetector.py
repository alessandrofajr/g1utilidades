import re

from datetime import date
from datetime import datetime
from flask import Flask, request, redirect, render_template, url_for
from pytz import timezone

def infos_downdetector():
    hoje = date.today() #Puxa a data de hoje
    dias_titulo = [ #Lista com os dias para entrar no título
      'segunda',
      'terça',
      'quarta',
      'quinta',
      'sexta',
      'sábado',
      'domingo'
    ]
    dias = [ #Lista com os dias para entrar no texto
      'segunda-feira',
      'terça-feira',
      'quarta-feira',
      'quinta-feira',
      'sexta-feira',
      'sábado',
      'domingo'
    ]

    dia_t_base = dias_titulo[hoje.weekday()].lower() #Variável para o dia de hoje no título
    dia_c_base = dias[hoje.weekday()].lower() #Variável para o dia de hoje no texto
    hora = datetime.now(timezone('America/Sao_Paulo')) #Puxa a hora local
    hora_c_base = str((hora.strftime('%Hh%M'))) #Define o formato da hora
    hora_c_sub_base = re.sub(r"\w$", "0", hora_c_base) #Substitui o último dígito da hora por zero, para arredondar

    dia_t_base = dias_titulo[hoje.weekday()].lower()
    dia_c_base = dias[hoje.weekday()].lower()
    hora_c_base = (hora.strftime('%Hh%M'))

    return hoje, dia_t_base, dia_c_base, hora_c_base, hora_c_sub_base