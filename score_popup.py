#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:00:04 2018

@author: acelentano
"""
    
import tkinter as tk
from tk import messagebox


root= tk.Tk() # create window

canvas1 = tk.Canvas(root, width = 800, height = 350)
canvas1.pack()


def score():
    MsgBox = tk.messagebox.askquestion ('Outcome','Did player1 win?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
       #link to outcome rating changes
    else:
        tk.messagebox.showinfo('Return','Suck it loser')
        
      
button1 = tk.Button (root, text='score',command=score)
canvas1.create_window(97, 270, window=button1)
  
  
root.mainloop()

from tkinter.commondialog import Dialog


def askyesno(title=None, message=None, **options):
    "Ask a question; return true if the answer is yes"
    s = _show(title, message, QUESTION, YESNO, **options)
    return s == YES