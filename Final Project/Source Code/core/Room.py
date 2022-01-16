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
            self.BookSystem.ui.MessageBoxError('Room Error','The room has been deleted')
            return
        print('Add Event!')
        #self.events.append(event)
        if not self.insert_event(event):
            #TODO not leave page
            self.BookSystem.ui.MessageBoxError('Input Error','The room not allow two event at same time')
            return
        event.id = self.BookSystem.gc.Create_Event(self.id,event.name,event.description,
                    (event.start_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'),
                    (event.end_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        


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
            self.BookSystem.ui.MessageBoxError('Room Error','The room has been deleted')
            return
        if not event.exist():
            print("BackToTimeLine")
            self.BookSystem.ui.bookInterface.BackToTimeLine()
            self.BookSystem.ui.MessageBoxError('Event Error','The event has been deleted')
            return
        found=False
        for i in range(len(self.events)):
            if self.events[i].id == event.id:
                found = True
                del self.events[i]
                break
        if not found:
            self.BookSystem.ui.bookInterface.BackToTimeLine()
            self.BookSystem.ui.MessageBoxError('Event Error','The event has been deleted')
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
            self.BookSystem.ui.MessageBoxError('Room Error','The room has been deleted')
            return
        if not new_event.exist():
            print("BackToTimeLine")
            self.BookSystem.ui.bookInterface.BackToTimeLine()
            self.BookSystem.ui.MessageBoxError('Event Error','The event has been deleted')
            return
        if not self.available_event_modify(new_event):
            #TODO not leave page
            self.BookSystem.ui.MessageBoxError('Input Error','The room not allow two event at same time')
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
    def event_overlap(self,eventA,eventB):
        if eventA.id == eventB.id: #update event
            return False
        if eventB.start_time > eventA.start_time:
            if eventB.start_time >= eventA.end_time:
                return False
            else:
                return True
        elif eventB.start_time < eventA.start_time:
            if eventB.end_time <= eventA.start_time:
                return False
            else:
                return True
        else: #eventB.start_time == eventA.start_time
            return True
    def insert_event(self,new_event):
        for i in range(len(self.events)):
            if self.events[i].start_time >= new_event.start_time:
                if not self.event_overlap(new_event,self.events[i]) and not self.event_overlap(new_event,self.events[i-1]):
                    self.events.insert(i,new_event)
                    return True
                else:
                    print("not available event")
                    return False      
        self.events.append(new_event)
        return True

    def available_event_modify(self,event):
        if len(self.events) == 0 or len(self.events) == 1:
            return True
        for i in range(len(self.events)-1):
            if self.events[i].id == event.id:
                print(str(event.start_time) + ' ' +str(event.end_time) )
                print(str(self.events[i-1].start_time) + ' ' +str(self.events[i-1].end_time) )
                print(str(self.events[i+1].start_time) + ' ' +str(self.events[i+1].end_time) )
                print( self.event_overlap(event,self.events[i-1]))
                print( self.event_overlap(event,self.events[i+1]))
                
                if not self.event_overlap(event,self.events[i-1]) and not self.event_overlap(event,self.events[i+1]):
                    print("available event")
                    return True
                else:
                    print("not available event")
                    return False
        print(str(event.start_time) + ' ' +str(event.end_time) )
        print(str(self.events[-2].start_time) + ' ' +str(self.events[-2].end_time) )
        print( self.event_overlap(event,self.events[-2]))
        if not self.event_overlap(event,self.events[-2]):
            print("available event")
            return True
        else:
            print("not available event")
            return False
