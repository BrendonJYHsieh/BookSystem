import mysql.connector

class DataBaseManager:
  mydb = mysql.connector.connect(
    host="140.118.127.106",
    user="Manager",
    password="10815044",
    database="Booksystem"
  )
  cursor = mydb.cursor()
  def show_rooms(self):
    self.cursor.execute("Select * from rooms")
    for x in self.cursor:
      print(x)

  def show_events(self):
    self.cursor.execute("Select * from events")
    for x in self.cursor:
      print(x)

  def show_participants(self):
    self.cursor.execute("Select * from participants")
    for x in self.cursor:
      print(x)

  def create_room(self,RoomName):
    sql = "INSERT IGNORE INTO rooms (RoomName) VALUES (%s) "
    val = (RoomName)
    params = (val,) # Due to single value
    self.cursor.execute(sql, params)
    self.mydb.commit()

  def create_event(self, EventID, EventName, EventDescription, StartTime, EndTime, RoomName):
    sql = "INSERT IGNORE INTO events (EventID, EventName, EventDescription, StartTime, EndTime, RoomName) VALUES (%s,%s,%s,%s,%s,%s) "
    val = (EventID, EventName, EventDescription, StartTime, EndTime, RoomName)
    self.cursor.execute(sql, val)
    self.mydb.commit()

  def create_participant(self, EventID, Email):
    sql = "INSERT IGNORE INTO participants (EventID, Email) VALUES (%s,%s) "
    val = (EventID, Email)
    self.cursor.execute(sql, val)
    self.mydb.commit()

DBM = DataBaseManager()
# DBM.create_room("test")
# DBM.show_rooms()
# DBM.create_event(11,"軟體工程", "Teacher:柯拉飛", '2021-10-15 13:20:00', '2021-10-15 15:10:00', "TR")
# DBM.show_events()
# DBM.create_participant(0,"testtest@gmail.com")
# DBM.show_participants()

