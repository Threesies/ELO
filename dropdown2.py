#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:17:27 2018

@author: acelentano
"""
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pandas as pd
import numpy as np
import os
from time import gmtime, strftime

root = tk.Tk()
text = tk.Text(root)
title = "RTB"
root.title(title)
export = "ThreesiesLog"



os.chdir('/Users/acelentano/pong/ELO')
champs = pd.read_csv('ThreesiesLog.csv')

current_rating = pd.read_csv('Threesies_Elo_Ratings')
current_rating.columns = ['Name', 'Rating']
current_rating.set_index('Name', inplace = True)
global dictionary
dictionary = current_rating.to_dict()

championships = pd.read_csv('Championships.csv')
championships.set_index('Names', inplace= True)
# =============================================================================
# Functions
# =============================================================================
def SubmitEntry():
    submit = tk.messagebox.askquestion("Submit Entry", "Submit Game?")
    if submit == "yes":
        player1 = e1.get()
        player2 = e2.get()
        gamewinner = e3.get()
        if e4.get() == 'Select Champion':
            global champs
            currentrow = pd.DataFrame([[player1,player2,gamewinner, strftime("%m-%d-%Y %H:%M", \
                    gmtime())]],columns=['Left Side Player','Right Side Player',\
                    'Winner','Time'])
            champs = pd.concat([champs,currentrow],axis=0, ignore_index=True, sort=True)
            champs.to_csv('ThreesiesLog.csv', index=False)   
        else: 
            add_championship(e4.get())
            championships.to_csv('Championships.csv')
            currentrow = pd.DataFrame([[player1,player2,gamewinner,strftime("%m-%d-%Y %H:%M", \
                        gmtime())]],columns=['Left Side Player','Right Side Player',\
                        'Winner','Time'])
            champs = pd.concat([champs,currentrow],axis=0, ignore_index=True, sort=True)
            champs.to_csv('ThreesiesLog.csv', index=False) 
        print_new(root)
        e1.set(choices[0])
        e2.set(choices[0])
        e3.set(choices[0])
        e4.set(champions[0])

def add_championship(y):
    num = championships.loc[y]
    newnum = num + 1
    championships.at[y] = newnum
    return championships

def QuitEntry():
    quittask = tk.messagebox.showinfo("End Tournament", "Submit Championship?")
    if quittask == "ok":
        root.destroy()

def loser(row):
    if row['Right Side Player'] == row['Winner']:
        return row['Left Side Player']
    else:
        return row['Right Side Player']

def expected_result(elo_a, elo_b):
    elo_width = 400
    expect_a = 1.0/(1+10**((elo_b - elo_a)/elo_width))
    return expect_a

def update_elo(winner_elo, loser_elo):
    k_factor = 64
    expected_win = expected_result(winner_elo, loser_elo)
    change_in_elo = k_factor * (1-expected_win)
    winner_elo += change_in_elo
    loser_elo -= change_in_elo
    return round(winner_elo, 2), round(loser_elo, 2)\

def player_matchup(player1, player2):
    global winner_matrix
    player2wins = winner_matrix[player1][player2]
    player1wins = winner_matrix[player2][player1]
    total = player1wins + player2wins
    player1_perc = round((player1wins/total)*100, 2)
    player2_perc = round((100 - player1_perc), 2)
    return player1_perc, player2_perc
    #print('Percentage wins for ' + str(player1) + ': ' + str(player1_perc)+'%')
    #print('Percentage wins for ' + str(player2) + ': ' + str(player2_perc)+'%')

def win_perc():
    for player in championships.index:
        wins = champs.Winner.value_counts()[player]
        loss = champs.Loser.value_counts()[player]
        percentage = (wins/(wins+loss))*100
        championships.at[player, "Win Percentage"] =  percentage
        championships.to_csv('Championships.csv')
    return championships

def update_text(root):
    printout = ''
    printout2=''
    matchup = ''
    if e1.get() != "Select Player":
        printout += (e1.get() + " " + str( (Ratings['Rating'][e1.get()])))
    if e2.get() != "Select Player":
        printout2 += (e2.get() + " " + str( (Ratings['Rating'][e2.get()])))
        matchup += str((player_matchup(e1.get(), e2.get())))
    text.delete('1.0', 'end')
    text.insert('1.0', printout + '\n')
    text.insert('1.0', printout2 + '\n')
    text.insert('1.0', matchup + '\n')
    text.tag_configure("center", justify='center')
    text.tag_add("center", 1.0, "end")
    
def print_new(root):
    champs['Loser'] = champs.apply(loser,axis=1)
    Winner = list(champs['Winner'])
    Loser = list(champs['Loser'])
    update_win =[]
    update_loss = []
    for i in range(len(Winner)):
        Win = Winner[i]
        Lose = Loser[i]
        updated_score = update_elo(dictionary['Rating'][Win], dictionary['Rating'][Lose])
        dictionary['Rating'][Win], dictionary['Rating'][Lose] = updated_score
        update_win.append(updated_score[0])
        update_loss.append(updated_score[1])
    Ratings = pd.DataFrame.from_dict(dictionary)
    new = ''
    if e3.get() != "Select Player":
        new += (e3.get() + " new rating: " + str( (Ratings['Rating'][e3.get()])))
    text.insert('1.0', new + '\n')
    
# =============================================================================
# Rating Preprocessing
# =============================================================================
#Add Loser
champs['Loser'] = champs.apply(loser,axis=1)
#Create list of Winners and Losers
Winner = list(champs['Winner'])
Loser = list(champs['Loser'])

#Blank List to fill DataFrame later
update_win =[]
update_loss = []

# =============================================================================
# Create new ELO Rating
# =============================================================================
for i in range(len(Winner)):
    Win = Winner[i]
    Lose = Loser[i]
    updated_score = update_elo(dictionary['Rating'][Win], dictionary['Rating'][Lose])
    dictionary['Rating'][Win], dictionary['Rating'][Lose] = updated_score
    update_win.append(updated_score[0])
    update_loss.append(updated_score[1])

# =============================================================================
# Add to DataFrame
# =============================================================================
champs['Winner ELO Update'] = update_win
champs['Loser ELO Update'] = update_loss     
    
# =============================================================================
# Player matchup percentages
# =============================================================================
#average number of wins on left side of table
#np.where(champs['Winner'] == champs['Left Side Player'],1,0).mean()
win_perc()
winner_matrix = pd.crosstab(champs['Winner'],champs['Loser'])

Ratings = pd.DataFrame.from_dict(dictionary)


# =============================================================================
# Create menus 
# =============================================================================
e1 = tk.StringVar(root)
e2 = tk.StringVar(root)
e3 = tk.StringVar(root)
e4 = tk.StringVar(root)

choices = ['Select Player', 'Carts','Ali','MP','SunChow','PPJ', 'Fonz', 'Alex', \
           'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jodie', 'Chris', 'RonRon', 'Peter', 'SeaBass', 'juju']
champions = ['Select Champion', 'Carts','Ali','MP','SunChow','PPJ', 'Fonz', 'Alex', \
             'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jodie', 'Chris', 'RonRon', 'Peter', 'SeaBass', 'juju']

e1.set(choices[0])
entry1 = tk.OptionMenu(root, e1, *choices, command = update_text)
entry1.grid(row=1, column=0, sticky='e')
entry1.config(width=10)

e2.set(choices[0])
entry2 = tk.OptionMenu(root, e2, *choices, command = update_text)
entry2.grid(row=1, column=2, sticky='e')   
entry2.config(width=10)

e3.set(choices[0])
entry3 = tk.OptionMenu(root, e3, *choices)
entry3.grid(row=3, column=1, sticky='nsew')
entry3.config(width=10)

e4.set(champions[0])
entry4 = tk.OptionMenu(root, e4, *champions)
entry4.grid(row=4, column=1, sticky='nsew')
entry4.config(width=10)


submit = tk.Button(root, fg="blue", bg="green", text = "Submit Game", width = 20, command = SubmitEntry, activebackground="yellow")
submit.config(width=20)
Quit = tk.Button(root, fg="blue", bg="green", text="End Tournament", width=20, command=QuitEntry, activebackground="yellow")
Quit.config(width=20)
# =============================================================================
# Dropdown Button formatting
# =============================================================================

firstname = tk.Label(text="Left Side Player", fg="green")
secondname = tk.Label(text="Right Side Player", fg="green")
winner = tk.Label(text="WINNER", fg="blue")
Champion = tk.Label(text="Champion!", fg="blue")

firstname.grid(row=0, column=0,sticky='e')
secondname.grid(row=0, column=2, sticky='e')
winner.grid(row=2, column=1, sticky='nsew')
submit.grid(row=5, column=1, sticky='nsew')
Quit.grid(row=7, column=1, sticky='nsew') 
root.grid_rowconfigure(4, minsize=20)
root.grid_columnconfigure(1, minsize = 10)

text.tag_configure("center", justify='center')
text.tag_add("center", 1.0, "end")
text.grid(row = 8, column = 1, sticky = 'nsew')

root.mainloop()

# =============================================================================
# Delete crap
# =============================================================================
del i, update_loss, update_win, updated_score, Winner, Lose, current_rating, Win 
del E, N, S, TclVersion, TkVersion, W, X, Y, export, title, wantobjects
del winner_matrix, dictionary, choices, Loser, champions