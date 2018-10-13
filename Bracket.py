#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:43:29 2018

@author: acelentano
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.choices = ['Carts','Ali','MP','SunChow','PPJ', 'Fonz', 'Alex', \
           'D$', 'M1', 'M2', 'Spidey', 'MH', 'Jodie', 'Chris', 'RonRon', 'Peter']
        
        #list of checkbuttons
        self.boxes = []
        #binary for whether box is checked 
        self.box_vars = []
        #count to loop through checkboxes
        self.box_num = 0

        btn_test1 = tk.Button(self, text="Select Players", width = 11, command = self.test1)
        btn_test1.grid()

    def test1(self):
        for name in self.choices:
            self.box_vars.append(tk.IntVar())
            self.boxes.append(tk.Checkbutton(self, text = name, variable = self.box_vars[self.box_num]))
            self.box_vars[self.box_num].set(0)
            self.boxes[self.box_num].grid(sticky = tk.W)
            self.box_num += 1
        
        submit = tk.Button(self, text = "Submit", width = 11, command = self.get)
        submit.grid()
        
    def get(self):
        for i in self.boxes:
            if tk.Checkbutton.cget(self) == 1:
                print(i)
            #self.boxes.append(tk.Checkbutton(self, text = name, variable = self.box_vars[self.box_num]))
            #self.box_vars[self.box_num].set(0)
            #self.boxes[self.box_num].grid(sticky = tk.W)
            #self.box_num += 1
        #for i in self.boxes:
         #   print(self.box_vars[self.box_num].get())
        root.destroy()
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()