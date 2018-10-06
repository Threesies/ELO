# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:49:30 2018
@author: 582957
"""


import pandas as pd
import ThreesiesDropdown

champs = pd.read_csv('ThreesiesLog.csv')
current_rating = pd.read_csv('Threesies_Elo_Ratings')
current_rating.columns = ['Name', 'Rating']
current_rating.set_index('Name', inplace = True)
dictionary = current_rating.to_dict()

championships = pd.read_csv('Championships.csv')
championships.set_index('Names', inplace= True)

# =============================================================================
# Functions
# =============================================================================

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

def add_championship(y):
    num = championships.loc[y]
    newnum = num + 1
    championships.at[y] = newnum
    return championships

# =============================================================================
# Preprocessing
# =============================================================================
#Add Loser
champs['Loser'] = champs.apply(loser,axis=1)
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
    i = 0
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
# Delete crap
# =============================================================================
del update_win, update_loss, Winner, Loser, i, Lose, Win, current_rating, updated_score

# =============================================================================
# Add to championship total
# =============================================================================
championships.to_csv('Championships.csv')
championships.sort_values('Number', ascending = False)
