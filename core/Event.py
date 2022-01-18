import time
from core import BookSystem
from database import DataBase
from datetime import date, datetime,timedelta
class Event:
    BookSystem = None
    room = None
    id = "" # event id from google calendar
    name = ""
    description = ""
    start_time = datetime
    end_time = datetime
    participants = None
    def __init__(self,_BookSystem,_room,_name,_description,_start_time,_end_time): #TODO: time
        self.BookSystem = _BookSystem
        self.room = _room
        self.name = _name
        self.description = _description
        self.start_time = _start_time
        self.end_time = _end_time
        self.participants = []
        return
    def update_participants(self,_participants):
        self.participants = _participants
    def update(self,new_event):
        for participant in self.participants:
            if not new_event.in_event(participant):
                self.BookSystem.db.delete_participant(self.id,participant)
                self.BookSystem.gc.Delete_Attendee(self.room.id,self.id,participant)
                self.BookSystem.getParticipant(participant).delete_event(self.id)
        for participant in new_event.participants:
            if not self.in_event(participant):
                self.BookSystem.db.create_participant(self.id,participant)
                self.BookSystem.gc.Add_Attendee(self.room.id,self.id,participant)
                self.BookSystem.addParticipant(participant).add_event(self)
        self.BookSystem.db.update_event(new_event.id,new_event.name,new_event.description,new_event.start_time,new_event.end_time)
        self.BookSystem.gc.Update_Summary(self.room.id,self.id,new_event.name)
        self.BookSystem.gc.Update_Description(self.room.id,self.id,new_event.description)
        self.BookSystem.gc.Update_Time(self.room.id,self.id,(new_event.start_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'),(new_event.end_time-timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%SZ'))
        self = new_event

    def in_event(self,email):
        for i in self.participants:
            if email == i:
                return True
        return False
    def exist(self):
        if self.room.exist():
            return self.room.getEventById(self.id) != None
        return False
    def overlap(self,other):
        if self.id == other.id: #update event
            return False
        if other.start_time > self.start_time:
            if other.start_time >= self.end_time:
                return False
            else:
                return True
        elif other.start_time < self.start_time:
            if other.end_time <= self.start_time:
                return False
            else:
                return True
        else: #eventB.start_time == eventA.start_time
            return True