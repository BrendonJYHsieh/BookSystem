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
        data = self.db.get_user(username)
        if(data):
            print("User has already existed")
        else:
            self.db.create_user(username,h)
        
    def login(self,username,password):
        s = hashlib.sha1()
        s.update(password.encode("utf-8"))
        h = s.hexdigest()
        data = self.db.vaild_user(username)
        if(data):
            if(self.db.vaild_user(username)[0]==h):
                self.CurrentUser = username
                self.valid = True
            else:
                print("Password is error.")
        else:
            print("User don't exist.")
        