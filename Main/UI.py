import BookSystem
import Room
import Event

UI_switch = 0 #room list -> 0 room info -> 1 event modify -> 2

def drawRoomList(): #list all room
    return
def drawRoomInfo(): #can modify room info
    return
def drawEventInfo(): #can modify event info
    return



def draw():
    if UI_switch == 0:
        drawRoomList()
    elif UI_switch == 1:
        drawRoomInfo()
    elif UI_switch == 2:
        drawEventInfo()
    return

def redraw():
    return


def roomBaseInfoModify(room):
    room.name = "xxx"
    room.description = "xxx"

def roomEventsModify(room):
    UI_switch = 2

def eventModify(event):
    event.name = "xxx"
    event.description = "xxx"
    event.start_time = None
    event.end_time = None

def eventParticipantModify(event,emails):
    event.participants = emails

