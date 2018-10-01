# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:49:30 2018

@author: 582957
"""

import pandas as pd
import ThreesiesDropdown
from ThreesiesDropdown import gamewinner, loser, e1, e2
ratings = pd.read_csv('Ratings.csv')

a = e1.get()
b = e2.get()

def FindCurrentRating(player):
    for row in ratings:
        match=(row['Name'])
        if player == match:
            player_rating = row['Rating']
        return player_rating

elo_a = FindCurrentRating(a)
elo_b = FindCurrentRating(b)

if a == gamewinner:
    winner_elo = elo_a
else: 
    winner_elo = elo_b
    
if a == loser:
    loser_elo = elo_a
else:
    loser_elo = elo_b
    
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
    return round(winner_elo, 2), round(loser_elo, 2)

updated_rating = update_elo(winner_elo, loser_elo)
print(a)
print(b)

print(winner_elo)
print(loser_elo)

#def UpdateCSV(): 
#    for i in players:
#        i = name
#        currentrow = pd.DataFrame([[name, ratings]],columns=['Name','Rating'])
#        Ratings = pd.concat([ratings,currentrow],axis=0, ignore_index=True)
#        Ratings.to_csv('Ratings.csv', index=False) 