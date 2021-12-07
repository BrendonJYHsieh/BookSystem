from UI import UI
from database import DataBase,DBloader
from google_calendar import CalendarAPI
class Room:
    name = ""
    BookSystem = None
    events = []
    def __init__(self,_BookSystem,_name):
        self.BookSystem = _BookSystem
        self.name = _name
        return
    def addEvent(self,event):        
        event.id = self.BookSystem.gc.Create_Event(event.name,event.description,event.start_time,event.end_time)
        self.events.append(event)
        self.BookSystem.db.create_event(event.id,event.name,event.start_time,event.end_time,self.name)
        return
    def deleteEvent(self):
        return
    def modifyEvent(self):
        return