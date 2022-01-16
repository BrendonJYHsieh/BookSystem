from UI import UI,BookInterface
from core import Room,Event
class UIloader:
    def __init__(self):
        return
    def load(self,ui,rooms):
        print("UI loader")
        selection = ui.room_list.curselection()
        select_name = ""
        if selection != ():
            select_name = ui.room_list.get(selection)
            print("select" + select_name)
        ui.roomListClear()
        for room_index in range(len(rooms)): #room manager載入UI
            if rooms[room_index].name == select_name:
                ui.roomListSelect(room_index)
            ui.roomListInsert(rooms[room_index].name)