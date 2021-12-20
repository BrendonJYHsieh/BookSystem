from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, DISABLED, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text
from core import Room
from UI import BaseInterface,LogInInterface,BookInterface
#import BookSystem
#import Room
#import Event

class BookSystemUI():
    BookSystem = None
    def __init__(self,_BookSystem):
        self.BookSystem = _BookSystem
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

        self.add_room = tk.Button(self.ManagerGroup,text='add',command=lambda : self.BookSystem.addRoom(Room.Room(self.BookSystem,self.room_name_strv.get())))
        self.edit_room = tk.Button(self.ManagerGroup,text='edit',command=self.roomListUpdate)
        self.delete_room = tk.Button(self.ManagerGroup,text='delete',command=lambda : self.BookSystem.deleteRoom(Room.Room(self.BookSystem,self.room_name_strv.get())))
        self.room_name_label = tk.Label(self.ManagerGroup,text='Room Name')
        
        self.room_name_strv.set('mew mew')
        self.room_name = tk.Entry(self.ManagerGroup,textvariable=self.room_name_strv)

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

        self.bookInterface = BookInterface.BookInterface(self.app,self.BookSystem)
        self.bookInterface.SetActive(True)

        #bookingGroup pack
        #UserGroup pack
        ImageTest3 = tk.Label(self.UserGroup, image=self.Img3).pack(side=tk.LEFT)
        #ManagerGroup pack
        #ImageTest4 = tk.Label(self.ManagerGroup, image=self.Img4).pack(side=tk.LEFT)
        #SettingGroup pack
        ImageTest5 = tk.Label(self.SettingGroup, image=self.Img5).place(relx=0,rely=0)
        self.app.after(5000,self.regular_update)

    def runUI(self):
        self.loginInterface = LogInInterface.LoginInterface(self.app,self.BookSystem)
        self.loginInterface.SetActive(0)
        self.app.mainloop()
    def regular_update(self):
        self.BookSystem.check_db_update()
        self.app.after(5000,self.regular_update)
    
    def roomListClear(self):
        self.room_list.delete(0,'end')

    def roomListInsert(self,name):
        self.room_list.insert(tk.END,name)
        self.bookInterface.UpdateRoomList()
    def roomListDelete(self,name):
        idx = self.room_list.get(0, tk.END).index(name)
        self.room_list.delete(idx)
        self.room_name_strv.set("")
        self.bookInterface.UpdateRoomList()
        self.bookInterface.BackToRoomList()
    def roomListUpdate(self):
        print("room update")
        selection = self.room_list.curselection()
        old_name = ""
        if selection != ():
            old_name = self.room_list.get(selection)
            self.BookSystem.updateRoom(old_name,self.room_name_strv.get())
            self.room_list.delete(selection)    
            self.room_list.insert(selection,self.room_name_strv.get())            
            self.bookInterface.UpdateRoomList()
        else:
            #TODO 警告
            return        
        
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
            self.bookInterface.SetActive(True)
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
            self.bookInterface.SetActive(False)
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
            self.bookInterface.SetActive(False)
            self.UserGroup.place_forget()
            self.ManagerGroup.place(x=230,y=20)
            self.SettingGroup.place_forget()
        elif _btnNum == 3:
            self.listBtn1.config(text="  Booking      ",bg="#22736e")
            self.listBtn1.config(command=0)
            self.listBtn2.config(text="  My meeting     ",bg="#20b2aa")
            self.listBtn2.config(command=lambda : self.ClickListBtn(1))
            self.listBtn3.config(text="  Manage room  ",bg="#20b2aa")
            self.listBtn3.config(command=lambda : self.ClickListBtn(2))
            self.listBtn4.config(text="  Setting              ", bg="#20b2aa")
            self.listBtn4.config(command=lambda : self.ClickListBtn(3))
            self.bookInterface.SetActive(True)
            self.UserGroup.place_forget()
            self.ManagerGroup.place_forget()
            self.SettingGroup.place_forget()
            self.bookInterface.BackToRoomList()
            self.loginInterface.SetActive(1)
            

    

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
