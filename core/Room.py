from UI import UI
from database import DataBase,DBloader
from google_calendar import CalendarAPI
class Room:
    id = "" # calendar id from google calendar
    name = ""
    BookSystem = None
    events = []
    def __init__(self,_BookSystem,_name):
        self.BookSystem = _BookSystem
        self.name = _name
        return
    def addEvent(self,event):        
        event.id = self.BookSystem.gc.Create_Event(self.id,event.name,event.description,event.start_time,event.end_time)
        self.BookSystem.gc.Update_Attendee(self.id,event.id,event.participants)
        self.events.append(event)
        self.BookSystem.db.create_event(event.id,event.name,event.description,event.start_time,event.end_time,self.name)
        return
    def deleteEvent(self,event):
        print('Delete Event!')
        found=False
        for i in range(len(self.events)):
            if self.events[i].name == event.name:
                event.id = self.events[i].id
                found = True
                del self.events[i]
                break
        if not found:
            return
        self.db.delete_event(event.name)     
        #self.ui.roomListDelete(event.name)
        self.gc.Delete_Event(event.id)
        print('Delete Event successful!')
    def modifyEvent(self):
        return