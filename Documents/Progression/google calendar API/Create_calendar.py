from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_1070385770691-brtd7htabnp363vvgqppemin71i4jno5.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION,SCOPES)

request_body = {
    'summary': 'test1'
}

response = service.calendars().insert(body=request_body).execute()
print(response)