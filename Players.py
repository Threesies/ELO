#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:11:21 2018

@author: acelentano
"""

import xlrd
workbook = xlrd.open_workbook('brackets.xlsx')
#message box to ask for number of players
#select players playing

def available_players():
    

def open_brackets():
    if #messagebox.input == 4
        sheet = workbook.sheet_by_name('4')
    elif #messagebox.input == 5
        sheet = workbook.sheet_by_name('5')
    elif #messagebox.input == 6
        sheet = workbook.sheet_by_name('6')
    elif #messagebox.input == 7
        sheet = workbook.sheet_by_name('7')
    elif #messagebox.input == 8
        sheet = workbook.sheet_by_name('8')
    elif #messagebox.input == 9
        sheet = workbook.sheet_by_name('9')
    elif #messagebox.input == 10
        sheet = workbook.sheet_by_name('10')


workbook = xlrd.open_workbook('ELO.xlsx')
sheet = workbook.sheet_by_name('Player Ratings')

For  
A_rating = sheet.cell(1, 1).value
B_rating = sheet.cell(1, 2).value
C_rating = sheet.cell(1, 3).value
D_rating = sheet.cell(1, 4).value
E_rating = sheet.cell(1, 5).value
F_rating = sheet.cell(1, 6).value
G_rating = sheet.cell(1, 7).value
H_rating = sheet.cell(1, 8).value
I_rating = sheet.cell(1, 9).value
J_rating = sheet.cell(1, 10).value
K_rating = sheet.cell(1, 11).value

ratings = [A_rating, B_rating, C_rating, D_rating, E_rating, F_rating, G_rating, H_rating, I_rating, J_rating, K_rating]
sorted(ratings, reverse=False)














def expected_outcome(player1, player2):

    return 1 / (1 + 10 ** ((B_rating - A_rating) / 400))
# add in factor of side of table players are on

win = 1.0
loss= 0.0
k = 32

#message box to ask who won
def new_rating(old, exp, score, k=32):
    """
    Calculate the new Elo rating for a player

    :param old: The previous Elo rating
    :param exp: The expected score for this match
    :param score: The actual score for this match
    :param k: The k-factor for Elo (default: 32)
    """
    old = A_rating
    return old + k * (score - expected_outcome)



def update_rating(winner, loser):
    winner_old_rating = winner.rating
    loser_old_rating = loser.rating
    s = 1 # "score"
    adjustment =  k * (s - expected_outcome(winner_old_rating, loser_old_rating))
    winner.rating += adjustment
    loser.rating -= adjustment


#writing new rating
# sheet.write(0, 0,'Inserting data in 1st Row and 1st Column')


class player(object):
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def getName(self):
        return self.name

    def getRating(self):
        return self.rating

    def __str__(self):
        return "%s has a rating of %s" % (self.name, self.rating)