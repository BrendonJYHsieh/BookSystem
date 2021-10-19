from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'client_secret_1070385770691-brtd7htabnp363vvgqppemin71i4jno5.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION,SCOPES)

cal_id = 'q72f2r362o8tj2lfa68kmrla1g@group.calendar.google.com'

colors = service.colors().get().execute()
pprint(colors)

hour_adjustment = -8
event_body = {
    'start' : {
        'dateTime' : convert_to_RFC_datetime(2021, 10, 19, 20 + hour_adjustment, 00),
        'timeZone' : 'Asia/Taipei'
    },
    'end':{
        'dateTime' : convert_to_RFC_datetime(2021, 10, 19, 20 + hour_adjustment, 30),
        'timeZone' : 'Asia/Taipei'
    },
    'summary':'meeting',
    'description':'discussion',
    'colorId' : 2,
    'status':'confirmed',
    'transparency':'opaque',
    'visibility':'private',
    'location':'Taipei'
}

response = service.events().insert(
    calendarId=cal_id,
    body=event_body
).execute()

pprint(response)
