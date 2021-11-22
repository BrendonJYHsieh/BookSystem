from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
#import BookSystem
#import Room
#import Event

class BookSystemUI():
    def __init__(self):
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
        self.RoomList_Frame = tk.Frame(self.bookingGroup,height=400,width=400,bd=0,background="#575757")
        self.RoomList_Canvas = tk.Canvas(self.RoomList_Frame,height=400,width=350,borderwidth=0, highlightthickness=0, background="#575757")
        self.RoomlIst_Scrollbar = tk.Scrollbar(self.RoomList_Frame, orient=VERTICAL,command=self.RoomList_Canvas.yview)
        self.RoomList_Canvas.configure(yscrollcommand=self.RoomlIst_Scrollbar.set)
        self.RoomList_Canvas.bind('<Configure>',lambda e:self.RoomList_Canvas.configure(scrollregion=self.RoomList_Canvas.bbox("all")))
        self.second_Fram = tk.Frame(self.RoomList_Canvas,height=400,width=350,bd=0,background="#575757")
        self.RoomList_Canvas.create_window((0,0),window=self.second_Fram,anchor="nw")
        for thing in range(1):
            tk.Button(self.second_Fram,text=f'Room  {thing}',height=2,width=46,command=lambda : self.ClickRoomBtn(f'Room  {thing}')).grid(row=thing,column=0,padx=10)
        #Booking System - Date
        self.RoomLabeDate = tk.LabelFrame(self.bookingGroup, text="      Choose Date", font=('Helvetica', '15'),height=550,width=550,bd=0,background="white")
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
    

        add_room = tk.Button(self.ManagerGroup,text='add')
        edit_room = tk.Button(self.ManagerGroup,text='edit')
        delete_room = tk.Button(self.ManagerGroup,text='delete')
        room_title_label = tk.Label(self.ManagerGroup,text='Room Name')
        room_title_strv = tk.StringVar()
        room_title_strv.set('mew mew')
        room_title = tk.Entry(self.ManagerGroup,textvariable=room_title_strv)
        room_description_label = tk.Label(self.ManagerGroup,text='Room Description')
        room_description_strv =  tk.StringVar()
        room_description_strv.set('haha cat')
        room_description = tk.Entry(self.ManagerGroup,textvariable=room_description_strv)

        room_list = tk.Listbox(self.ManagerGroup)
        room_scroll = tk.Scrollbar(room_list, orient=tk.VERTICAL,command = room_list.yview)

        room_list.insert(tk.END,'cat livingroom')
        room_list.insert(tk.END,'cat bathroom')
        room_list.insert(tk.END,'cat kitchen')
        for i in range(30):
            room_list.insert(END,str(i))
        room_list.config(yscrollcommand = room_scroll)
        ####################### manage group place
        add_room.place(x=0,y=450,width=120)
        edit_room.place(x=150,y=450,width=120)
        delete_room.place(x=300,y=450,width=120)
        room_title_label.place(x=0,y=50)
        room_title.place(x=0,y=100,width=420)
        
        room_description_label.place(x=0,y=200)
        room_description.place(x=0,y=250,width=420)
        
        
        room_list.place(x=430,y=0,height=500)      
        room_scroll.place(x=100,y=0,height=500)
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

        self.app.mainloop()
            
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

    def ClickRoomBtn(self, RoomName):
        self.screenState = self.screenState+1
        self.RoomLabel.config(text='\n      Choose Room     '+RoomName)        
        self.RoomLabeDate.place(x=0,y=50)
        self.date = datetime.datetime.now()

        self.yearOption = [self.date.year,self.date.year+1,self.date.year+2,self.date.year+3,self.date.year+4]
        self.yearComboBox = ttk.Combobox(self.RoomLabeDate,values=self.yearOption,state="readonly")
        self.yearComboBox.current(0)
        self.yearComboBox.place(x=0,y=0)
        self.yearComboBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(0))

        self.monthOption = []
        for i in range(1,13):
            if i >= self.date.month:
                self.monthOption.append(i)
        self.monthComboBox = ttk.Combobox(self.RoomLabeDate,values=self.monthOption,state="readonly")
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
            self.monthComboBox = ttk.Combobox(self.RoomLabeDate,values=self.monthOption,state="readonly")
            self.monthComboBox.current(0)
            self.monthComboBox.place(x=200,y=0)
            self.monthComboBox.bind("<<ComboboxSelected>>", lambda event:self.DropDownChange(1))
        self.GenerateCalendar(self.yearOption[self.yearComboBox.current()],self.monthOption[self.monthComboBox.current()],1)

    def GenerateCalendar(self,year,month,day):
        self.CalendarBackGround = tk.LabelFrame(self.RoomLabeDate,height=550,width=550,bd=0,background="white")
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
    def ChooseDate(self,year,month,day):
        self.RoomLabeDate.config(text='     Choose Date       '+str(year)+'/'+str(month)+'/'+str(day))
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
