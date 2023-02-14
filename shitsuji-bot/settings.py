import os

INSTALLED_APPS = ['GSHEET', 'RECIPE', 'TORRENT']
""" Sheet Settings """
columns = {
  'desc': 'A',
  'amount': 'C',
  'date': 'D',
  'category': 'B',
  'tip_ammount': 'P',
  'tip_date': 'Q',

  # cell
  'total': 'H17'
}
CAT = {
  'alq': 'Alquiler',
  'com': 'Comida',
  'ser': 'Servicios',
  'cas': 'Casa',
  'afu': 'Afuera',
  'sus': 'Sustancia',
  'gus': 'Gustos'
}
""" Telegram """
TOKEN = os.getenv('BOT_TOKEN')
""" Google Sheet """
WORKING_SHEET_ID = os.environ.get('WORKING_SHEET_ID')
SHEET_NAME = os.environ.get('SHEET_NAME')
SCOPE = [
  'https://www.googleapis.com/auth/spreadsheets',
  'https://www.googleapis.com/auth/drive',
]
""" Recipe API  """
RECIPE_URL = os.environ.get('RECIPE_URL')
RECIPE_APP_ID = os.environ.get('RECIPE_APP_ID')
RECIPE_APP_KEY = os.environ.get('RECIPE_APP_KEY')
CREDS_JSON = 'creds.json'
"""Torrent Downloader"""
TORRENT_PATH="/code/Films"