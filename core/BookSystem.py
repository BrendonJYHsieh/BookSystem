from UI import UI,UIloader
from database import DataBase,DBloader
from google_calendar import CalendarAPI
from core import Room,Authorization
class BookSystem:
    users = []
    rooms = []
    def __init__(self):
        self.ui = UI.BookSystemUI(self)
        self.gc = CalendarAPI.calendar_API()
        self.db = DataBase.DataBaseManager()
        self.dbl = DBloader.DBloader()
        self.uil = UIloader.UIloader()
        self.auth = Authorization.Authorization()
        return
    def start(self):
        self.rooms = self.dbl.load(self,self.db)
        for room_index in range(len(self.rooms)):
            print(self.rooms[room_index].name)

        self.ui.initialUI()
        self.uil.load(self.ui,self.rooms)
        self.ui.runUI()

    def getRoom(self,name):
        for i in range(len(self.rooms)):
            if self.rooms[i].name == name:
                return self.rooms[i]
        return None
    def getRoomEvents(self,room_name):
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room_name:
                return self.rooms[i].events
        return None

    def addRoom(self,room):
        print('Add Room!')
        if room.name == "":
            print('Room_name is Empty!')
            return
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room.name:
                #TODO 彈出警告視窗
                print('Room_name is Duplicated!')
                return
        room.BookSystem = self
        room.id = self.gc.Create_Calendar(room.name)
        self.rooms.append(room)
        self.db.create_room(room.id,room.name)
        self.ui.roomListInsert(room.name)
        print('Add Room successful!')
        self.db.update_lastupdate()
        return
    def deleteRoom(self,room):
        print('Delete Room!')
        found=False
        for i in range(len(self.rooms)):
            if self.rooms[i].name == room.name:
                room.id = self.rooms[i].id
                found = True
                del self.rooms[i]
                break
        if not found:
            return
        self.db.delete_room(room.name)     
        self.ui.roomListDelete(room.name)
        self.gc.Delete_Calendar(room.id)
        print('Delete Room successful!')
        self.db.update_lastupdate()
        return
    def updateRoom(self,old_name,new_name):
        print('Update Room!')
        found=False
        for i in range(len(self.rooms)):
            if self.rooms[i].name == old_name:
                found = True
                self.rooms[i].name = new_name
                roomID = self.rooms[i].id
                break
        if not found:
            #TODO 彈出警告視窗
            return
        self.db.update_room(old_name,new_name)
        self.ui.roomListUpdate()
        self.gc.Update_Calendar(roomID,new_name)
        self.db.update_lastupdate()
        print('Update Room successful!')
