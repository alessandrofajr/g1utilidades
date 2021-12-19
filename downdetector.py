import re

from datetime import date
from datetime import datetime
from pytz import timezone
import pytz

def infos_downdetector():
    hoje = datetime.now(pytz.timezone('America/Sao_Paulo')) #Puxa a data de hoje
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

    dia_t = dias_titulo[hoje.weekday()].lower() #Variável para o dia de hoje no título
    dia_c = dias[hoje.weekday()].lower() #Variável para o dia de hoje no texto
    hora = datetime.now(timezone('America/Sao_Paulo')) #Puxa a hora local
    hora_c = str((hora.strftime('%Hh%M'))) #Define o formato da hora
    hora_c_sub = re.sub(r"\w$", "0", hora_c) #Substitui o último dígito da hora por zero, para arredondar

    dia_t = dias_titulo[hoje.weekday()].lower()
    dia_c = dias[hoje.weekday()].lower()
    hora_c = (hora.strftime('%Hh%M'))

    return hoje, dia_t, dia_c, hora_c, hora_c_sub
