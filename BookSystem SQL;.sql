use BookSystem;
Create table Rooms(
	RoomName varchar(20) Not Null
);

Create table Events(
	EventName varchar(20) Not Null,
    EventDescription varchar(400) Not Null,
    StartTime: date
    EndTime: date
    RoomName varchar(20) Not Null
);

Create table Participants(
    Email varchar(20) Not Null,
    RoomName varchar(20) Not Null,
    EventName varchar(20) Not Null
);
