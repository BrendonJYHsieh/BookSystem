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

class LoginInterface(BaseInterface.BaseInterface):
    def __init__(self,_parent,_booksystem):
        self.BookSystem = _booksystem
        self.mainCanvas = tk.Canvas(_parent,height=600,width=800,bd=0, highlightthickness = 0,background="white")

        self.account = tk.Label(self.mainCanvas,text="Account：", font=('Helvetica', '15'),background="#dcdcdc")
        self.account.place(x=0,y=20)
        self.accountStr = tk.StringVar()
        self.account = tk.Entry(self.mainCanvas,textvariable=self.accountStr)
        self.account.place(x=120,y=28,width=200)

        self.password = tk.Label(self.mainCanvas,text="Account：", font=('Helvetica', '15'),background="#dcdcdc")
        self.password.place(x=0,y=70)
        self.passwordStr = tk.StringVar()
        self.password = tk.Entry(self.mainCanvas,textvariable=self.passwordStr)
        self.password.place(x=120,y=78,width=200)

        self.loginBtn = tk.Button(self.mainCanvas,text="Login",command=self.LogInAccount)
        self.loginBtn.place(x=0,y=120)
        self.signBtn = tk.Button(self.mainCanvas,text="Sign",command=self.SignAccount)
        self.signBtn.place(x=100,y=120)

        self.remindText = tk.Label(self.mainCanvas,text="測試版登入介面，功能未實作，點<<Login>>直接進入。",font=('Helvetica', '15'),fg="red").place(x=0,y=170)
        self.SetActive(0)
    def Enable(self):
        self.mainCanvas.place(x=0,y=0)
        pass
    def Disable(self):
        self.mainCanvas.place_forget()
        pass

    def LogInAccount(self):
        self.BookSystem.auth.login(self.accountStr.get(),self.passwordStr.get())
        self.SetActive(not self.BookSystem.auth.valid)
        pass
    def SignAccount(self):
        self.BookSystem.auth.register(self.accountStr.get(),self.passwordStr.get())
        pass