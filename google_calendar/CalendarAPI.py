from pprint import pprint
from google_calendar.Google import Create_Service, convert_to_RFC_datetime

class calendar_API:
    
    def __init__(self):
        self.CLIENT_SECRET_FILE = 'google_calendar\client_secret.json'
        self.API_NAME = 'calendar'
        self.API_VERSION = 'v3'
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.service = Create_Service(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCOPES)
        self.cal = []

    def find_calendar(self, name):
        for i in range(len(self.cal)):
            if self.cal[i].name == name:
                return i

    def Create_Calendar(self, name):
        request_body = {
            'summary': name
        }
        response = self.service.calendars().insert(body=request_body).execute()
        print("Calendar Created")
        tmp = Calendar(name,response['id'],self.service)
        self.cal.append(tmp)

    def Update_Calendar(self, name, New_name):
        a = self.find_calendar(name)
        self.cal[a].name = New_name
        request_body = {
            'summary': New_name
        }
        self.service.calendars().update(calendarId=self.cal[a].id,body=request_body).execute()
        print("Calendar Updated")

    def Delete_Calendar(self, name):
        a = self.find_calendar(name)
        self.service.calendars().delete(calendarId=self.cal[a].id).execute()
        print("Calendar Deleted")

    def Create_Event(self, roomname, name, description, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute):
        a = self.find_calendar(roomname)
        self.cal[a].Create_Event(name, description, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute)
    
    def Delete_Event(self, roomname, eventid):
        a = self.find_calendar(roomname)
        self.cal[a].Delete_Event(eventid)

    def Update_Summary(self, roomname, eventid, summary):
        a = self.find_calendar(roomname)
        self.cal[a].Update_Summary(eventid, summary)

    def Update_Description(self, roomname, eventid, description):
        a = self.find_calendar(roomname)
        self.cal[a].Update_Description(eventid, description)

    def Update_Attendee(self, roomname, eventid, attendee):
        a = self.find_calendar(roomname)
        self.cal[a].Update_Attendee(eventid, attendee)

    def Update_Time(self, roomname, eventid, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute):
        a = self.find_calendar(roomname)
        self.cal[a].Update_Time(eventid, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute)

    def Delete_Attendee(self, roomname, eventid, attendee):
        a = self.find_calendar(roomname)
        self.cal[a].Delete_Attendee(eventid, attendee)

class Calendar(calendar_API):

    def __init__(self, name, id, service):
        self.name = name
        self.id = id
        self.event_id = []
        self.event_body = []
        self.invited = []
        self.service = service

    def Create_Event(self, name, description, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute):
        hour_adjustment = -8
        request_body = {
            'start' : {
                'dateTime' : convert_to_RFC_datetime(start_year, start_month, start_day, start_hour + hour_adjustment, start_minute),
                'timeZone' : 'Asia/Taipei'
            },
            'end':{
                'dateTime' : convert_to_RFC_datetime(end_year, end_month, end_day, end_hour + hour_adjustment, end_minute),
                'timeZone' : 'Asia/Taipei'
            },
            'summary': name,
            'description':description,
            'attendees':[

            ],
            'colorId' : 2,
            'status':'confirmed',
            'transparency':'opaque',
            'visibility':'private',
        }
        response = self.service.events().insert(
            calendarId=self.id,
            body=request_body
        ).execute()
        print("Event Created")
        self.event_id.append(response['id'])
        self.event_body.append(request_body)
        print(response['id'])
        return response['id']

    def find_event(self, eventid):
        for i in range(len(self.event_id)):
            if self.event_id[i] == eventid:
                return i

    def Update_Summary(self, eventid, summary):
        a = self.find_event(eventid)
        self.event_body[a]['summary'] = summary
        self.service.events().update(
        calendarId = self.id,
        eventId = self.event_id[a],
        body = self.event_body[a]).execute()
        print("Event summary updated")

    def Update_Description(self, eventid, description):
        a = self.find_event(eventid)
        self.event_body[a]['description'] = description
        self.service.events().update(
        calendarId = self.id,
        eventId = self.event_id[a],
        body = self.event_body[a]).execute()
        print("Event description updated")

    def find_attendee(self, name):
        for i in range(len(self.invited)):
            if self.invited[i] == name:
                return i

    def Update_Attendee(self, eventid, attendee):
        a = self.find_event(eventid)
        add_attendees = {
            "email": attendee
        }
        self.invited.append(attendee)
        self.attendees = self.event_body[a]['attendees']
        self.attendees.append(add_attendees)
        body = {
            "attendees": self.attendees
        }
        self.service.events().patch(
        calendarId = self.id,
        eventId = self.event_id[a],
        body=body).execute()
        print("Event attendee updated")

    def Update_Time(self, eventid, start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute):
        a = self.find_event(eventid)
        hour_adjustment = -8
        start_datetime = convert_to_RFC_datetime(start_year, start_month, start_day, start_hour + hour_adjustment, start_minute)
        end_datetime = convert_to_RFC_datetime(end_year, end_month, end_day, end_hour + hour_adjustment, end_minute)
        self.event_body[a]['start']['dateTime'] = start_datetime
        self.event_body[a]['end']['dateTime'] = end_datetime
        self.service.events().update(
        calendarId = self.id,
        eventId = self.event_id[a],
        body=self.event_body[a]).execute()
        print("Event time updated")

    def Delete_Attendee(self, eventid, attendee):
        a = self.find_event(eventid)
        b = self.find_attendee(attendee)
        self.attendees.pop(b)
        body = {
            "attendees": self.attendees
        }
        self.service.events().patch(
        calendarId = self.id,
        eventId = self.event_id[a],
        body=body).execute()
        self.invited.pop(b)
        print("Attendee Deleted")

    def Delete_Event(self, eventid):
        a = self.find_event(eventid)
        self.service.events().delete(
        calendarId = self.id,
        eventId = self.event_id[a]
        ).execute()
        self.event_id.pop(a)
        self.event_name.pop(a)
        print("Event Deleted")


#from CalendarAPI import calendar_API

#Cal = calendar_API()
#Cal.Create_Calendar('test789')
#Cal.Create_Event('test789','meeting','project discussion',2021,11,30,15,00,2021,11,30,19,00)
#Cal.Update_Summary('test789',id,'coding')
#Cal.Update_Description('test789',id,'coding this project')
#Cal.Update_Time('test789',id,2021,11,2,20,00,2021,11,2,23,30)
#Cal.Update_Attendee('test789',id,'danielwind9016@gmail.com')
#Cal.Delete_Attendee('test789',id,'danielwind9016@gmail.com')
#Cal.Delete_Event('test789',id)
#Cal.Update_Calendar('test789','test123')
#Cal.Delete_Calendar('test789')