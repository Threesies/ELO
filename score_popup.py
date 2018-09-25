#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:00:04 2018

@author: acelentano
"""

#lists player names from excel file
import openpyxl
wb = openpyxl.load_workbook('ELO.xlsx')
sheet = wb['Player Ratings'] 

def get_players():
    for row in range(2, sheet.max_row + 1):
        player  = sheet['A' + str(row)].value
        print (player)
