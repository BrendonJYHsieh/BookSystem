import mysql.connector
import datetime

class DataBaseManager:
  def __init__(self) -> None:
      self.connect()
      pass
  def connect(self):
    self.mydb = mysql.connector.connect(
      host="jp-tyo-ilj-1.natfrp.cloud",
      port= "60867",
      user="Manager",
      password="10815044",
      database="Booksystem",
      auth_plugin='mysql_native_password',
      autocommit=True
    )  
    self.cursor = self.mydb.cursor()
  def get_lastupdate(self):
    self.cursor.execute("Select * from Synchronize LIMIT 1")
    tuples = []
    x : datetime
    for x in self.cursor:
      tuples.append(x)
    return x[0]
  
  def get_rooms(self):
    self.cursor.execute("Select * from rooms")
    tuples = []
    for x in self.cursor:
      tuples.append(x)
    return tuples

  def get_events(self, RoomName):
    sql = "Select * FROM events WHERE RoomName = %s"
    val = (RoomName)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    tuples = []
    for x in self.cursor:
      tuples.append(x)
    return tuples

  def get_participants_By_Event (self, EventID):
    sql = "Select Email FROM participants WHERE EventID = %s"
    val = (EventID)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    tuples = []
    for x in self.cursor:
      tuples.append(x)
    return tuples
  def get_participants(self):
    self.cursor.execute("Select Email from participants")
    tuples = []
    for x in self.cursor:
      print(x)
      tuples.append(x)
    return tuples
      
  def get_myEventID(self, Email):
    sql = "Select EventID FROM participants WHERE Email = %s"
    val = (Email)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    tuples = []
    for x in self.cursor:
      tuples.append(x)
    return tuples
  
  def get_myEvent(self, EventID):
    sql = "Select * FROM events WHERE EventID = %s"
    val = (EventID)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    tuples = []
    for x in self.cursor:
      tuples.append(x)
      print(x)
    return tuples
  
  def get_user(self, Username):
    sql = "Select Username FROM users WHERE Username = %s"
    val = (Username)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    tuples = []
    for x in self.cursor:
      tuples.append(x)
    return tuples
  
  def vaild_user(self, Username):
    sql = "Select Password FROM users WHERE Username = %s"
    val = (Username)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    for x in self.cursor:
      return x
  

  def create_room(self,RoomID, RoomName):
    sql = "INSERT IGNORE INTO rooms (RoomID, RoomName) VALUES (%s, %s) "
    val = (RoomID,RoomName)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    self.update_lastupdate()

  def create_event(self, EventID, EventName, EventDescription, StartTime, EndTime, RoomName):
    sql = "INSERT IGNORE INTO events (EventID, EventName, EventDescription, StartTime, EndTime, RoomName) VALUES (%s,%s,%s,%s,%s,%s) "
    val = (EventID, EventName, EventDescription, StartTime, EndTime, RoomName)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    self.update_lastupdate()

  def create_participant(self, EventID, Email):
    sql = "INSERT IGNORE INTO participants (EventID, Email) VALUES (%s,%s) "
    val = (EventID, Email)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    self.update_lastupdate()

  def create_user(self,Username, Password):
    sql = "INSERT IGNORE INTO users (Username, Password) VALUES (%s, %s) "
    val = (Username,Password)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    #self.update_lastupdate() #暫時不更新這個
    
  def delete_room(self,RoomName):
    sql = "DELETE FROM rooms WHERE RoomName = %s"
    val = (RoomName)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    self.mydb.commit()
    self.update_lastupdate()

  def delete_event(self, EventID):
    sql = "DELETE FROM events WHERE EventID = %s"
    val = (EventID)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    self.mydb.commit()
    self.update_lastupdate()
  
  def delete_participant(self, EventID, Email):
    sql = "DELETE FROM participants WHERE EventID = %s AND Email = %s"
    val = (EventID,Email)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    
  def update_room(self,OldRoomName, NewRoomName):
    sql = "UPDATE rooms SET RoomName = %s WHERE RoomName = %s"
    val = (NewRoomName,OldRoomName)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    self.update_lastupdate()
  
  def update_event(self, EventID, EventName,EventDescription, StartTime, EndTime):
    sql = "UPDATE events SET EventName = %s, EventDescription = %s, StartTime = %s, EndTime = %s WHERE EventID = %s"
    val = (EventName ,EventDescription, StartTime , EndTime , EventID)
    self.cursor.execute(sql, val)
    self.mydb.commit()
    self.update_lastupdate()
    
  def update_lastupdate(self):
    sql = "UPDATE Synchronize SET LastUpdate = %s"
    val = (datetime.datetime.now())
    params = (val,)
    self.cursor.execute(sql, params)
    self.mydb.commit()


DBM = DataBaseManager()
#DBM.update_event(0,"@@@","dsfsdfsdf",'2021-11-19 13:20:00', '2021-11-19 15:20:00')
### Create ###
# DBM.create_room("test")
# DBM.show_rooms()
#DBM.update_lastupdate()
DBM.get_participants();
# DBM.create_event(11,"軟體工程", "Teacher:柯拉飛", '2021-10-15 13:20:00', '2021-10-15 15:10:00', "TR")
#DBM.show_events('TR')

# DBM.create_participant(0,"testtest@gmail.com")
# DBM.show_participants()

### Delete ###
# DBM.delete_room("sadsa")
# DBM.show_rooms()

# DBM.delete_event(11)
# DBM.show_events()

# DBM.delete_participant(0,"testtest@gmail.com")
#DBM.show_participants(1)



