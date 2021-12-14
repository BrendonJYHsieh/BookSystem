Create Database BookSystem;
use BookSystem;
Create table Rooms(
    RoomID varchar(60) Not Null,
	RoomName varchar(20) Not Null
);

Create table Events(
    EventID varchar(30) Not Null,
	EventName varchar(20) Not Null,
    EventDescription varchar(400) Not Null,
    StartTime datetime Not Null,
    EndTime datetime Not Null,
    RoomName varchar(20) Not Null
);

Create table Participants(
    EventID varchar(30) Not Null,
    Email varchar(40) Not Null
);

Create table Users(
    UserName varchar(40) Not Null,
	Password varchar(100) Not Null
);

Create table Synchronize(
    LastUpdate datetime Not Null
);

Insert into Rooms (RoomID,RoomName) Values
("etrewtwe@dfasfas","TR"),
("etrewtwe@dfasfas","IB"),
("etrewtwe@dfasfas","T4")

INSERT INTO Synchronize(LastUpdate)
VALUES(NOW());

Insert into Events (EventID, EventName, EventDescription, StartTime, EndTime, RoomName) Values
("0","次世代無線網路概論", "Teacher:周詩梵", '2021-10-11 10:20:00', '2021-10-11 11:10:00', "IB"),
("1","作業系統", "Teacher:鄭仁偉", '2021-10-11 13:20:00', '2021-10-11 15:10:00', "TR"),
("2","科技英文", "Teacher:黃子玲", '2021-10-11 15:30:00', '2021-10-11 18:20:00', "T4"),

("3","程式語言", "Teacher:吳怡樂", '2021-10-12 13:20:00', '2021-10-12 15:10:00', "TR"),
("4","作業系統", "Teacher:鄭仁偉", '2021-10-12 15:30:00', '2021-10-12 16:20:00', "TR"),

("5","英文小說與電影", "Teacher:方博杰", '2021-10-13 10:20:00', '2021-10-13 12:10:00', "IB"),

("6","程式語言", "Teacher:吳怡樂", '2021-10-14 9:10:00', '2021-10-14 10:00:00', "TR"),
("7","軟體工程", "Teacher:柯拉飛", '2021-10-14 10:20:00', '2021-10-14 11:10:00', "TR"),
("8","新聞英文", "Teacher:卜莎娜", '2021-10-14 13:20:00', '2021-10-14 16:20:00', "T4"),

("9","翻譯與習作", "Teacher:李宜懃", '2021-10-15 10:20:00', '2021-10-15 12:10:00', "T4"),
("10","軟體工程", "Teacher:柯拉飛", '2021-10-15 13:20:00', '2021-10-15 15:10:00', "TR")

Insert into Participants (EventID, Email) Values
("47u9716adbs709hv3nbmlr6b24","b10815044@gapps.ntust.edu.tw"),

("1","b10815044@gapps.ntust.edu.tw"),

("2","b10815058@gapps.ntust.edu.tw"),

("3","b10815054@gapps.ntust.edu.tw"),
("3","b10815058@gapps.ntust.edu.tw"),

("4","b10815044@gapps.ntust.edu.tw"),
("4","b10815058@gapps.ntust.edu.tw"),

("5","b10815044@gapps.ntust.edu.tw"),
("5","b10815054@gapps.ntust.edu.tw"),

("6","b10815044@gapps.ntust.edu.tw"),
("6","b10815054@gapps.ntust.edu.tw"),
("6","b10815058@gapps.ntust.edu.tw"),

("7","b10815044@gapps.ntust.edu.tw"),
("7","b10815054@gapps.ntust.edu.tw"),
("7","b10815058@gapps.ntust.edu.tw"),

("8","b10815044@gapps.ntust.edu.tw"),
("8","b10815054@gapps.ntust.edu.tw"),
("8","b10815058@gapps.ntust.edu.tw"),

("9","b10815044@gapps.ntust.edu.tw"),
("9","b10815054@gapps.ntust.edu.tw"),
("9","b10815058@gapps.ntust.edu.tw")

Alter table rooms add primary key (RoomName);

Alter table Events 
add Constraint Fk_RoomName 
foreign key (RoomName) References rooms(RoomName)
ON UPDATE CASCADE ON DELETE CASCADE;

Alter table Events add primary key (EventID);

Alter table Participants 
add Constraint Fk_EventID foreign key (EventID) References Events(EventID)
ON UPDATE CASCADE ON DELETE CASCADE;