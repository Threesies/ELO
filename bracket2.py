#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:17:27 2018

@author: acelentano
"""

import tkinter as tk


def update_text():
    global cbs
    global _string
    global string
    string = []
    _string = ''
    for name, checkbutton in cbs.items():
        if checkbutton.var.get():
            string.append(checkbutton['text'])
            _string += checkbutton['text'] + '\n'
    text.delete('1.0', 'end')
    text.insert('1.0', _string)

def get():
    print(string) 
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    text = tk.Text("Player Selection")

    cb_list =['Carts','Ali','MP','SunChow','PPJ', 'Fonz', 'Alex', \
           'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jodie', 'Chris', 'RonRon', 'Peter']
    cbs = dict()
    for i, value in enumerate(cb_list):
        cbs[value] = tk.Checkbutton(root, text=value, onvalue=True,
                                offvalue=False, command=update_text)
        cbs[value].var = tk.BooleanVar(root, value=False)
        cbs[value]['variable'] = cbs[value].var

        cbs[value].grid(row=i, column=0, sticky = 'W')

submit = tk.Button(root, text = "Submit", width = 11, command = get, sticky = 'W')
submit.grid()

player_count = (len(string))

text.grid()
root.mainloop()