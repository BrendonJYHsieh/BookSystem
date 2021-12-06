from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text
from core import Room
#import BookSystem
#import Room
#import Event

class BookSystemUI():
    def __init__(self):
        return
    def initialUI(self):
        self.app = tk.Tk()
        #Window setting
        self.app.title("Booking System.ver0.1")
        self.app.geometry("800x600")
        self.app.resizable(0,0)
        self.app.config(background="#dcdcdc")
        self.app.config(borderwidth=0)
        self.app.attributes("-alpha",0.95)
        self.screenState = 0
        #Testing image
        #pixelVirtual = tk.PhotoImage(width=1,height=1)

        #List canvas setting
        self.listCanvas1 = tk.Canvas(self.app, bg="#22736e",height=600,width=210)
        self.listCanvas1.config(highlightthickness=0)
        self.listCanvas2 = tk.Canvas(self.app, bg="#20b2aa",height=600,width=185)
        self.listCanvas2.config(highlightthickness=0)

        #List Button setting
        self.btnIcon1 = tk.PhotoImage(file= r"Asset\Image\Booking_Icon.png")
        self.btnIcon1 = self.btnIcon1.subsample(17,17)
        self.listBtn1 = tk.Button(self.app, text="  Booking      ", font=('Helvetica', '13'), image=self.btnIcon1, bg="#22736e",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ClickListBtn(0))
        self.btnIcon2 = tk.PhotoImage(file= r"Asset\Image\MyMeeting_Icon.png")
        self.btnIcon2 = self.btnIcon2.subsample(17,17)
        self.listBtn2 = tk.Button(self.app, text="  My meeting     ", font=('Helvetica', '13'), image=self.btnIcon2, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ClickListBtn(1))
        self.btnIcon3 = tk.PhotoImage(file= r"Asset\Image\ManagerMode_Icon.png")
        self.btnIcon3 = self.btnIcon3.subsample(17,17)
        self.listBtn3 = tk.Button(self.app, text="  Manage room  ", font=('Helvetica', '13'), image=self.btnIcon3, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ClickListBtn(2))
        self.btnIcon4 = tk.PhotoImage(file= r"Asset\Image\Setting_Icon.png")
        self.btnIcon4 = self.btnIcon4.subsample(17,17)
        self.listBtn4 = tk.Button(self.app, text="  Setting              ", font=('Helvetica', '13'), image=self.btnIcon4, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ClickListBtn(3))

        #Setting LabelFrame
        #Booking System - Room
        self.bookingGroup = tk.LabelFrame(self.app, text="Booking", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        self.RoomLabel = tk.Label(self.bookingGroup,text="\n      Choose Room", font=('Helvetica', '15'),background="#dcdcdc")
        self.DateLabel = tk.Label(self.bookingGroup,text="      Choose Date", font=('Helvetica', '15'),background="#dcdcdc")
        self.TimeLabel = tk.Label(self.bookingGroup,text="      Choose Time", font=('Helvetica', '15'),background="#dcdcdc")
        self.RoomList_Frame = tk.Frame(self.bookingGroup,height=400,width=400,bd=0,background="#575757")
        self.RoomList_Canvas = tk.Canvas(self.RoomList_Frame,height=400,width=350,borderwidth=0, highlightthickness=0, background="#575757")
        self.RoomlIst_Scrollbar = tk.Scrollbar(self.RoomList_Frame, orient=VERTICAL,command=self.RoomList_Canvas.yview)
        self.RoomList_Canvas.configure(yscrollcommand=self.RoomlIst_Scrollbar.set)
        self.RoomList_Canvas.bind('<Configure>',lambda e:self.RoomList_Canvas.configure(scrollregion=self.RoomList_Canvas.bbox("all")))
        self.second_Fram = tk.Frame(self.RoomList_Canvas,height=400,width=350,bd=0,background="#575757")
        self.RoomList_Canvas.create_window((0,0),window=self.second_Fram,anchor="nw")
        self.roomBtnList = []
        self.CreateRoom()
        '''for thing in range(1):
            #Add button to list
            tk.Button(self.second_Fram,text=f'Room  {thing}',height=2,width=46,command=lambda : self.ClickRoomBtn(f'Room  {thing}')).grid(row=thing,column=0,padx=10)
        '''
        #Booking System - Date
        self.DateGroup = tk.LabelFrame(self.bookingGroup,height=550,width=550,bd=0,background="#dcdcdc")
        #Booking System - TimeLine
        self.TimeLineGroup = tk.LabelFrame(self.bookingGroup,height=550,width=550,bd=0,background="#dcdcdc")
        #Booking System - Event
        self.EventGroup = tk.Canvas()
        #User's book
        self.UserGroup = tk.LabelFrame(self.app, text="My Meeting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        #Manager setting
        self.ManagerGroup = tk.LabelFrame(self.app, text="Manager Setting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        #App setting
        self.SettingGroup = tk.LabelFrame(self.app, text="Setting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        
        #load other img
        self.Img3 = tk.PhotoImage(file= r"Asset\Image\Dogg03.png").subsample(3,3)
        self.Img4 = tk.PhotoImage(file= r"Asset\Image\Dogg04.png").subsample(3,3)
        self.Img5 = tk.PhotoImage(file= r"Asset\Image\Dogg05.png").subsample(3,3)
    

        self.room_name_strv = tk.StringVar()
        self.room_description_strv =  tk.StringVar()

        self.add_room = tk.Button(self.ManagerGroup,text='add',command=lambda : self.BookSystem.addRoom(Room.Room(self.room_name_strv.get())))
        self.edit_room = tk.Button(self.ManagerGroup,text='edit')
        self.delete_room = tk.Button(self.ManagerGroup,text='delete',command=lambda : self.BookSystem.deleteRoom(Room.Room(self.room_name_strv.get())))
        self.room_name_label = tk.Label(self.ManagerGroup,text='Room Name')
        
        self.room_name_strv.set('mew mew')
        self.room_name = tk.Entry(self.ManagerGroup,textvariable=self.room_name_strv)
        self.room_description_label = tk.Label(self.ManagerGroup,text='Room Description')
        
        self.room_description_strv.set('haha cat')
        self.room_description = tk.Entry(self.ManagerGroup,textvariable=self.room_description_strv)

        self.room_list = tk.Listbox(self.ManagerGroup)
        self.room_scroll = tk.Scrollbar(self.room_list, orient=tk.VERTICAL,command = self.room_list.yview)

        self.room_list.config(yscrollcommand = self.room_scroll)
        self.room_list.bind('<<ListboxSelect>>',self.roomListSelect)
        ####################### manage group place
        self.add_room.place(x=0,y=450,width=120)
        self.edit_room.place(x=150,y=450,width=120)
        self.delete_room.place(x=300,y=450,width=120)
        self.room_name_label.place(x=0,y=50)
        self.room_name.place(x=0,y=100,width=420)
        
        self.room_description_label.place(x=0,y=200)
        self.room_description.place(x=0,y=250,width=420)
        
        
        self.room_list.place(x=430,y=0,height=500)      
        self.room_scroll.place(x=100,y=0,height=500)
        #######################
        
        #Put the object to window
        self.listCanvas1.place(x=0,y=0)
        self.listCanvas2.place(x=0,y=0)
        self.listBtn1.place(x=0,y=0)
        self.listBtn2.place(x=0,y=85)
        self.listBtn3.place(x=0,y=170)
        self.listBtn4.place(x=0,y=520)
        self.bookingGroup.place(x=230,y=20)
        #bookingGroup pack
        self.RoomLabel.place(x=0,y=0)
        
        self.RoomList_Frame.place(x=80,y=100)
        self.RoomList_Canvas.pack(side=LEFT,fill=BOTH)
        self.RoomlIst_Scrollbar.pack(side=RIGHT,fill=Y)
        #UserGroup pack
        ImageTest3 = tk.Label(self.UserGroup, image=self.Img3).pack(side=tk.LEFT)
        #ManagerGroup pack
        #ImageTest4 = tk.Label(self.ManagerGroup, image=self.Img4).pack(side=tk.LEFT)
        #SettingGroup pack
        ImageTest5 = tk.Label(self.SettingGroup, image=self.Img5).place(relx=0,rely=0)

    def runUI(self):
        self.app.mainloop()
    
    def roomListInsert(self,name):
        self.room_list.insert(tk.END,name)
    def roomListDelete(self,name):
        idx = self.room_list.get(0, tk.END).index(name)
        self.room_list.delete(idx)
        self.room_name_strv.set("")
    def roomListSelect(self,event):
        selection = self.room_list.curselection()
        if selection != ():
            self.room_name_strv.set(self.room_list.get(selection[0]))
        else: #沒選到任何item時設為空字串
            self.room_name_strv.set("")
            
    #Open target's LabelFram and list button and close the other
    def ClickListBtn(self, _btnNum) :
        if _btnNum == 0:
            self.listBtn1.config(text="  Booking      ",bg="#22736e")
            self.listBtn1.config(command=0)
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ClickListBtn(1))
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ClickListBtn(2))
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ClickListBtn(3))
            self.bookingGroup.place(x=230,y=20)
            self.UserGroup.place_forget()
            self.ManagerGroup.place_forget()
            self.SettingGroup.place_forget()
        elif _btnNum == 1:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ClickListBtn(0))
            self.listBtn2.config(text="  My meeting   ",bg="#22736e")
            self.listBtn2.config(command=0)
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ClickListBtn(2))
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ClickListBtn(3))
            self.bookingGroup.place_forget()
            self.UserGroup.place(x=230,y=20)
            self.ManagerGroup.place_forget()
            self.SettingGroup.place_forget()
        elif _btnNum == 2:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ClickListBtn(0))
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ClickListBtn(1))
            self.listBtn3.config(text="  Manage room",bg="#22736e")
            self.listBtn3.config(command=0)
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ClickListBtn(3))
            self.bookingGroup.place_forget()
            self.UserGroup.place_forget()
            self.ManagerGroup.place(x=230,y=20)
            self.SettingGroup.place_forget()
        elif _btnNum == 3:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ClickListBtn(0))
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ClickListBtn(1))
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ClickListBtn(2))
            self.listBtn4.config(text="  Setting            ", bg="#22736e")
            self.listBtn4.config(command=0)
            self.bookingGroup.place_forget()
            self.UserGroup.place_forget()
            self.ManagerGroup.place_forget()
            self.SettingGroup.place(x=230,y=20)

    def CreateRoom(self):
        index = 0
        for room in self.BookSystem.rooms:
            self.roomBtnList.append(tk.Button(self.second_Fram,text=room.name,height=2,width=46,command=lambda r = room.name : self.ClickRoomBtn(r)))
            index += 1
        index = 0
        for btn in self.roomBtnList:
            btn.grid(row=index,column=0,padx=10)
            index += 1
        
    def ClickRoomBtn(self, RoomName):
        self.RoomList_Frame.place_forget()
        self.screenState = self.screenState+1
        self.RoomLabel.config(text='\n      Choose Room     ' + RoomName)
        self.DateLabel.place(x=0,y=50)
        self.DateGroup.place(x=0,y=100)
        self.date = datetime.datetime.now()

        self.yearOption = [self.date.year,self.date.year+1,self.date.year+2,self.date.year+3,self.date.year+4]
        self.yearComboBox = ttk.Combobox(self.DateGroup,values=self.yearOption,state="readonly")
        self.yearComboBox.current(0)
        self.yearComboBox.place(x=0,y=0)
        self.yearComboBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(0))

        self.monthOption = []
        for i in range(1,13):
            if i >= self.date.month:
                self.monthOption.append(i)
        self.monthComboBox = ttk.Combobox(self.DateGroup,values=self.monthOption,state="readonly")
        self.monthComboBox.current(0)
        self.monthComboBox.place(x=200,y=0)
        self.monthComboBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(1))

        self.GenerateCalendar(self.date.year,self.date.month,self.date.day)

    def DropDownChange(self,mode):
        if(mode==0):
            self.monthOption = []
            if self.yearComboBox.get() == str(self.date.year):
                for i in range(1,13):
                    if i >= self.date.month:
                        self.monthOption.append(i)
            else:
                for i in range(1,13):
                    self.monthOption.append(i)
            self.monthComboBox = ttk.Combobox(self.DateGroup,values=self.monthOption,state="readonly")
            self.monthComboBox.current(0)
            self.monthComboBox.place(x=200,y=0)
            self.monthComboBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(1))
        self.CalendarBackGround.destroy()
        self.GenerateCalendar(self.yearOption[self.yearComboBox.current()],self.monthOption[self.monthComboBox.current()],1)

    def GenerateCalendar(self,year,month,day):
        self.CalendarBackGround = tk.LabelFrame(self.DateGroup,height=550,width=550,bd=0,background="#dcdcdc")
        self.CalendarBackGround.place(x=0,y=50)
        self.dayOption =[]
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
                dayBtnTmp = tk.Button(self.CalendarBackGround, text=f"{i}", font=('Helvetica', '13'),height=2,width=5,state=tk.DISABLED, command=lambda:self.ChooseDate(year,month,i))
            else:
                dayBtnTmp = tk.Button(self.CalendarBackGround, text=f"{i}", font=('Helvetica', '13'),height=2,width=5, command=lambda m=i:self.ChooseDate(year,month,m))
            dayBtnTmp.place(x=((i+week-1)%7)*50,y=int((i+week-1)/7)*50)

    def ChooseDate(self,year,month,day):
        self.TimeLineGroup.destroy()
        self.TimeLineGroup = tk.LabelFrame(self.bookingGroup,height=550,width=550,bd=0,background="#dcdcdc")
        self.DateLabel.config(text='      Choose Date       '+str(year)+'/'+str(month)+'/'+str(day))
        self.DateGroup.place_forget()
        self.TimeLabel.place(x = 0, y=75)
        self.TimeLineGroup.place(x=0,y=100)
        
        self.TimeLine_Frame = tk.Frame(self.TimeLineGroup,height=350,width=400,bd=0,background="#575757")
        self.TimeLine_Canvas = tk.Canvas(self.TimeLine_Frame,height=400,width=400,borderwidth=0, highlightthickness=0, background="#575757")
        self.TimeLine_Scrollbar = tk.Scrollbar(self.TimeLine_Frame, orient=VERTICAL,command=self.TimeLine_Canvas.yview)
        self.TimeLine_Canvas.configure(yscrollcommand=self.TimeLine_Scrollbar.set)
        self.TimeLine_Canvas.bind('<Configure>',lambda e:self.TimeLine_Canvas.configure(scrollregion=self.TimeLine_Canvas.bbox("all")))
        self.TimeLine_SecFram = tk.Frame(self.TimeLine_Canvas,height=400,width=350,bd=0,background="#575757")
        self.TimeLine_Canvas.create_window((0,0),window=self.TimeLine_SecFram,anchor="nw")
        self.timeLineImgSmall = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnSmall.png")
        self.timeLineImgBig = tk.PhotoImage(file= r"Asset\Image\TimeLineBtnBig.png")
        self.timeLineList = []
        time = 0
        #Add button to TimeLine
        for thing in range(48):
            if time < 10:
                timeStr = '0' + str(time)
            else : 
                timeStr = str(time)
            if thing%2 == 0:
                self.timeLineList.append(tk.Button(self.TimeLine_SecFram,text=f'\n{timeStr}:00', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgSmall,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 0 : self.GenerateEvent(hr,min)))
            else:
                self.timeLineList.append(tk.Button(self.TimeLine_SecFram,text=f'\n{timeStr}:30', font=('Helvetica', '13'),fg='#dcdcdc',image=self.timeLineImgBig,background="#575757",activebackground="#575757", disabledforeground="black", relief=SUNKEN, borderwidth=0,compound=LEFT,command=lambda hr = time,min = 30 : self.GenerateEvent(hr,min)))
                time += 1
        
        self.TimeLine_Frame.place(x=250,y=20,anchor="n")
        self.TimeLine_Canvas.pack(side=LEFT,fill=BOTH)
        self.TimeLine_Scrollbar.pack(side=RIGHT,fill=Y)

        self.EventBoxCanvas = tk.Canvas(self.TimeLine_SecFram,background='red', relief=SUNKEN, highlightthickness=0,width=300,height=60)
        self.Eventlabel = tk.Label(self.EventBoxCanvas,text="Event Name")
        for thing in range(48):
            self.timeLineList[thing].grid(row=thing,column=0,padx=10)
        self.EventBoxCanvas.place(anchor='nw',x=20,y=20)
        self.Eventlabel.place(anchor='nw',x=0,y=0)

    def GenerateEvent(self,hr,min):
        hrStr = ""
        minStr = ""
        if hr < 10:
            hrStr = '0' + str(hr)
        else:
            hrStr = str(hr)
        if min == 0:
            minStr = '0' + str(min)
        else:
            minStr = str(min)
        self.TimeLabel.config(text='      Choose Time       ' + hrStr + '：' + minStr + '      to')
        self.TimeLineGroup.destroy()
        self.EventGroup.destroy()
        self.EventGroup = tk.Canvas(self.bookingGroup,height=550,width=550,bd=0, highlightthickness = 0, background="#dcdcdc")
        self.EventGroup.place(x=0,y=100)
        #End Time Drop Down
        self.leftTime = []
        if min == 0:
            self.leftTime.append(hrStr + ':30')
        for i in range(hr + 1, 24):
            self.leftTime.append(str(i) + ':00')
            self.leftTime.append(str(i) + ':30')
        self.endTimeDropBox = ttk.Combobox(self.bookingGroup,values=self.leftTime,state="readonly")
        self.endTimeDropBox.current(0)
        self.endTimeDropBox.place(x = 350, y=80)
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
    
    

#application = BookSystemUI()


"""UI_switch = 0 #room list -> 0 room info -> 1 event modify -> 2

def drawRoomList(): #list all room
    return
def drawRoomInfo(): #can modify room info
    return
def drawEventInfo(): #can modify event info
    return



def draw():
    if UI_switch == 0:
        drawRoomList()
    elif UI_switch == 1:
        drawRoomInfo()
    elif UI_switch == 2:
        drawEventInfo()
    return

def redraw():
    return


def roomBaseInfoModify(room):
    room.name = "xxx"
    room.description = "xxx"

def roomEventsModify(room):
    UI_switch = 2

def eventModify(event):
    event.name = "xxx"
    event.description = "xxx"
    event.start_time = None
    event.end_time = None

def eventParticipantModify(event,emails):
    event.participants = emails
"""
