from UI import UI,UIloader
from database import DataBase,DBloader
from google_calendar import CalenderAPI
from core import Room
class BookSystem:
    rooms = []
    def __init__(self):
        self.ui = UI.BookSystemUI()
        self.gc = CalenderAPI.calendar_API()
        self.db = DataBase.DataBaseManager()
        self.dbl = DBloader.DBloader()
        self.uil = UIloader.UIloader()
        return
    def start(self):
        
        self.ui.BookSystem = self
        self.ui.initialUI()
        '''
        self.db.get_rooms()
        self.db.get_events('IB')
        self.db.get_participants('0')
        '''
        self.rooms = self.dbl.load(self.db)
        print(len(self.rooms))
        for room_index in range(len(self.rooms)):
            print(self.rooms[room_index].name)

        self.uil.load(self.ui,self.rooms)
        self.ui.runUI()

    def addRoom(self,room):
        if room.name == "":
            return
        print('add room!')
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room.name:
                return
        self.rooms.append(room)
        self.db.create_room(room.name)
        self.db.get_rooms()        
        self.ui.roomListInsert(room.name)
        self.gc.Create_Calendar(room.name)
        return
    def deleteRoom(self,room):
        print('del room!')
        found=False
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room.name:
                found = True
                del self.rooms[i]
                break
        if not found:
            return
        self.db.delete_room(room.name)
        self.db.get_rooms()       
        self.ui.roomListDelete(room.name)
        self.gc.Delete_Calendar(room.name)
        return
