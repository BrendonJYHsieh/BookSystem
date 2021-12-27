from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text
import re
from UI import BaseInterface
from core import Room,Event

class UsersBookInterface(BaseInterface.BaseInterface):
    def __init__(self,_parent,_booksystem):
        super().__init__(_parent)
        self.bookSystem = _booksystem
        self.interfaceTitle = tk.Label(self.mainCanvas,text="My Meeting", font=('Helvetica', '20'),background="#dcdcdc")
        self.interfaceTitle.place(x=10,y=10)
        self.eventList = []

        self.eventListGroup = tk.Frame(self.mainCanvas,height=400,width=400,bd=0,background="black")
        self.eventListCanvas = tk.Canvas(self.eventListGroup,height=400,width=350,borderwidth=0, highlightthickness=0, background="#575757")
        self.eventLIstScrollbar = tk.Scrollbar(self.eventListGroup, orient=VERTICAL,command=self.eventListCanvas.yview)
        self.eventListCanvas.configure(yscrollcommand=self.eventLIstScrollbar.set)
        self.eventListCanvas.bind('<Configure>',lambda e:self.eventListCanvas.configure(scrollregion=self.eventListCanvas.bbox("all")))
        self.eventListSecondFram = tk.Frame(self.eventListCanvas,height=400,width=350,bd=0,background="#575757")
        self.eventListCanvas.create_window((0,0),window=self.eventListSecondFram,anchor="nw")

        self.eventListGroup.place(x=80,y=100)
        self.eventListCanvas.pack(side=LEFT,fill=BOTH)
        self.eventLIstScrollbar.pack(side=RIGHT,fill=Y)

        index = 0
        events = self.bookSystem.getUserEvents(self.bookSystem.auth.CurrentUser)
        for event in events:
            self.CreateEvent(index, event)

    def Enable(self):
        super().Enable()
        pass
    def UpdateEventList(self):
        for btn in self.eventList:
            btn.destroy()
        self.eventList = []
        index = 0
        events = self.bookSystem.getUserEvents(self.bookSystem.auth.CurrentUser)
        #print('-----------------------')
        #print(self.bookSystem.auth.CurrentUser)
        events = self.bookSystem.getParticipant("frakwuo1@gmail.com").events
        print(events)
        for event in events:
            self.CreateEvent(index, event)
            index += 1
        pass
    def CreateEvent(self,_index, _event):
        eventBoxCanvas = tk.Canvas(self.eventListSecondFram,background='red', relief=SUNKEN, highlightthickness=0,width=280,height=80)
        eventlabel = tk.Label(eventBoxCanvas, text = _event.name, font=('Helvetica', '13'),background='red')
        timeStr = str(_event.start_time.year) + '/' + str(_event.start_time.month) + '/' + str(_event.start_time.day) + ' ' + str(_event.start_time.hour).zfill(2) + ':' + str(_event.start_time.minute).zfill(2) +' ~ ' +  str(_event.end_time.hour).zfill(2) + ':' + str(_event.end_time.minute).zfill(2)
        eventTime = tk.Label(eventBoxCanvas, text = timeStr, font=('Helvetica', '8'),background='red')
        eventRoom = tk.Label(eventBoxCanvas, text = _event.room.name, font=('Helvetica', '10'),background='red')
        eventHandler = tk.Label(eventBoxCanvas, text = _event.participants[0], font=('Helvetica', '10'),background='red')
        #deleteBtn = tk.Button(eventBoxCanvas, text="delete")
        #modifyBtn = tk.Button(eventBoxCanvas, text="modify")
        eventBoxCanvas.grid(row=_index,column=0,padx=10,pady = 5)
        eventlabel.place(anchor='nw',x=0,y=0)
        eventTime.place(anchor='sw', x= 0 ,y=80)
        eventRoom.place(anchor='nw',x=80 ,y=20)
        eventHandler.place(anchor='se',x=280,y=80)
        #deleteBtn.place(anchor='nw',x=0,y=30)
        #modifyBtn.place(anchor='nw',x=50,y=30)
        self.eventList.append(eventBoxCanvas)
        pass