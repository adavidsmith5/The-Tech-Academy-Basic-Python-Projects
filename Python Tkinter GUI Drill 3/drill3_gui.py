import tkinter as tk
from tkinter import *
import os

import drill3_func as d3



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=False)
        self.master.geometry('{}x{}'.format(700,700))
        self.master.title('File Transfer')
        self.master.config(bg='lightgray')

        self.btn_add = tk.Button(self.master,width=20,height=2,text='Source Directory',command=lambda: d3.sourceFileDirectory(self))
        self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),stick=W)

        self.lblSourceDirectory = tk.Label(self.master,bg='lightgray',text='Source File Directory:')
        self.lblSourceDirectory.grid(row=9,column=0,padx=(25,0),pady=(45,10),stick=W)
        
        self.txtSourceName = Entry(self.master,width=50,text='')
        self.txtSourceName.grid(row=9,column=2,padx=(0,0),pady=(45,10),stick=W)


        self.btn_add = tk.Button(self.master,width=20,height=2,text='Destination Directory',command=lambda: d3.destinationFileDirectory(self))
        self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),stick=W)

        self.lblDestinationDirectory = tk.Label(self.master,bg='lightgray',text='Source File Directory:')
        self.lblDestinationDirectory.grid(row=11,column=0,padx=(25,0),pady=(45,10),stick=W)
        
        self.txtDestinationName = Entry(self.master,width=50,text='')
        self.txtDestinationName.grid(row=11,column=2,padx=(0,0),pady=(45,10),stick=W)
    
        self.btn_add = tk.Button(self.master,width=20,height=2,text='Transfer Files',command=lambda: d3.transferFiles(self))
        self.btn_add.grid(row=12,column=0,padx=(25,0),pady=(45,10),stick=W)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
