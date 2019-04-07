# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:06:50 2019

@author: Abhishek
"""
import csv
import pickle
import tkinter as tk
from tkinter import Scrollbar
from tkinter import messagebox


def add(event):
    sym = Entry1.get()
    if(len(sym)!=0):
        if sym in Symtoms:
            if sym not in Listbox1.get(0,'end'): 
                Listbox1.insert(tk.END, sym)
        else:
            messagebox.showerror("DOC-BOT Error","Please Select Symtoms from given List")
        Entry1.delete(0,'end')
    else:
        messagebox.showerror("DOC-BOT Error","Please Enter Symtoms")

def clear():
    Listbox1.delete(0,'end')


def insert(event):
    sym = event.widget
    Entry1.delete(0,'end')
    Listbox1.insert(tk.END, sym.get(sym.curselection()))
    
def onselect(event):
    try:
        box = event.widget
        Entry1.delete(0,'end')
        Entry1.insert(0,box.get(box.curselection()))
    except:
        pass
    
    box.bind("<Return>", insert)
    
def predict():
    patient_sym = Listbox1.get(0,'end')
    if(len(patient_sym) != 0):
        sym_vect = [0]*398
        for sym in patient_sym:
            if sym in Symtoms:
                sym_vect[Symtoms.index(sym)]=1
    
        sym_vect = [sym_vect]
        index = int(DOC_model.predict(sym_vect))
        
        messagebox.showinfo("Disease Prediction",Disease[index]+"\n"+doc[index][0]+"-"+ doc[index][1])
    else:
       messagebox.showerror("DOC-BOT Error","Please Enter Symtoms for Disease prediction")

def mainPanel():
    global top
    top = tk.Tk()
    top.geometry("812x620+151+41")
    top.title("DOC-BOT")
    top.configure(background = 'floral white')

    Frame1 = tk.Frame(top)
    Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(background="#99d8d6")
                     
    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.209, rely=0.032, height=51, width=194)
    Label1.configure(font="-family {Microsoft Tai Le} -size 18 -weight bold -underline 1")
    Label1.configure(background="#99d8d6")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''DOC-BOT''')
    Label1.configure(width=194)
    
    Labelframe1 = tk.LabelFrame(Frame1)
    Labelframe1.place(relx=0.616, rely=0.016, relheight=0.976, relwidth=0.382)
    Labelframe1.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Labelframe1.configure(relief='groove')
    Labelframe1.configure(foreground="black")
    Labelframe1.configure(text='''All Symtoms''')
    Labelframe1.configure(background="#d9d9d9")
    Labelframe1.configure(width=250)

    global Listbox2
    Listbox2 = tk.Listbox(Labelframe1)
    Listbox2.place(relx=0.016, rely=0.033, relheight=0.945, relwidth=0.948, bordermode='ignore') 
    Listbox2.configure(background="#c7f9ff")
    Listbox2.configure(disabledforeground="#a3a3a3")
    Listbox2.configure(font="TkFixedFont")
    Listbox2.configure(foreground="#000000")
    Listbox2.configure(width=234)
    
    Listbox2.bind('<<ListboxSelect>>', onselect)
    
    scrollbar = Scrollbar(Labelframe1, orient="vertical")
    scrollbar.config(command=Listbox2.yview)
    scrollbar.pack(side="right", fill="y")

    Listbox2.config(yscrollcommand=scrollbar.set)
 
    for sym in Symtoms:
        Listbox2.insert(tk.END, sym)
 
    Label2 = tk.Label(Frame1)
    Label2.place(relx=0.123, rely=0.194, height=21, width=104)
    Label2.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Label2.configure(background="#99d8d6")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Enter Symtoms''')
    Label2.configure(width=94)

    entry_var = tk.StringVar()
    
    global Entry1
    Entry1 = tk.Entry(Frame1)
    Entry1.place(relx=0.259, rely=0.194,height=20, relwidth=0.239)
    Entry1.configure(background="#d6e2ff",textvariable = entry_var)
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    global Listbox1
    Listbox1 = tk.Listbox(Frame1)
    Listbox1.place(relx=0.123, rely=0.29, relheight=0.374, relwidth=0.374)
    Listbox1.configure(background="#c7f9ff")
    Listbox1.configure(disabledforeground="#a3a3a3")
    Listbox1.configure(font="-family {Microsoft Tai Le} -size 10")
    Listbox1.configure(foreground="#000000")
    Listbox1.configure(width=164)

    scrollbar = Scrollbar(Listbox1, orient="vertical")
    scrollbar.config(command=Listbox1.yview)
    scrollbar.pack(side="right", fill="y")

    Listbox1.config(yscrollcommand=scrollbar.set)
    
    Entry1.bind("<Return>", add)

    Button2 = tk.Button(Frame1)
    Button2.place(relx=0.148, rely=0.726, height=30, width=97)
    Button2.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Button2.configure(activebackground="#ececec" , command = predict)
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#7fd89d")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Predict Disease''')
    Button2.configure(width=97)
 
    Button3 = tk.Button(Frame1)
    Button3.place(relx=0.369, rely=0.726, height=30, width=69)
    Button3.configure(font="-family {Microsoft Tai Le} -size 10 -weight bold")
    Button3.configure(activebackground="#ececec", command = clear)
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#7fd89d")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''Clear List''')
    Button3.configure(width=69)
    
    top.mainloop()


if __name__ == "__main__":
    filename = 'DOC-BOT_model.sav'
    
    data = dict()
    with open('Dataset.csv','r') as file:
        reader = csv.reader(file)
        for disease,symtoms in reader:
            if disease in data:
                data[disease].append(symtoms)
            else:
                data[disease] = [symtoms]
    global Disease
    Disease = list(data.keys())
     
    global Symtoms    
    Symtoms = set()
    for x in data.values():
        for y in x:
            Symtoms.add(y)
    
    Symtoms = sorted(Symtoms)   

    global doc
    doc = list()
    with open('Doctor.csv','r') as file:
        reader = csv.reader(file)
        for x in reader:
            doc.append(x)
            
    global DOC_model
    DOC_model = pickle.load(open(filename, 'rb'))
 
    mainPanel()