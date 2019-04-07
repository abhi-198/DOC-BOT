# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:56:15 2019

@author: Abhishek
"""

import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import Scrollbar

def enter(event):
    try:
        entry = event.widget
        symptom = entry.get()
        if(len(symptom)!=0):
            Listbox1.insert(tk.END,symptom)
        else:
            messagebox.showerror("Entry Error","Please Enter Symtoms")
        entry.delete(0,'end')
    except:
        messagebox.showerror("Entry Error","Please fill All feilds")
        
def save(disease, name, room):
    try:
        if(disease in Disease):
            messagebox.showerror("Entry Error","Disease already exist in Database.")
            return
    except:
        messagebox.showerror("Entry Error","Please fill the all feild")
        return
    
    patient_sym = Listbox1.get(0,'end')
        
    with open('Dataset.csv', 'a') as csvFile:
        for x in patient_sym:
            csvFile.write(disease+","+x+"\n")

    csvFile.close()
    
    with open('Doctor.csv','a') as csvFile:
        csvFile.write(name+","+room+"\n")
        
    csvFile.close()
    messagebox.showinfo("Entry Message","Disease Saved Successfully")
    Listbox1.delete(0,'end')

def clear(top):
    top.destroy()
    NewDiseaseEntry()
    
def NewDiseaseEntry():
    top = tk.Tk()
    top.geometry("515x620+104+57")
    top.title("New Disease Entry")
    top.configure(background="#68abd8")
    
    Frame1 = tk.Frame(top)
    Frame1.place(relx=0.058, rely=0.032, relheight=0.944 , relwidth=0.883)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#97d8d2")
    Frame1.configure(width=455)

    Labelframe1 = tk.LabelFrame(Frame1)
    Labelframe1.place(relx=0.088, rely=0.256, relheight=0.368, relwidth=0.813)
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''Symptoms''')
    Labelframe1.configure(background="#a8d8d0")
    Labelframe1.configure(width=370)
    
    global Listbox1
    Listbox1 = tk.Listbox(Labelframe1)
    Listbox1.place(relx=0.027, rely=0.093, relheight=0.847 , relwidth=0.93, bordermode='ignore')
    Listbox1.configure(background="white")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="TkFixedFont")
    Listbox1.configure(foreground="#000000")
    Listbox1.configure(width=344)
    
    scrollbar = Scrollbar(Labelframe1, orient="vertical")
    scrollbar.config(command=Listbox1.yview)
    scrollbar.pack(side="right", fill="y")

    Listbox1.config(yscrollcommand=scrollbar.set)
    
    Entry1 = tk.Entry(Frame1)
    Entry1.place(relx=0.352, rely=0.171,height=20, relwidth=0.514)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")
    Entry1.configure(width=234)
    
    Entry1.bind("<Return>",enter)
 
    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.33, rely=0.051, height=31, width=164)
    Label1.configure(background="#a8d8d0")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Microsoft Tai Le} -size 13 -weight bold -underline 1")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''New Disease Entry''')
    Label1.configure(width=164)
 

    Entry2 = tk.Entry(Frame1)
    Entry2.place(relx=0.374, rely=0.684,height=20, relwidth=0.514)
    Entry2.configure(background="white", )
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="TkFixedFont")
    Entry2.configure(foreground="#000000")
    Entry2.configure(insertbackground="black")
    Entry2.configure(width=234)
 
 
    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.11, rely=0.171, height=21, width=74)
    Label2.configure(background="#a8d8d0")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Microsoft YaHei} -size 9 -weight bold")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Symptom''')
    Label2.configure(width=74)
 
    Label3 = tk.Label(Frame1)
    Label3.place(relx=0.132, rely=0.684, height=21, width=64)
    Label3.configure(background="#a8d8d0")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Disease''')
    Label3.configure(width=64)
 
    Label4 = tk.Label(Frame1)
    Label4.place(relx=0.132, rely=0.752, height=21, width=84)
    Label4.configure(background="#a8d8d0")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Doctor's Name''')
    Label4.configure(width=84)
    

    Entry3 = tk.Entry(Frame1)
    Entry3.place(relx=0.396, rely=0.752,height=20, relwidth=0.492)
    Entry3.configure(background="white")
    Entry3.configure(disabledforeground="#a3a3a3")
    Entry3.configure(font="TkFixedFont")
    Entry3.configure(foreground="#000000")
    Entry3.configure(insertbackground="black")
    Entry3.configure(width=234)
    

    Entry4 = tk.Entry(Frame1)
    Entry4.place(relx=0.396, rely=0.821,height=20, relwidth=0.492)
    Entry4.configure(background="white")
    Entry4.configure(disabledforeground="#a3a3a3")
    Entry4.configure(font="TkFixedFont")
    Entry4.configure(foreground="#000000")
    Entry4.configure(insertbackground="black")
    Entry4.configure(width=234)
 
    Label5 = tk.Label(Frame1)
    Label5.place(relx=0.066, rely=0.803, height=41, width=124)
    Label5.configure(background="#a8d8d0")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''Doctor's Room no.''')
    Label5.configure(width=124)

    Button1 = tk.Button(Frame1)
    Button1.place(relx=0.681, rely=0.906, height=24, width=87)
    Button1.configure(activebackground="#98cbed")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#bec3d8")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Save Disease''')
    Button1.configure(width=87)
    Button1.configure(command= lambda: save(Entry2.get(),Entry3.get(),Entry4.get()))

    Button2 = tk.Button(Frame1)
    Button2.place(relx=0.481, rely=0.906, height=24, width=87)
    Button2.configure(activebackground="#98cbed")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#bec3d8")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Clear''')
    Button2.configure(width=87, command = lambda:clear(top))
    
    top.mainloop()


if __name__== "__main__":

    global Disease
    Disease = list()
    
    with open('Dataset.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for disease,symtoms in reader:
            Disease.append(disease)
    
    
    NewDiseaseEntry()
    