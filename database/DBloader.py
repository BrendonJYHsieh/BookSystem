from database import DataBase
from core import Room,Event
class DBloader:
    rooms = []
    def __init__(self):
        return
    def load(self,db):
        room_tuples = db.get_rooms()
        for x in room_tuples:
            self.rooms.append(Room.Room(x[0]))
        
        for room_index in range(len(self.rooms)):
            event_tuples = db.get_events(self.rooms[room_index].name)
            for x in event_tuples:
                self.rooms[room_index].events.append(Event.Event(x[0],x[1],x[2]))
        
        for room_index in range(len(self.rooms)):
            for event_index in range(len(self.rooms[room_index].events)):
                participant_tuples = db.get_participants(self.rooms[room_index].events[event_index].id)
                for x in participant_tuples:
                    self.rooms[room_index].events[event_index].participants.append(x[0])
        return self.rooms