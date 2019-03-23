import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,200))
        self.master.title('Folder Directory')
        self.master.config(bg='lightgray')

        self.btn_add = tk.Button(self.master,width=20,height=2,text='Select File Path',command=lambda: getFileDirectory(self))
        self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),stick=W)

        self.lblDirectory = tk.Label(self.master,bg='lightgray',text='File Directory:')
        self.lblDirectory.grid(row=9,column=0,padx=(25,0),pady=(45,10),stick=W)
        
        self.txtFileName = Entry(self.master,width=50,text='')
        self.txtFileName.grid(row=9,column=2,padx=(0,0),pady=(45,10),stick=W)


def getFileDirectory(self):
    fileDirectory = filedialog.askdirectory()
    self.txtFileName.insert(0,fileDirectory)
    widget_width = len(self.txtFileName.get())
    self.txtFileName.config(width=widget_width)
    




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
