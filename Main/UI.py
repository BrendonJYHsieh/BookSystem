from os import stat
import tkinter.font as fnt
import tkinter as tk
from tkinter.constants import CENTER, END, FLAT, LEFT, SUNKEN, TOP
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
        self.app.attributes("-alpha",0.9)

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
        self.listBtn1 = tk.Button(self.app, text="  Booking      ", font=('Helvetica', '13'), image=self.btnIcon1, bg="#22736e",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ListBtnClick(0))
        self.btnIcon2 = tk.PhotoImage(file= r"Asset\Image\MyMeeting_Icon.png")
        self.btnIcon2 = self.btnIcon2.subsample(17,17)
        self.listBtn2 = tk.Button(self.app, text="  My meeting     ", font=('Helvetica', '13'), image=self.btnIcon2, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ListBtnClick(1))
        self.btnIcon3 = tk.PhotoImage(file= r"Asset\Image\ManagerMode_Icon.png")
        self.btnIcon3 = self.btnIcon3.subsample(17,17)
        self.listBtn3 = tk.Button(self.app, text="  Manage room  ", font=('Helvetica', '13'), image=self.btnIcon3, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ListBtnClick(2))
        self.btnIcon4 = tk.PhotoImage(file= r"Asset\Image\Setting_Icon.png")
        self.btnIcon4 = self.btnIcon4.subsample(17,17)
        self.listBtn4 = tk.Button(self.app, text="  Setting              ", font=('Helvetica', '12'), image=self.btnIcon4, bg="#20b2aa",activebackground="#22736e", disabledforeground="black",height=80,width=181, relief=SUNKEN, borderwidth=0,compound=LEFT, command=lambda : self.ListBtnClick(3))

        #Setting LabelFrame
        self.bookingGroup = tk.LabelFrame(self.app, text="Booking", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        self.UserGroup = tk.LabelFrame(self.app, text="My Meeting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        self.ManagerGroup = tk.LabelFrame(self.app, text="Manager Setting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        self.SettingGroup = tk.LabelFrame(self.app, text="Setting", font=('Helvetica', '20'),height=550,width=550,bd=0,background="#dcdcdc")
        #load other img
        self.Img1 = tk.PhotoImage(file= r"Asset\Image\Dogg01.png").subsample(3,3)
        self.Img2 = tk.PhotoImage(file= r"Asset\Image\Dogg02.png").subsample(3,3)
        self.Img3 = tk.PhotoImage(file= r"Asset\Image\Dogg03.png").subsample(3,3)
        self.Img4 = tk.PhotoImage(file= r"Asset\Image\Dogg04.png").subsample(3,3)
        self.Img5 = tk.PhotoImage(file= r"Asset\Image\Dogg05.png").subsample(3,3)

        #bookingGroup pack
        ImageTest1 = tk.Label(self.bookingGroup, image=self.Img1).pack(side=tk.LEFT)
        ImageTest2 = tk.Label(self.bookingGroup, image=self.Img2).pack(side=tk.LEFT)
        #UserGroup pack
        ImageTest3 = tk.Label(self.UserGroup, image=self.Img3).pack(side=tk.LEFT)
        #ManagerGroup pack
        ImageTest4 = tk.Label(self.ManagerGroup, image=self.Img4).pack(side=tk.LEFT)
        #SettingGroup pack
        ImageTest5 = tk.Label(self.SettingGroup, image=self.Img5).place(relx=0,rely=0)
        



        #Put the object to window
        self.listCanvas1.place(x=0,y=0)
        self.listCanvas2.place(x=0,y=0)
        self.listBtn1.place(x=0,y=0)
        self.listBtn2.place(x=0,y=85)
        self.listBtn3.place(x=0,y=170)
        self.listBtn4.place(x=0,y=520)
        self.bookingGroup.place(x=230,y=20)

        self.app.mainloop()
            
    #Open target's LabelFram and list button and close the other
    def ListBtnClick(self, _btnNum) :
        if _btnNum == 0:
            self.listBtn1.config(text="  Booking      ",bg="#22736e")
            self.listBtn1.config(command=0)
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ListBtnClick(1))
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ListBtnClick(2))
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ListBtnClick(3))
            self.bookingGroup.place(x=230,y=20)
            self.UserGroup.place_forget()
            self.ManagerGroup.place_forget()
            self.SettingGroup.place_forget()
        elif _btnNum == 1:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ListBtnClick(0))
            self.listBtn2.config(text="  My meeting   ",bg="#22736e")
            self.listBtn2.config(command=0)
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ListBtnClick(2))
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ListBtnClick(3))
            self.bookingGroup.place_forget()
            self.UserGroup.place(x=230,y=20)
            self.ManagerGroup.place_forget()
            self.SettingGroup.place_forget()
        elif _btnNum == 2:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ListBtnClick(0))
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ListBtnClick(1))
            self.listBtn3.config(text="  Manage room",bg="#22736e")
            self.listBtn3.config(command=0)
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ListBtnClick(3))
            self.bookingGroup.place_forget()
            self.UserGroup.place_forget()
            self.ManagerGroup.place(x=230,y=20)
            self.SettingGroup.place_forget()
        elif _btnNum == 3:
            self.listBtn1.config(text="  Booking          ",bg="#20b2aa")
            self.listBtn1.config(command=lambda : self.ListBtnClick(0))
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ListBtnClick(1))
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ListBtnClick(2))
            self.listBtn4.config(text="  Setting            ", bg="#22736e")
            self.listBtn4.config(command=0)
            self.bookingGroup.place_forget()
            self.UserGroup.place_forget()
            self.ManagerGroup.place_forget()
            self.SettingGroup.place(x=230,y=20)

application = BookSystemUI()


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
