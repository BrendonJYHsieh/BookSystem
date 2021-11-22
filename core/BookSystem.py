from UI import UI
from database import DataBase
from google_calendar import CalenderAPI
class BookSystem:
    rooms = []
    def __init__(self):
        application = UI.BookSystemUI()
        db = DataBase.DataBaseManager()
        db.show_rooms()
        return
    def showRoom(self):
        UI.draw()
        return
    def addRoom(self):
        #DataBase.writeDataBase()
        return
    def deleteRoom(self):
        #DataBase.writeDataBase()
        return
    def update(self): #update UI
        UI.redraw()
        return
