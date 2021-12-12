from UI import UI
from database import DataBase,DBloader
from google_calendar import CalendarAPI
from datetime import datetime,timedelta 
class Room:
    id = ""
    name = ""
    BookSystem = None
    events = []
    def __init__(self,_BookSystem,_name):
        self.BookSystem = _BookSystem
        self.name = _name
        return
    def addEvent(self,event):        
        event.id = self.BookSystem.gc.Create_Event(self.id,event.name,event.description,
                    (datetime.strptime(event.start_time,'%Y-%m-%dT%H:%M:%SZ')-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    (datetime.strptime(event.end_time,'%Y-%m-%dT%H:%M:%SZ')-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        self.events.append(event)
        self.BookSystem.db.create_event(event.id,event.name,event.description,event.start_time,event.end_time,self.name)
        return
    def deleteEvent(self):
        return
    def modifyEvent(self):
        return