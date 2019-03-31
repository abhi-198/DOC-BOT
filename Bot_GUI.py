# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:06:50 2019

@author: Abhishek
"""

from tkinter import *

def mainPanel():
    panel = Tk()
    panel.geometry("744x680+323+4")
    panel.configure(background = "#75a6d8")
    panel.title("DOC-BOT")
    mainLable = Label(panel, text = "DOC-BOT", background = "#a2d8c6", width = 185).place(relx=0.376, rely=0.044, height=51, width=184)
    
    centerFrame = LabelFrame(panel, text = "CHAT")
    centerFrame.place(relx=0.067, rely=0.162, relheight=0.515, relwidth=0.86)
    centerFrame.configure(relief = 'groove')
    centerFrame.configure(foreground = 'black')
    centerFrame.configure(background = "#6cbbd8")
    centerFrame.configure(width = 640)
    
    message = Entry(panel,background="#d8c2d8",font = 'TkFixedFont',width = 524).place(relx=0.228, rely=0.735,height=70, relwidth=0.704)
    
    Label(panel,text = "Message", background = "#d8c2d8",width = 95).place(relx=0.081, rely=0.735, height=31, width=94)
    
    Button(panel, text = "Exit").place(relx=0.524, rely=0.897, height=24, width=87)
    Button(panel, text = "Reset" ).place(relx=0.766, rely=0.897, height=24, width=77)
    panel.mainloop()
    
mainPanel()