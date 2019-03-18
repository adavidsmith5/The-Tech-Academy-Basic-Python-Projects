#Python Version: 3.7.2
#
#Author: Tony Smith
#
#Purpose: Learn how to use Tkinter, Python, SQLite3, to create
#           a phonebook application
#
#Tested OS: This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Importing other modules for the project
import phonebook_gui
import phonebook_func



class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master=master
        self.master.minsize(500,300) #(height, width)
        self.master.maxsize(500,300)
        #This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg='#f0f0f0')
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, 'X' on windows OS.
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets form a separate module,
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
