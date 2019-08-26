import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open('hoja-prueba').sheet1

data = sheet.get_all_records()

print(data)