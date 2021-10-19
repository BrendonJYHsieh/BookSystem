import DataBase
import UI

class BookSystem:
    rooms = []
    def __init__(self):
        return
    def init(self):
        DataBase.loadDataBase()
        return
    def showRoom(self):
        UI.draw()
        return
    def addRoom(self):
        DataBase.writeDataBase()
        return
    def deleteRoom(self):
        DataBase.writeDataBase()
        return
    def update(self): #update UI
        UI.redraw()
        return
