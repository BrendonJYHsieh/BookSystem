from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text
from UI import BaseInterface
from core import Room

'''
Interface -> RoomList = 0 -> Calendar = 1 -> TimeLine = 2 -> CheckBoard = 3
'''
class BookInterface(BaseInterface.BaseInterface):
    state = 0

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
    def Enable(self):
        self.mainCanvas.place(x=230,y=20)
        self.interfaceTitle.place(x=10,y=10)
        if self.state == 0:
            self.chooseRoomLabel.place(x=40,y=60)
            self.SetRoomListActive(True)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(False)
        if self.state == 1:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.SetRoomListActive(False)
            self.SetCalendarActive(True)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(False)
        if self.state == 2:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.timeLineLabel.place(x=40,y=110)
            self.SetRoomListActive(False)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(True)
            self.SetCheckBoardActive(False)
        if self.state == 3:
            self.chooseRoomLabel.place(x=40,y=60)
            self.calendarLabel.place(x=40,y=85)
            self.timeLineLabel.place(x=40,y=110)
            self.SetRoomListActive(False)
            self.SetCalendarActive(False)
            self.SetTimeLineActive(False)
            self.SetCheckBoardActive(True)
    def Disable(self):
        self.mainCanvas.place_forget()
    '''============================RoomList============================'''
    def CreateRoomListGroup(self):
        self.roomListGroup = tk.Frame(self.mainCanvas,height=400,width=400,bd=0,background="#575757")

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
            self.roomBtnList.append(tk.Button(self.roomListSecondFram,text=room.name,height=2,width=46,command=lambda r = room.name : self.ClickRoomButton(r)))
            index += 1
        index = 0
        for btn in self.roomBtnList:
            btn.grid(row=index,column=0,padx=10)
            index += 1
    def ClickRoomButton(self, _roomName):
        self.state = 1
        self.chooseRoomLabel.config(text='      Choose Room     ' + _roomName)
        self.Enable()
    '''============================Calendar============================'''
    def CreateCalendarGroup(self):
        self.calendarGroup = tk.Canvas(self.mainCanvas,height=430,width=550,bd =0, highlightthickness = 0,background="#dcdcdc")
        self.date = datetime.datetime.now()
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
        self.yearComboBox.place(x=0,y=0)
        self.monthComboBox.place(x=200,y=0)
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
            self.monthComboBox.place(x=200,y=0)
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
        self.calendarBackGround.place(x=0,y=50)
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
    '''============================TimeLine============================'''
    def CreateTimeLineGroup(self):
        self.timeLineGroup = tk.Canvas(self.mainCanvas,height=450,width=550, highlightthickness = 0,bd=0,background="black")

        self.timeLineFrame = tk.Frame(self.timeLineGroup,height=350,width=400,bd=0,background="#575757")
        self.timeLineCanvas = tk.Canvas(self.timeLineFrame,height=400,width=400,borderwidth=0, highlightthickness=0, background="#575757")
        self.timeLineScrollbar = tk.Scrollbar(self.timeLineFrame, orient=VERTICAL,command=self.timeLineCanvas.yview)
        self.timeLineCanvas.configure(yscrollcommand=self.timeLineScrollbar.set)
        self.timeLineCanvas.bind('<Configure>',lambda e:self.timeLineCanvas.configure(scrollregion=self.timeLineCanvas.bbox("all")))
        self.timeLineSecFram = tk.Frame(self.timeLineCanvas,height=400,width=350,bd=0,background="#575757")
        self.timeLineCanvas.create_window((0,0),window=self.timeLineSecFram,anchor="nw")
        self.timeLineImgSmall = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnSmall.png")
        self.timeLineImgBig = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnBig.png")
        self.timeLineList = []
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
                self.timeLineList.append(tk.Button(self.timeLineSecFram,text=f'\n{timeStr}:00', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgSmall,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 0 : self.ClickTimeLine(hr,min)))
            else:
                self.timeLineList.append(tk.Button(self.timeLineSecFram,text=f'\n{timeStr}:30', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgBig,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 30 : self.ClickTimeLine(hr,min)))
                time += 1

        self.timeLineFrame.place(x=250,y=10,anchor="n")
        self.timeLineCanvas.pack(side=LEFT,fill=BOTH)
        self.timeLineScrollbar.pack(side=RIGHT,fill=Y)
        for thing in range(48):
            self.timeLineList[thing].grid(row=thing,column=0,padx=10)
        self.UpdateTimeLineEvent()
    def SetTimeLineActive(self,_value):
        if _value == True:
            self.timeLineGroup.place(x=0,y=140)
        else :
            self.timeLineGroup.place_forget()
    def UpdateTimeLineEvent(self):
        self.eventBoxList = []
        
        self.eventBoxCanvas = tk.Canvas(self.timeLineSecFram,background='red', relief=SUNKEN, highlightthickness=0,width=300,height=60)
        self.eventlabel = tk.Label(self.eventBoxCanvas,text="Event Name")
        self.eventBoxCanvas.place(anchor='nw',x=20,y=20)
        self.eventlabel.place(anchor='nw',x=0,y=0)

        self.eventBoxList.append(self.eventBoxCanvas)
    def ClickTimeLine(self,_hour,_min):
        self.TargetStartHour = _hour
        self.TargetStartMin = _min
        self.state = 3
        if self.TargetStartHour < 10:
            hrStr = '0' + str(self.TargetStartHour)
        else:
            hrStr = str(self.TargetStartHour)
        if self.TargetStartMin == 0:
            minStr = '0' + str(self.TargetStartMin)
        else:
            minStr = str(self.TargetStartMin)
        self.timeLineLabel.config(text='      Choose Time       ' + hrStr + '：' + minStr + '      to')
        self.Enable()
    '''============================CheckBoard============================'''
    def CreateCheckBoardGroup(self):
        self.EventGroup = tk.Canvas(self.mainCanvas,height=400,width=550,bd=0, highlightthickness = 0, background="#dcdcdc")
        #End Time Drop Down
        self.leftTime = []
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
        self.endTimeDropBox = ttk.Combobox(self.mainCanvas,values=self.leftTime,state="readonly")
        self.endTimeDropBox.current(0)

        self.EventGroup.place(x=0,y=100)
        self.endTimeDropBox.place(x = 350, y=110)
        #self.endTimeDropBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(0))
        #Title
        self.NameLabel = tk.Label(self.EventGroup,text="Event Title：", font=('Helvetica', '15'),background="#dcdcdc")
        self.NameLabel.place(x=0,y=50)
        self.titleNameStr = tk.StringVar()
        self.titleName = tk.Entry(self.EventGroup,textvariable=self.titleNameStr)
        self.titleName.place(x=120,y=58,width=200)

        self.OrganizerLabel = tk.Label(self.EventGroup,text="Organizer (E-mail)：", font=('Helvetica', '15'),background="#dcdcdc")
        self.OrganizerLabel.place(x=0,y=80)
        self.OrganizerStr = tk.StringVar()
        self.Organizer = tk.Entry(self.EventGroup,textvariable=self.OrganizerStr)
        self.Organizer.place(x=180,y=88,width=200)

        self.ParticipantLabel = tk.Label(self.EventGroup,text="Participant (E-mail)：", font=('Helvetica', '15'),background="#dcdcdc")
        self.ParticipantLabel.place(x=0,y=110)
        self.Participants = []
        self.Participant = ttk.Combobox(self.EventGroup,values=self.Participants)
        self.Participant.place(x = 200, y=118,width=200)
        self.addParticipant = tk.Button(self.EventGroup,text="Add")
        self.addParticipant.place(x = 420, y=118)
        self.deleteParticipant = tk.Button(self.EventGroup,text="Delete")
        self.deleteParticipant.place(x = 470, y=118)
        self.DescribeLabel = tk.Label(self.EventGroup,text="Event Describe：", font=('Helvetica', '15'),background="#dcdcdc")
        self.DescribeLabel.place(x = 0, y=140)
        self.DescribeStr = tk.StringVar()
        self.Describe = tk.Text(self.EventGroup,width=70,height=15)
        self.Describe.place(x=0,y=170,anchor="nw")
        self.CheckingBtn = tk.Button(self.EventGroup,text="OK")
        self.CheckingBtn.place(relx=0.5,y=380)
    def SetCheckBoardActive(self,_value):
        if _value == True:
            self.EventGroup.place(x=0,y=170)
            self.endTimeDropBox.place(x=380,y=114)
        else :
            self.EventGroup.place_forget()
            self.endTimeDropBox.place_forget()
    def CheckBoardFinish():
        pass
    def CheckBoardCancel():
        pass

