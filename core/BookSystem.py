from UI import UI
from database import DataBase
from google_calendar import CalenderAPI
class BookSystem:
    rooms = []
    def __init__(self):
        
        self.ui = UI.BookSystemUI()
        self.ui.BookSystem = self
        self.ui.initialUI()
        self.gc = CalenderAPI.calendar_API()
        self.db = DataBase.DataBaseManager()
        self.db.show_rooms()
        self.ui.runUI()

        return
    def showRoom(self):
        UI.draw()
        return
    def addRoom(self,room):
        print('add room!')
        self.gc.Create_Calendar(room.name,room.description)
        return
    def deleteRoom(self):
        #DataBase.writeDataBase()
        return
    def update(self): #update UI
        UI.redraw()
        return
