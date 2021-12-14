from database import DataBase
import hashlib

class Authorization:
    CurrentUser=""
    valid = False
    
    def __init__(self):
        self.db = DataBase.DataBaseManager()

    def register(self,username,password):
        s = hashlib.sha1()
        s.update(password.encode("utf-8"))
        h = s.hexdigest()
        print("username")
        self.db.create_user(username,h)
        
    def login(self,username,password):
        s = hashlib.sha1()
        s.update(password.encode("utf-8"))
        h = s.hexdigest()
        if(self.db.vaild_user(username)[0]==h):
            self.valid = True;
            self.CurrentUser = username
        