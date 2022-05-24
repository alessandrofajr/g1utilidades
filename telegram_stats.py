from datetime import date, timedelta, datetime
import json
from urllib.request import urlopen
import pandas as pd
from pytz import timezone
import pytz
import gspread
import base64

token = os.environ["TELEGRAM_TOKEN"]
channels = ['tsejus','jairbolsonarobrasil', 'LulanoTelegram', 'cirogomes']
channel_subs = []
extraction_date = [str(datetime.now(timezone('America/Sao_Paulo')))]*len(channels)

for channel in channels:
  url = f"https://api.telegram.org/bot{token}/getChatMembersCount?chat_id=@{channel}"
  with urlopen(url) as f:
    resp = json.load(f)
  channel_subs.append(resp.get('result')) 
  
df = pd.DataFrame({ 
    'channel' :channels,
    'subscribers':channel_subs,
    'extraction_date':extraction_date})

decoded_content = os.environ["GOOGLE_SHEETS_CREDENTIALS"] #Credenciais do Google Sheets
decoded_credentials = base64.b64decode(decoded_content)
credentials = json.loads(decoded_credentials)

spreadsheet_id = os.environ["GOOGLE_SHEET_ID_TELEGRAM"]
service_account = gspread.service_account_from_dict(credentials)
sh = service_account.open_by_key(spreadsheet_id)

worksheet = sh.add_worksheet(title=f"{date.today()}", rows="1", cols="1") #Adicionando o dataframe em uma worksheet do Google Sheets
set_with_dataframe(worksheet, df)
