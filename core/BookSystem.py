from UI import UI
from database import DataBase
from google_calendar import CalenderAPI
from core import Room,DBloader
class BookSystem:
    rooms = []
    def __init__(self):
        self.ui = UI.BookSystemUI()
        self.gc = CalenderAPI.calendar_API()
        self.db = DataBase.DataBaseManager()
        self.dbl = DBloader.DBloader()
        return
    def start(self):
        self.dbl.load(self.db)
        self.ui.BookSystem = self
        self.ui.initialUI()
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
        self.db.show_rooms()        
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
        self.db.show_rooms()       
        self.ui.roomListDelete(room.name)
        self.gc.Delete_Calendar(room.name)
        return
