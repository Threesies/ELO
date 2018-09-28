#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:37:10 2018

@author: cburns
"""
#from https://stackoverflow.com/questions/35330224/python-tkinter-xlsxwriter-trying-to-export-user-input-to-excel-file?rq=1
import tkinter
import os
import tkinter.messagebox
from time import gmtime, strftime
from tkinter import OptionMenu
import pandas as pd

os.chdir('/users/acelentano/pong/')
champs = pd.read_csv('ThreesiesLog.csv')

choices = ['Select Player', 'Carts','AC','MP','Sun Chow','PPJ', 'Fonz', 'Alex', 'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jods']


root = tkinter.Tk()
e1 = tkinter.StringVar(root)
e2 = tkinter.StringVar(root)
e3 = tkinter.StringVar(root)

e1.set(choices[0])
e2.set(choices[0])
e3.set(choices[0])

title = "RTB"
root.title(title)
#root.geometry("600x600")

entry1 = OptionMenu(root, e1, *choices)
entry2 = OptionMenu(root, e2, *choices)
entry3 = OptionMenu(root, e3, *choices)

export = "CSV"

#Submit Button
def SubmitEntry():
    submit = tkinter.messagebox.askquestion("Submit Entry", "Are you sure you want to submit?")
    if submit == "yes":
        player1 = e1.get()
        player2 = e2.get()
        winner = e3.get()
        currentrow = pd.DataFrame([[player1,player2,winner,strftime("%m-%d-%Y %H:%M", gmtime())]],columns=['Left Side Player','Right Side Player','Winner','Time'])
        global champs
        champs = pd.concat([champs,currentrow],axis=0, ignore_index=True)
        userconfirm = tkinter.messagebox.showinfo("Save","Your entry has been saved to a " + export + " document!")
        e1.set(choices[0])
        e2.set(choices[0])
        e3.set(choices[0])

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()

def QuitEntry():
    quitask = tkinter.messagebox.askquestion("Quit", "Are you sure you want to quit?")
    if quitask == "yes":
            root.destroy()
            champs.to_csv('ThreesiesLog.csv', index=False)  

firstname = tkinter.Label(root, text="Left Side Player", fg="green")
secondname = tkinter.Label(root, text="Right Side Player", fg="green")
winner = tkinter.Label(root, text="WINNER", fg="blue")


TextArea = tkinter.Text()
ScrollBar = tkinter.Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side='right', fill='y')

Submit = tkinter.Button(root, fg="blue", bg="green", text="Submit", width=50, command=SubmitEntry, activebackground="yellow")
Quit = tkinter.Button(root, fg="blue", bg="green", text="Quit", width=50, command=QuitEntry,activebackground="yellow")

root.bind_all('<Key>', keypress)
firstname.pack()
entry1.pack()
secondname.pack()
entry2.pack()
winner.pack()
entry3.pack()
TextArea.pack(expand='YES', fill='both')
Submit.pack()
Quit.pack() 

root.mainloop()