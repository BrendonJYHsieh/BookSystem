from UI import UI,UIloader
from database import DataBase,DBloader
from google_calendar import CalendarAPI
from core import Room
class BookSystem:
    rooms = []
    def __init__(self):
        self.ui = UI.BookSystemUI()
        self.gc = CalendarAPI.calendar_API()
        self.db = DataBase.DataBaseManager()
        self.dbl = DBloader.DBloader()
        self.uil = UIloader.UIloader()
        return
    def start(self):
        self.ui.BookSystem = self
        self.rooms = self.dbl.load(self.db)
        for room_index in range(len(self.rooms)):
            print(self.rooms[room_index].name)

        self.ui.initialUI()
        self.uil.load(self.ui,self.rooms)
        self.ui.runUI()

    def addRoom(self,room):
        if room.name == "":
            return
        print('add room!')
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room.name:
                #TODO 彈出警告視窗
                return
        self.rooms.append(room)
        self.db.create_room(room.name)
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
        self.ui.roomListDelete(room.name)
        self.gc.Delete_Calendar(room.name)
        return
    def updateRoom(self,old_name,new_name):
        found=False
        for i in range(len(self.rooms)):
            if self.rooms[i].name == old_name:
                found = True
                self.rooms[i].name = new_name
                break
        if not found:
            #TODO 彈出警告視窗
            return
        print("old:" + old_name)
        print("new:" + new_name)
        self.db.get_rooms()    
        self.db.update_room(old_name,new_name)
        #self.gc.Update_Calendar(old_name,new_name)
