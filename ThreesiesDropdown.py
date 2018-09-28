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
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
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
    submit = tkinter.messagebox.askquestion("Submit Entry", "Submit Game?")
    if submit == "yes":
        player1 = e1.get()
        player2 = e2.get()
        winner = e3.get()
        currentrow = pd.DataFrame([[player1,player2,winner,strftime("%m-%d-%Y %H:%M", gmtime())]],columns=['Left Side Player','Right Side Player','Winner','Time'])
        global champs
        champs = pd.concat([champs,currentrow],axis=0, ignore_index=True)
        e1.set(choices[0])
        e2.set(choices[0])
        e3.set(choices[0])

def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()

def QuitEntry():
    quitask = tkinter.messagebox.askquestion("Quit", "Are you sure the fun is over?")
    if quitask == "yes":
            root.destroy()
            champs.to_csv('ThreesiesLog.csv', index=False)  
            userconfirm = tkinter.messagebox.showinfo("Save","Your entry has been saved to a " + export + " document!")

firstname = tkinter.Label(text="Left Side Player", fg="green")
secondname = tkinter.Label(text="Right Side Player", fg="green")
winner = tkinter.Label(text="WINNER", fg="blue")

Submit = tkinter.Button(root, fg="blue", bg="green", text="Submit Game", width=30, command=SubmitEntry, activebackground="yellow")
Quit = tkinter.Button(root, fg="blue", bg="green", text="Submit Tournament", width=30, command=QuitEntry,activebackground="yellow")

root.bind_all('<Key>', keypress)
firstname.grid(row=0, column=0,sticky='e')
entry1.grid(row=1, column=0, sticky='e')
secondname.grid(row=0, column=1, sticky='e')
entry2.grid(row=1, column=1, sticky='e')
winner.grid(row=2, column=1, sticky='nsew')
entry3.grid(row=3, column=1, sticky='nsew')
Submit.grid(row=5, column=1, sticky='nsew')
Quit.grid(row=6, column=1, sticky='nsew') 

root.grid_rowconfigure(4, minsize=20)

root.mainloop()