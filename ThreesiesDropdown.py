#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:37:10 2018
@author: acelentano
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
root = tkinter.Tk()
title = "RTB"
root.title(title)
export = "ThreesiesLog"

e1 = tkinter.StringVar(root)
e2 = tkinter.StringVar(root)
e3 = tkinter.StringVar(root)

#winning = ['Select Winner']
#e3.set(winning[0])
#def update(root):
#    option1 = e1.get()
#    option2 = e2.get()
#    winning.insert(1, option1)
#    winning.insert(2, option2)

choices = ['Select Player', 'Carts','Ali','MP','SunChow','PPJ', 'Fonz', 'Alex', 'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jodie', 'Chris']

e1.set(choices[0])
entry1 = OptionMenu(root, e1, *choices)
entry1.grid(row=1, column=0, sticky='e')
entry1.config(width=10)

e2.set(choices[0])
entry2 = OptionMenu(root, e2, *choices)
entry2.grid(row=1, column=2, sticky='e')   
entry2.config(width=10)

e3.set(choices[0])
entry3 = tkinter.OptionMenu(root, e3, *choices)
entry3.grid(row=3, column=1, sticky='nsew')
entry3.config(width=15)

#Submit Button
def SubmitEntry():
    submit = tkinter.messagebox.askquestion("Submit Entry", "Submit Game?")
    if submit == "yes":
        player1 = e1.get()
        player2 = e2.get()
        gamewinner = e3.get()
        currentrow = pd.DataFrame([[player1,player2,gamewinner,strftime("%m-%d-%Y %H:%M", gmtime())]],columns=['Left Side Player','Right Side Player','Winner','Time'])
        global champs
        champs = pd.concat([champs,currentrow],axis=0, ignore_index=True)
        champs.to_csv('ThreesiesLog.csv', index=False)  
        e1.set(choices[0])
        e2.set(choices[0])
        e3.set(choices[0])

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()

def QuitEntry():
    quitask = tkinter.messagebox.showinfo("Save","Your entries have been saved to " + export)
    if quitask == "yes":
            root.destroy() 

firstname = tkinter.Label(text="Left Side Player", fg="green")
secondname = tkinter.Label(text="Right Side Player", fg="green")
winner = tkinter.Label(text="WINNER", fg="blue")

Submit = tkinter.Button(root, fg="blue", bg="green", text="Submit Game", width=20, command=SubmitEntry, activebackground="yellow")
Quit = tkinter.Button(root, fg="blue", bg="green", text="End Tournament", width=20, command=QuitEntry,activebackground="yellow")

root.bind_all('<Key>', keypress)
firstname.grid(row=0, column=0,sticky='e')
secondname.grid(row=0, column=2, sticky='e')
winner.grid(row=2, column=1, sticky='nsew')
Submit.grid(row=5, column=1, sticky='nsew')
Quit.grid(row=6, column=1, sticky='nsew') 
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(4, minsize=20)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()