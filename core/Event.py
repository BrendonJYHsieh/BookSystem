import time
from database import DataBase
class Event:
    id = "" # event id from google calendar
    name = ""
    description = ""
    start_time = None
    end_time = None
    participants = ["","",""]
    def __init__(self,_id,_name,_description): #TODO: time and participants
        self.id = _id
        self.name = _name
        self.description = _description
        return
    def addParticipant():
        return
    def deleteParticipant():
        return
