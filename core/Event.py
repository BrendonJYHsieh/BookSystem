import time
from core import BookSystem
from database import DataBase
from datetime import date, datetime
class Event:
    BookSystem = None
    id = "" # event id from google calendar
    name = ""
    description = ""
    start_time : datetime
    end_time : datetime
    def __init__(self,_BookSystem,_name,_description,_start_time,_end_time): #TODO: time
        self.BookSystem = _BookSystem
        self.name = _name
        self.description = _description
        self.start_time = _start_time
        self.end_time = _end_time
        return