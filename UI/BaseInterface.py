from os import stat
import tkinter.font as fnt
import tkinter as tk
import tkinter.ttk as ttk
import datetime
from tkinter.constants import ANCHOR, BOTH, CENTER, COMMAND, END, FALSE, FLAT, LEFT, N, NW, RIGHT, SUNKEN, TOP, VERTICAL, Y
from typing import Text

class BaseInterface():
    def __init__(self,_parent):
        self.mainCanvas = tk.Canvas(_parent,height=550,width=550,bd=0, highlightthickness = 0,background="#dcdcdc")
    def SetActive(self,_value):
        if _value == True :
            self.Enable()
        else :
            self.Disable()
    def Enable():
        pass
    def Disable():
        pass