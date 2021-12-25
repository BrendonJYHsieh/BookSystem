from database import DataBase
from core import Room,Event,Participant
class DBloader:
    def __init__(self):
        return
    def load(self,BookSystem,db):
        room_tuples = db.get_rooms()
        for x in room_tuples:
            room = Room.Room(BookSystem,x[1])
            room.id = x[0]
            room.BookSystem = BookSystem
            BookSystem.rooms.append(room)
        
        for room_index in range(len(BookSystem.rooms)):
            event_tuples = db.get_events(BookSystem.rooms[room_index].name)
            for x in event_tuples:
                event = Event.Event(BookSystem,BookSystem.rooms[room_index],x[1],x[2],x[3],x[4])
                event.id = x[0]
                BookSystem.rooms[room_index].events.append(event) 
        for room_index in range(len(BookSystem.rooms)):
            for event_index in range(len(BookSystem.rooms[room_index].events)):
                participant_tuples = db.get_participants_By_Event(BookSystem.rooms[room_index].events[event_index].id)
                for x in participant_tuples:                    
                    BookSystem.rooms[room_index].events[event_index].participants.append(x[0])
                    participant = BookSystem.addParticipant(x[0])
                    participant.add_event(BookSystem.rooms[room_index].events[event_index])

        return
    
    
        