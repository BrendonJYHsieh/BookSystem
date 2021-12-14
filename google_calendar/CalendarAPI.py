from pprint import pprint
from google_calendar.Google import Create_Service

class calendar_API:
    
    def __init__(self):
        self.CLIENT_SECRET_FILE = 'google_calendar\client_secret.json'
        self.API_NAME = 'calendar'
        self.API_VERSION = 'v3'
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.service = Create_Service(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCOPES)

    def Create_Calendar(self, name):
        request_body = {
            'summary': name
        }
        response = self.service.calendars().insert(body=request_body).execute()
        pprint(response)
        print("Calendar Created")
        return response['id']

    def Update_Calendar(self, id, New_name):
        response = self.service.calendars().get(calendarId=id).execute()
        response['summary'] = New_name
        self.service.calendars().update(calendarId=id,body=response).execute()
        print("Calendar Updated")

    def Delete_Calendar(self, id):
        self.service.calendars().delete(calendarId=id).execute()
        print("Calendar Deleted")

    def Create_Event(self, id, name, description, start_time, end_time):
        request_body = {
            'start' : {
                'dateTime' : start_time,
                'timeZone' : 'Asia/Taipei'
            },
            'end':{
                'dateTime' : end_time,
                'timeZone' : 'Asia/Taipei'
            },
            'summary': name,
            'description':description,
            'colorId' : 2,
            'status':'confirmed',
            'transparency':'opaque',
            'visibility':'private',
            'guestsCanInviteOthers':'false'
        }
        response = self.service.events().insert(
            calendarId=id,
            body=request_body,
            sendUpdates="all"
        ).execute()
        pprint(response)
        print("Event Created")
        return response['id']
    
    def Delete_Event(self, id, eventid):
        self.service.events().delete(
        calendarId = id,
        eventId = eventid,
        sendUpdates="all"
        ).execute()
        print("Event Deleted")

    def Update_Summary(self, id, eventid, summary):
        response = self.service.events().get(calendarId=id,eventId=eventid).execute()
        response['summary'] = summary
        self.service.events().update(
        calendarId = id,
        eventId = eventid,
        body = response,
        sendUpdates="all").execute()
        print("Event summary updated")

    def Update_Description(self, id, eventid, description):
        response = self.service.events().get(calendarId=id,eventId=eventid).execute()
        response['description'] = description
        self.service.events().update(
        calendarId = id,
        eventId = eventid,
        body = response,
        sendUpdates="all").execute()
        print("Event description updated")

    def Update_Time(self, id, eventid, start_time, end_time):
        response = self.service.events().get(calendarId=id,eventId=eventid).execute()
        response['start']['dateTime'] = start_time
        response['end']['dateTime'] = end_time
        self.service.events().update(
        calendarId = id,
        eventId = eventid,
        body = response,
        sendUpdates="all").execute()
        print("Event Time updated")

    def Update_Attendee(self, id, eventid, attendee):
        response = self.service.events().get(calendarId=id,eventId=eventid).execute()
        add_attendees = {
            "email": attendee
        }
        pprint(response)
        if 'attendees' in response:
            response['attendees'].append(add_attendees)
            self.service.events().patch(
            calendarId = id,
            eventId = eventid,
            body=response,
            sendUpdates="all").execute()
        else:
            request_body = {
                "attendees": [add_attendees]
            }
            response.update(request_body)
            pprint(response)
            self.service.events().patch(
            calendarId = id,
            eventId = eventid,
            body=response,
            sendUpdates="all").execute()
    
        print("Event attendee updated")
        

    def Delete_Attendee(self, id, eventid, attendee):
        response = self.service.events().get(calendarId=id,eventId=eventid).execute()
        pprint(response)
        for a in response['attendees'][:]:
            if (a['email'] == attendee):
                response['attendees'].remove(a)
        self.service.events().patch(
        calendarId = id,
        eventId = eventid,
        body=response,
        sendUpdates="all").execute()
        print("Attendee Deleted")


#from CalendarAPI import calendar_API

#Cal = calendar_API()
#Cal.Create_Calendar('New_Name')
#Cal.Create_Event('calendarID','Summary','Description','Start_Time','End_Time')
#Cal.Update_Summary('calendarID','EventID','New_Summary')
#Cal.Update_Description('calendarID','EventID','New_Description')
#Cal.Update_Time('calendarID','EventID','New_StartTime','New_EndTime')
#Cal.Update_Attendee('calendarID','EventID','Email')
#Cal.Delete_Attendee('calendarID','EventID','Email')
#Cal.Delete_Event('calendarID','EventID')
#Cal.Update_Calendar('calendarID','New_Name')
#Cal.Delete_Calendar('calendarID')