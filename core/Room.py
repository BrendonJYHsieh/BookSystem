from UI import UI
from database import DataBase,DBloader
from google_calendar import CalendarAPI
from datetime import datetime,timedelta 
class Room:
    id = "" # calendar id from google calendar
    name = ""
    BookSystem = None
    events = []
    def __init__(self,_BookSystem,_name):
        self.BookSystem = _BookSystem
        self.name = _name
        self.events = []
        return
    def addEvent(self,event):
        print('Add Event!')        
        event.id = self.BookSystem.gc.Create_Event(self.id,event.name,event.description,
                    (event.start_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    (event.end_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        
        self.events.append(event)
        self.BookSystem.db.create_event(event.id,event.name,event.description,event.start_time,event.end_time,self.name)
        if event.participants: #participants not empty
            self.BookSystem.gc.Update_Attendee(self.id,event.id,event.participants)
            for participant in event.participants:
                self.BookSystem.db.create_participant(event.id,participant);      
        print('Add Event successful!')
        return
    
    def deleteEvent(self,event):
        print('Delete Event!')
        found=False
        for i in range(len(self.events)):
            if self.events[i].id == event.id:
                found = True
                del self.events[i]
                break
        if not found:
            return
        self.BookSystem.db.delete_event(event.id)
        self.BookSystem.gc.Delete_Event(self.id,event.id)
        print('Delete Event successful!')
    def modifyEvent(self,event,deleted_users):
        print('Modify Event!')        
        self.BookSystem.db.update_event(event.id,event.name,event.description,event.start_time,event.end_time,self.name)
        if event.participants: #participants not empty
            self.BookSystem.gc.Update_Attendee(self.id,event.id,event.participants)
            for participant in event.participants:
                self.BookSystem.db.create_participant(event.id,participant);      
        if event.deleted_users:
            for username in event.deleted_users:
                self.BookSystem.db.delete_participant(username,participant); 
        print('Modify Event successful!')
        return

    def getEvent(self,name):
        for i in range(len(self.events)):
            if self.events[i].name == name:
                return self.events[i]
        return None
    def getEventParticipants(self,event_id):
        for i in range(len(self.events)):
            if self.events[i].id == event_id:
                return self.events[i].participants
        return None