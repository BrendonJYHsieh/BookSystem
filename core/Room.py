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
        self.BookSystem.check_db_update()
        if not self.exist():
            self.BookSystem.ui.bookInterface.BackToRoomList()
        print('Add Event!')        
        event.id = self.BookSystem.gc.Create_Event(self.id,event.name,event.description,
                    (event.start_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    (event.end_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        
        self.events.append(event)
        self.BookSystem.db.create_event(event.id,event.name,event.description,event.start_time,event.end_time,self.name)
        if event.participants: #participants not empty            
            for participant in event.participants:
                self.BookSystem.gc.Add_Attendee(self.id,event.id,participant)
                self.BookSystem.db.create_participant(event.id,participant)
                self.BookSystem.addParticipant(participant).add_event(self.events[-1])
        print('Add Event successful!')
        return
    
    def deleteEvent(self,event):
        self.BookSystem.check_db_update()
        if not self.exist():
            self.BookSystem.ui.bookInterface.BackToRoomList()
            return
        if not event.exist():
            print("BackToTimeLine")
            self.BookSystem.ui.bookInterface.BackToTimeLine()
            return
        found=False
        for i in range(len(self.events)):
            if self.events[i].id == event.id:
                found = True
                del self.events[i]
                break
        if not found:
            return
        print('Delete Event!')
        self.BookSystem.db.delete_event(event.id)
        self.BookSystem.gc.Delete_Event(self.id,event.id)
        for participant in event.participants:
            self.BookSystem.getParticipant(participant).delete_event(event.id)
        print('Delete Event successful!')
    def updateEvent(self,new_event):
        self.BookSystem.check_db_update()
        if not self.exist():
            self.BookSystem.ui.bookInterface.BackToRoomList()
            return
        if not new_event.exist():
            print("BackToTimeLine")
            self.BookSystem.ui.bookInterface.BackToTimeLine()
            return
        for i in range(len(self.events)):
            if self.events[i].id == new_event.id:
                self.events[i].update(new_event)
                break            
        print('Modify Event successful!')
        return

    def getEvent(self,name):
        for i in range(len(self.events)):
            if self.events[i].name == name:
                return self.events[i]
        return None
    def getEventById(self,id):
        for i in range(len(self.events)):
            if self.events[i].id == id:
                return self.events[i]
        return None
    def getEventParticipants(self,event_id):
        for i in range(len(self.events)):
            if self.events[i].id == event_id:
                return self.events[i].participants
        return None
    def exist(self):
        return self.BookSystem.getRoomById(self.id) != None
    def garbage_event_collection(self):
        for event in self.events:
            if event.end_time < datetime.today():
                self.deleteEvent(event)
