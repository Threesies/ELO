#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:30:24 2018

@author: acelentano
"""

import pandas as pd
import ELORating
import tkinter
import os
import tkinter.messagebox
from time import gmtime, strftime
from tkinter import OptionMenu

champs = pd.read_csv('ThreesiesLog.csv')
current_rating = pd.read_csv('Threesies_Elo_Ratings')
current_rating.columns = ['Name', 'Rating']
current_rating.set_index('Name', inplace = True)
dictionary = current_rating.to_dict()

os.chdir('/users/acelentano/pong/')
champs = pd.read_csv('ThreesiesLog.csv')
root = tkinter.Tk()
title = "RTB"
root.title(title)
export = "ThreesiesLog"

e1 = tkinter.StringVar(root)
e2 = tkinter.StringVar(root)
e3 = tkinter.StringVar(root)

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
        if player1 == gamewinner:
            loser = player2
        else:
            loser = player1
        currentrow = pd.DataFrame([[player1,player2,gamewinner,loser,strftime("%m-%d-%Y %H:%M", gmtime())]],columns=['Left Side Player','Right Side Player','Winner', 'Loser','Time'])
        global champs
        champs = pd.concat([champs,currentrow],axis=0, ignore_index=True)
        champs.to_csv('ThreesiesLog.csv', index=False)  
        
        run(ELORating.py)
        

# =============================================================================

def expected_result(elo_a, elo_b):


def update_elo(winner_elo, loser_elo):


# =============================================================================
# Preprocessing
# =============================================================================
#Create list of Winners and Losers
Winner = list(champs['Winner'])
Loser = list(champs['Loser'])

#Blank List to fill DataFrame later (line 68 and 69)
update_win =[]
update_loss = []

# =============================================================================
# Create new ELO Rating
# =============================================================================
for i in range(len(Winner)):
    Win = Winner[i]
    Lose = Loser[i]
    updated_score = update_elo(dictionary['Rating'][Win], dictionary['Rating'][Lose])
    #dictionary['Rating'][Win], dictionary['Rating'][Lose] = updated_score
    update_win.append(updated_score[0])
    update_loss.append(updated_score[1])

# =============================================================================
# Add to DataFrame
# =============================================================================
champs['Winner ELO Update'] = update_win
champs['Loser ELO Update'] = update_loss

# =============================================================================
# Delete crap
# =============================================================================
del update_win, update_loss, Winner, Loser, i, Lose, Win, current_rating, updated_score






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
