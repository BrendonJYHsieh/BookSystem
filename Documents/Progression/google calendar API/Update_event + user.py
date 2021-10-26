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
        'dateTime' : convert_to_RFC_datetime(2021, 10, 22, 20 + hour_adjustment, 00),
        'timeZone' : 'Asia/Taipei'
    },
    'end':{
        'dateTime' : convert_to_RFC_datetime(2021, 10, 22, 20 + hour_adjustment, 30),
        'timeZone' : 'Asia/Taipei'
    },
    'summary':'meeting',
    'description':'discussion',
    'colorId' : 2,
    'attendees': [
        {'email': 'danielhuang9016@gmail.com'}
    ],
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

"""修改日曆
event_id = 'kndusifselqc69jacun96pr8bc'


response = service.events().get(
    calendarId=cal_id,
    eventId=event_id
).execute()

pprint(response)



start_datetime = convert_to_RFC_datetime(2021, 10, 19, 14 + hour_adjustment, 00)
end_datetime = convert_to_RFC_datetime(2021, 10, 19, 16 + hour_adjustment, 30)
response['start']['dateTime'] = start_datetime
response['end']['dateTime'] = end_datetime
response['summary'] = 'coding'
response['description'] = 'programming'

service.events().update(
    calendarId=cal_id,
    eventId=event_id,
    body=response).execute()


"""

"""加入成員
rule = {
    'scope': {
        'type': 'user',
        'value': 'danielhuang9016@gmail.com',
    },
    'role': 'writer'
}

created_rule = service.acl().insert(calendarId=cal_id, body=rule).execute()

pprint(created_rule['id'])
"""
