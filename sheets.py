import gspread
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)

sheet = client.open("practice").sheet1

data = sheet.get_all_records()
col1 = sheet.col_values(1)
col2 = sheet.col_values(2)
col3 = sheet.col_values(3)
#pprint(col1)
sheet = client.open("practice").worksheet("sheet2")
#col1.copy()
sheet.insert_row(col1)
sheet = client.open("practice").worksheet("sheet3")
#col2.copy()
sheet.insert_row(col2)
sheet = client.open("practice").worksheet("sheet4")
#col2.copy()
sheet.insert_row(col3)



