from os import stat, stat_result
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime 
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text
import re
from UI import BaseInterface
from core import Room,Event

'''
Interface -> RoomList = 0 -> Calendar = 1 -> TimeLine = 2 -> CheckBoard = 3
'''
class BookInterface(BaseInterface.BaseInterface):
    state = 0
    TargetDay = -1
    def __init__(self,_parent,_booksystem):
        super().__init__(_parent)
        self.BookSystem = _booksystem
        self.interfaceTitle = tk.Label(self.mainCanvas,text="Booking", font=('Helvetica', '20'),background="#dcdcdc")
        self.chooseRoomLabel = tk.Label(self.mainCanvas,text="      Choose Room", font=('Helvetica', '15'),background="#dcdcdc")
        self.calendarLabel = tk.Label(self.mainCanvas,text="      Choose Date", font=('Helvetica', '15'),background="#dcdcdc")
        self.timeLineLabel = tk.Label(self.mainCanvas,text="      Choose Time", font=('Helvetica', '15'),background="#dcdcdc")
        self.CreateRoomListGroup()
        self.CreateCalendarGroup()
        self.CreateTimeLineGroup()
        self.CreateCheckBoardGroup()
        self.backButton = tk.Button(self.mainCanvas,text="Back",command=self.Back)
    def Enable(self):
        self.mainCanvas.place(x=230,y=20)
        self.interfaceTitle.place(x=10,y=10)
        self.Switch()
    def Disable(self):
        self.mainCanvas.place_forget()
    def Switch(self):
        if self.state == 0:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place_forget()
            self.timeLineLabel.place_forget()
            self.SetRoomListActive(True)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(False)
            self.backButton.place_forget()
        if self.state == 1:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.timeLineLabel.place_forget()
            self.SetRoomListActive(False)
            self.SetCalendarActive(True)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(False)
            self.backButton.place(x=0,y=540)
        if self.state == 2:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.timeLineLabel.place(x=40,y=110)
            self.SetRoomListActive(False)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(True)
            self.SetCheckBoardActive(False)
            self.backButton.place(x=0,y=540)
        if self.state == 3:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.timeLineLabel.place(x=40,y=110)
            self.SetRoomListActive(False)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(True)
            self.backButton.place(x=0,y=540)
    def Back(self):
        self.state -= 1
        if self.state ==0:
            self.chooseRoomLabel.configure(text="      Choose Room")
        elif self.state == 1:
            self.calendarLabel.configure(text="      Choose Date")
        elif self.state == 2:
            self.timeLineLabel.configure(text="      Choose Time")
        self.Switch()
        pass
    '''============================RoomList============================'''
    def CreateRoomListGroup(self):
        self.roomListGroup = tk.Frame(self.mainCanvas,height=400,width=400,bd=0,background="black")

        self.roomListCanvas = tk.Canvas(self.roomListGroup,height=400,width=350,borderwidth=0, highlightthickness=0, background="#575757")
        self.roomLIstScrollbar = tk.Scrollbar(self.roomListGroup, orient=VERTICAL,command=self.roomListCanvas.yview)
        self.roomListCanvas.configure(yscrollcommand=self.roomLIstScrollbar.set)
        self.roomListCanvas.bind('<Configure>',lambda e:self.roomListCanvas.configure(scrollregion=self.roomListCanvas.bbox("all")))
        self.roomListSecondFram = tk.Frame(self.roomListCanvas,height=400,width=350,bd=0,background="#575757")
        self.roomListCanvas.create_window((0,0),window=self.roomListSecondFram,anchor="nw")

        self.roomListGroup.place(x=80,y=100)
        self.roomListCanvas.pack(side=LEFT,fill=BOTH)
        self.roomLIstScrollbar.pack(side=RIGHT,fill=Y)

        self.roomBtnList = []   #Room Btn List
        self.CreateRoom()
    def SetRoomListActive(self,_value):
        if _value == True:
            self.roomListGroup.place(x=80,y=100)
        else :
            self.roomListGroup.place_forget()
    def UpdateRoomList(self):
        for btn in self.roomBtnList:
            btn.destroy()
        self.roomBtnList = []   #Room Btn List
        self.CreateRoom()
    def CreateRoom(self):
        index = 0
        for room in self.BookSystem.rooms:
            roomName = room.name
            for event in room.events:
                if datetime.now() > event.start_time and datetime.now() < event.end_time:
                    roomName += ' (使用中)'
            self.roomBtnList.append(tk.Button(self.roomListSecondFram,text=roomName,height=2,width=46,command=lambda r = room.name : self.ClickRoomButton(r)))
            index += 1
        index = 0
        for btn in self.roomBtnList:
            btn.grid(row=index,column=0,padx=10)
            index += 1
    def ClickRoomButton(self, _roomName):
        self.state = 1
        self.targetRoom = _roomName
        self.chooseRoomLabel.config(text='      Choose Room     ' + _roomName)
        self.Enable()
    def BackToRoomList(self):
        self.state = 0
        self.chooseRoomLabel.configure(text="      Choose Room")
        self.Switch()
        pass
    def BackToTimeLine(self):
        self.state = 2
        self.SetRoomListActive(False)
        self.SetCalendarActive(False)
        self.SetTimeLineActive(True)
        self.SetCheckBoardActive(False)
        self.backButton.place(x=0,y=540)
        self.timeLineLabel.config(text='      Choose Time')
        pass
    '''============================Calendar============================'''
    def CreateCalendarGroup(self):
        self.calendarGroup = tk.Canvas(self.mainCanvas,height=400,width=550,bd =0, highlightthickness = 0,background="#dcdcdc")
        self.date = datetime.now()
        self.targetYear = self.date.year
        self.targetMonth = self.date.month
        self.yearOption = [self.date.year,self.date.year+1,self.date.year+2,self.date.year+3,self.date.year+4]
        self.yearComboBox = ttk.Combobox(self.calendarGroup,values=self.yearOption,state="readonly")
        self.yearComboBox.current(0)
        self.yearComboBox.bind("<<ComboboxSelected>>", lambda event:self.ChangeDateDropDown(0))
        self.monthOption = []
        for i in range(1,13):
            if i >= self.date.month:
                self.monthOption.append(i)
        self.monthComboBox = ttk.Combobox(self.calendarGroup,values=self.monthOption,state="readonly")
        self.monthComboBox.current(0)
        self.monthComboBox.bind("<<ComboboxSelected>>", lambda event:self.ChangeDateDropDown(1))

        self.calendarGroup.place(x=0,y=110)
        self.yearComboBox.place(x=75,y=20)
        self.monthComboBox.place(x=275,y=20)
        self.GenerateCalendar()
    def SetCalendarActive(self,_value):
        if _value == True:
            self.calendarGroup.place(x=0,y=110)
        else :
            self.calendarGroup.place_forget()
    def ChangeDateDropDown(self,_mode):
        if _mode == 0 :
            self.monthOption = []
            if self.yearComboBox.get() == str(self.date.year):
                for i in range(1,13):
                    if i >= self.date.month:
                        self.monthOption.append(i)
            else:
                for i in range(1,13):
                    self.monthOption.append(i)
            self.targetYear = int(self.yearComboBox.get())
            self.monthComboBox.destroy()
            self.monthComboBox = ttk.Combobox(self.calendarGroup,values=self.monthOption,state="readonly")
            self.monthComboBox.current(0)
            self.monthComboBox.place(x=275,y=20)
            self.monthComboBox.bind("<<ComboboxSelected>>", lambda event:self.ChangeDateDropDown(1))
        self.targetMonth = int(self.monthComboBox.get())
        self.UpdateCalendar()
    def CalculateWeek(self,year,month):
        week = 0
        yearBase = 0
        monthBaseNormal = [0,3,3,6,1,4,6,2,5,0,3,5]
        monthBaseLeap = [0,3,4,0,2,5,0,3,6,1,4,6]
        if(year%400==0 or (year%4==0 and year%100!=0)):
            yearBase = 1
        if(yearBase == 0):
            return ((year + int(year/4) + int(year/400) - int(year/100) - (yearBase+1) + monthBaseNormal[month-1] + 1))%7
        else:
            return ((year + int(year/4) + int(year/400) - int(year/100) - (yearBase+1) + monthBaseLeap[month-1] + 1))%7
    def GenerateCalendar(self):
        year = self.targetYear
        month = self.targetMonth
        self.calendarBackGround = tk.Canvas(self.calendarGroup,height=550,width=550, highlightthickness = 0,bd=0,background="#dcdcdc")
        self.calendarBackGround.place(x=80,y=80)
        self.dayBtnList =[]
        week = self.CalculateWeek(year,month)
        for i in range(1,32):
            dayBtnTmp = tk.Button(self.calendarBackGround, text=f"{i}", font=('Helvetica', '13'),height=2,width=5, command=lambda m=i:self.ClickCalendarButton(m))
            self.dayBtnList.append(dayBtnTmp)
        monthNum = 31
        if((year%400==0 or (year%4==0 and year%100!=0)) and month ==2):
            monthNum = 29
        elif(month == 2):
            monthNum = 28
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            monthNum = 30
        elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            monthNum = 31
        for i in range(1,monthNum+1):
            if (i <self.date.day and year == self.date.year and month == self.date.month):
                self.dayBtnList[i - 1].configure(state=tk.DISABLED)
                #dayBtnTmp = tk.Button(self.calendarBackGround, text=f"{i}", font=('Helvetica', '13'),height=2,width=5,state=tk.DISABLED, command=lambda:self.ChooseDate(year,month,i))
            else:
                #dayBtnTmp = tk.Button(self.calendarBackGround, text=f"{i}", font=('Helvetica', '13'),height=2,width=5, command=lambda m=i:self.ChooseDate(m))
                self.dayBtnList[i - 1].configure(state=tk.NORMAL)
        for i in range(0,31):
            if i+1 <= monthNum:
                self.dayBtnList[i].place(x=((i+week-1)%7)*50,y=int((i+week-1)/7)*50)
            else :
                self.dayBtnList[i].place_forget()
    def UpdateCalendar(self):
        year = self.targetYear
        month = self.targetMonth
        week = self.CalculateWeek(year,month)
        monthNum = 31
        if((year%400==0 or (year%4==0 and year%100!=0)) and month ==2):
            monthNum = 29
        elif(month == 2):
            monthNum = 28
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            monthNum = 30
        elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            monthNum = 31
        for i in range(1,monthNum+1):
            if (i <self.date.day and year == self.date.year and month == self.date.month):
                self.dayBtnList[i - 1].configure(state=tk.DISABLED)
            else:
                self.dayBtnList[i - 1].configure(state=tk.NORMAL)
        for i in range(0,31):
            if i+1 <= monthNum:
                self.dayBtnList[i].place(x=((i+week-1)%7)*50,y=int((i+week-1)/7)*50)
            else :
                self.dayBtnList[i].place_forget()
    def ClickCalendarButton(self,_day):
        self.TargetDay = _day
        self.state = 2
        self.calendarLabel.config(text='      Choose Date       '+str(self.targetYear)+'/'+str(self.targetMonth)+'/'+str(self.TargetDay))
        self.Enable()
        self.UpdateTimeLineEvent()
    '''============================TimeLine============================'''
    def CreateTimeLineGroup(self):
        self.timeLineGroup = tk.Canvas(self.mainCanvas,height=370,width=550, highlightthickness = 0,bd=0,background="#dcdcdc")

        self.timeLineFrame = tk.Frame(self.timeLineGroup,height=350,width=400,bd=0,background="#575757")
        self.timeLineCanvas = tk.Canvas(self.timeLineFrame,height=350,width=400,borderwidth=0, highlightthickness=0, background="#575757")
        self.timeLineScrollbar = tk.Scrollbar(self.timeLineFrame, orient=VERTICAL,command=self.timeLineCanvas.yview)
        self.timeLineCanvas.configure(yscrollcommand=self.timeLineScrollbar.set)
        self.timeLineCanvas.bind('<Configure>',lambda e:self.timeLineCanvas.configure(scrollregion=self.timeLineCanvas.bbox("all")))
        self.timeLineSecFram = tk.Frame(self.timeLineCanvas,height=300,width=350,bd=0,background="#575757")
        self.timeLineCanvas.create_window((0,0),window=self.timeLineSecFram,anchor="nw")
        self.timeLineImgSmall = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnSmall.png")
        self.timeLineImgBig = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnBig.png")
        self.timeLineList = []
        self.eventBoxList = []
        self.TargetStartHour = 0
        self.TargetStartMin = 0
        time = 0
        #Add button to TimeLine
        for thing in range(48):
            if time < 10:
                timeStr = '0' + str(time)
            else : 
                timeStr = str(time)
            if thing%2 == 0:
                self.timeLineList.append(tk.Button(self.timeLineSecFram,text=f'{timeStr}:00', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgBig,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 0 : self.ClickTimeLine(hr,min)))
            else:
                self.timeLineList.append(tk.Button(self.timeLineSecFram,text=f'{timeStr}:30', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgSmall,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 30 : self.ClickTimeLine(hr,min)))
                time += 1

        self.timeLineFrame.place(x=250,y=10,anchor="n")
        self.timeLineCanvas.pack(side=LEFT,fill=BOTH)
        self.timeLineScrollbar.pack(side=RIGHT,fill=Y)
        for thing in range(48):
            self.timeLineList[thing].grid(row=thing,column=0,padx=10)
    def SetTimeLineActive(self,_value):
        if _value == True:
            self.timeLineGroup.place(x=35,y=140)
        else :
            self.timeLineGroup.place_forget()
    def UpdateTimeLineEvent(self):
        for i in range(0 , 48):
            self.timeLineList[i].config(state=tk.NORMAL)
        for label in self.eventBoxList:
            label.destroy()
        self.eventBoxList.clear()
        room = self.BookSystem.getRoom(self.targetRoom)
        if room == None:
            self.BackToRoomList()
            return
        for event in room.events :
            dateTmp = event.start_time
            if dateTmp.year == self.targetYear and dateTmp.month == self.targetMonth and dateTmp.day == self.TargetDay :
                self.CreatEventLabel(event)
                pass
    def ClickTimeLine(self,_hour,_min):
        self.TargetStartHour = _hour
        self.TargetStartMin = _min
        self.state = 3
        self.timeLineLabel.config(text='      Choose Time       ' + str(self.TargetStartHour).zfill(2) + '：' + str(self.TargetStartMin).zfill(2) + '      to')
        self.Enable()
    def CreatEventLabel(self, _event):
        startPosition = _event.start_time.hour * 2
        if _event.start_time.minute != 0 :
            startPosition += 1
        endPosition = _event.end_time.hour * 2
        if _event.end_time.hour == 23 and _event.end_time.minute == 59 :
            endPosition += 2
        elif _event.end_time.minute != 0 :
            endPosition += 1
        for i in range(startPosition ,endPosition):
            self.timeLineList[i].config(state=tk.DISABLED)
        eventBoxCanvas = tk.Canvas(self.timeLineSecFram,background='red', relief=SUNKEN, highlightthickness=0,width=280,height=60 * (endPosition - startPosition))
        eventlabel = tk.Label(eventBoxCanvas, text = _event.name, font=('Helvetica', '13'),background='red')
        deleteBtn = tk.Button(eventBoxCanvas, text="delete",command=lambda event = _event, target = eventBoxCanvas : self.DeleteEvent(event, target))
        modifyBtn = tk.Button(eventBoxCanvas, text="modify",command=lambda event = _event : self.ModifyEvent(event))
        eventBoxCanvas.place(anchor='nw',x=10,y=60.05 * startPosition)
        eventlabel.place(anchor='nw',x=0,y=0)
        deleteBtn.place(anchor='nw',x=0,y=30)
        modifyBtn.place(anchor='nw',x=50,y=30)
        self.eventBoxList.append(eventBoxCanvas)
        pass
    def DeleteEvent(self, _event, target):
        self.BookSystem.getRoom(self.targetRoom).deleteEvent(_event)
        for i in self.eventBoxList:
            if i == target:
                i.destroy()
        self.eventBoxList.remove(target)
        self.UpdateTimeLineEvent()
        pass
    def ModifyEvent(self,_event):
        '''修改寫這邊'''
        self.titleNameStr.set('')
        self.OrganizerStr.set('')
        self.Participants.clear()
        self.Participants.append('')
        self.Participant.configure(values=self.Participants)
        self.Participant.current(0)
        self.Describe.delete(1.0,"end")
        self.state = 3
        self.timeLineLabel.config(text='      Choose Time       ' + str(_event.start_time.hour).zfill(2) + '：' + str(_event.start_time.minute).zfill(2) + '      to')
        self.titleNameStr.set(_event.name)
        self.leftTime.clear()
        count = 0
        currentEndTime = 0
        if _event.start_time.minute == 0:
            self.leftTime.append(str(_event.start_time.hour).zfill(2) + ':' + str(30).zfill(2))
            if _event.end_time.hour == _event.start_time.hour and _event.end_time.minute == 30:
                currentEndTime = count
            count += 1
        for i in range(_event.start_time.hour + 1 ,24):
            self.leftTime.append(str(i).zfill(2) + ':' + str(0).zfill(2))
            self.leftTime.append(str(i).zfill(2) + ':' + str(30).zfill(2))
            if _event.end_time.hour == i and _event.end_time.minute == 0:
                currentEndTime = count
            count += 1
            if _event.end_time.hour == i and _event.end_time.minute == 30:
                currentEndTime = count
            count += 1
        self.endTimeDropBox.configure(values=self.leftTime)
        self.endTimeDropBox.current(currentEndTime)
        self.Participants.clear()
        self.deletePaticipants.clear()
        self.Participants.append("")
        for i in range(len(_event.participants)):
            if i ==0 :
                self.OrganizerStr.set(_event.participants[i])
            else:
                self.Participants.append(_event.participants[i])
        self.Participant.configure(values=self.Participants)
        self.Participant.current(0)
        self.Describe.insert(1.0,_event.description)

        self.chooseRoomLabel.place(x=40,y=60)
        self.calendarLabel.place(x=40,y=85)
        self.timeLineLabel.place(x=40,y=110)
        self.SetRoomListActive(False)
        self.SetCalendarActive(False)
        self.SetTimeLineActive(False)
        self.EventGroup.place(x=0,y=150)
        self.endTimeDropBox.place(x=380,y=114)
        self.backButton.place(x=0,y=540)
        self.CheckingBtn.configure(command = lambda event = _event : self.CheckBoardModify(event))
        pass
    '''============================CheckBoard============================'''
    def CreateCheckBoardGroup(self):
        self.EventGroup = tk.Canvas(self.mainCanvas,height=400,width=550,bd=0, highlightthickness = 0, background="#dcdcdc")
        #End Time Drop Down
        self.leftTime = []
        self.endTimeDropBox = ttk.Combobox(self.mainCanvas,values=self.leftTime,state="readonly")

        self.EventGroup.place(x=0,y=150)
        self.endTimeDropBox.place(x = 350, y=110)
        #self.endTimeDropBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(0))
        #Title
        self.NameLabel = tk.Label(self.EventGroup,text="Event Title：", font=('Helvetica', '15'),background="#dcdcdc")
        self.NameLabel.place(x=0,y=40)
        self.titleNameStr = tk.StringVar()
        self.titleName = tk.Entry(self.EventGroup,textvariable=self.titleNameStr)
        self.titleName.place(x=120,y=48,width=200)
        self.NameErrorLabel = tk.Label(self.EventGroup,text="Error...", font=('Helvetica', '10'),fg='red',background="#dcdcdc")

        self.OrganizerLabel = tk.Label(self.EventGroup,text="Organizer (E-mail)：", font=('Helvetica', '15'),background="#dcdcdc")
        self.OrganizerLabel.place(x=0,y=70)
        self.OrganizerStr = tk.StringVar()
        self.Organizer = tk.Entry(self.EventGroup,textvariable=self.OrganizerStr)
        self.Organizer.place(x=180,y=78,width=200)
        self.OrganizerErrorLabel = tk.Label(self.EventGroup,text="Error...", font=('Helvetica', '10'),fg='red',background="#dcdcdc")

        self.ParticipantLabel = tk.Label(self.EventGroup,text="Participant (E-mail)：", font=('Helvetica', '15'),background="#dcdcdc")
        self.ParticipantLabel.place(x=0,y=100)
        self.Participants = []
        self.deletePaticipants = []
        self.Participants.append("")
        self.Participant = ttk.Combobox(self.EventGroup,values=self.Participants)
        self.Participant.bind("<<ComboboxSelected>>", lambda event:self.ChangeParticipantLabelDropDown)
        self.Participant.place(x = 200, y=108,width=200)
        self.addParticipant = tk.Button(self.EventGroup,text="Add",command=self.AddParticipantLabelDropDown)
        self.addParticipant.place(x = 420, y=108)
        self.deleteParticipant = tk.Button(self.EventGroup,text="Delete",command=self.DeleteParticipantLabelDropDown)
        self.deleteParticipant.place(x = 470, y=108)
        self.DescribeLabel = tk.Label(self.EventGroup,text="Event Describe：", font=('Helvetica', '15'),background="#dcdcdc")
        self.DescribeLabel.place(x = 0, y=130)
        self.Describe = tk.Text(self.EventGroup,width=70,height=13)
        self.Describe.place(x=0,y=170,anchor="nw")
        self.CheckingBtn = tk.Button(self.EventGroup,text="OK",command=self.CheckBoardFinish)
        self.CheckingBtn.place(relx=0.5,y=370)
    def SetCheckBoardActive(self,_value):
        if _value == True:
            self.EventGroup.place(x=0,y=150)
            self.endTimeDropBox.place(x=380,y=114)
            self.titleNameStr.set('')
            self.OrganizerStr.set('')
            self.Participants.clear()
            self.Participants.append('')
            self.Participant.configure(values=self.Participants)
            self.Participant.current(0)
            self.Describe.delete(1.0,"end")
            self.CheckingBtn.configure(command=self.CheckBoardFinish)
            self.UpdateLeftTime()
        else :
            self.EventGroup.place_forget()
            self.endTimeDropBox.place_forget()
    def UpdateLeftTime(self):
        self.leftTime.clear()
        if self.TargetStartHour < 10:
            hrStr = '0' + str(self.TargetStartHour)
        else:
            hrStr = str(self.TargetStartHour)
        if self.TargetStartMin == 0:
            minStr = '0' + str(self.TargetStartMin)
        else:
            minStr = str(self.TargetStartMin)
        if self.TargetStartMin == 0:
            self.leftTime.append(hrStr + ':30')
        for i in range(self.TargetStartHour + 1, 24):
            self.leftTime.append(str(i) + ':00')
            self.leftTime.append(str(i) + ':30')
        self.leftTime.append('24:00')
        self.endTimeDropBox.configure(values=self.leftTime)
        self.endTimeDropBox.current(0)
    def ChangeParticipantLabelDropDown(self):
        print(self.Participant.get())
        pass
    def AddParticipantLabelDropDown(self):
        self.Participants.append(self.Participant.get())
        self.Participant.configure(values=self.Participants)
        self.Participant.current(0)
        pass
    def DeleteParticipantLabelDropDown(self):
        if self.Participant.get() == "":
            return
        self.deletePaticipants.append(self.Participant.get())
        self.Participants.remove(self.Participant.get())
        self.Participant.configure(values=self.Participants)
        self.Participant.current(0)
        pass
    def CheckFormat(self):
        self.NameErrorLabel.place_forget()
        self.OrganizerErrorLabel.place_forget()
        complete_event = True
        if self.titleNameStr.get() == "" :
            self.NameErrorLabel.configure(text="標題不得為空...")
            complete_event = False
            self.NameErrorLabel.place(x=120,y=2)
        if self.OrganizerStr.get() == "" :
            self.OrganizerErrorLabel.configure(text="舉辦人信箱不得為空...")
            self.OrganizerErrorLabel.place(x=180,y=52)
            complete_event = False
        elif self.invalid_email(self.OrganizerStr.get()):
            self.OrganizerErrorLabel.configure(text="信箱格式錯誤...")
            self.OrganizerErrorLabel.place(x=180,y=52)
            complete_event = False
        
        self.final_participants = []
        self.final_participants.append(self.OrganizerStr.get())
        for i in range(1,len(self.Participants)):
            if self.invalid_email(self.Participants[i]):
                #TODO 信箱格式錯誤警告
                complete_event = False
                break               
            else:
                self.final_participants.append(self.Participants[i])
        print(self.Participants)
        return complete_event
    def CheckBoardFinish(self):
        if self.CheckFormat() == True:
            _endTime = self.endTimeDropBox.get()
            _endTimeSplit = _endTime.split(":")
            _hour = int(_endTimeSplit[0])
            _minute = int(_endTimeSplit[1])
            if _hour == 24 and _minute == 0:
                _hour = 23
                _minute = 59
            #print(self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,int(self.TargetStartHour),int(self.TargetStartMin)))
            #print(self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,_hour,_minute))
            room = self.BookSystem.getRoom(self.targetRoom) #傳入room得名字，回傳room
            if room == None:
                #TODO 提醒房間已不存在
                self.BackToRoomList()
                return
            new_event = Event.Event(self.BookSystem,room,self.titleNameStr.get(), self.Describe.get(1.0, tk.END+"-1c"), self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,self.TargetStartHour,self.TargetStartMin),self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,_hour,_minute))
            new_event.update_participants(self.final_participants)
            room.addEvent(new_event)
            self.UpdateTimeLineEvent()
            self.BackToTimeLine()
        pass
    def CheckBoardModify(self,_event):
        if self.CheckFormat() == True:
            _endTime = self.endTimeDropBox.get()
            _endTimeSplit = _endTime.split(":")
            _hour = int(_endTimeSplit[0])
            _minute = int(_endTimeSplit[1])
            if _hour == 24 and _minute == 0:
                _hour = 23
                _minute = 59
            print(self.BookSystem,self.titleNameStr.get())
            print(self.Describe.get(1.0, tk.END+"-1c"))
            print(self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,self.TargetStartHour,self.TargetStartMin))
            print(self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,_hour,_minute))
            print(self.final_participants)
            room = self.BookSystem.getRoom(self.targetRoom) #傳入room得名字，回傳room
            if room == None:
                #TODO 提醒房間已不存在
                self.BackToRoomList()
                return
            new_event = Event.Event(self.BookSystem,room,self.titleNameStr.get(), self.Describe.get(1.0, tk.END+"-1c"), self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,self.TargetStartHour,self.TargetStartMin),self.convert_to_RFC_datetime(self.targetYear,self.targetMonth,self.TargetDay,_hour,_minute))
            new_event.id = _event.id
            new_event.update_participants(self.final_participants)
            room.updateEvent(new_event)
            self.UpdateTimeLineEvent()
        pass
    '''============================OtherMethod============================'''
    def convert_to_RFC_datetime(self, year=1900, month=1, day=1, hour=0, minute=0):
        #hour-=8 #台灣時區
        dt = datetime(year, month, day, hour, minute, 0)
        print(type(dt))
        return dt
 
    def invalid_email(self,email): #檢查email格式
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return False 
        else:
            return True


