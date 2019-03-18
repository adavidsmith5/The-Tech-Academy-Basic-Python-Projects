import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True,height=True)
        self.master.geometry('{}x{}'.format(900,250))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.btnBrowse = Button(self.master,width=12,text='Browse...',font=('Helvetica',14),fg='black',bg='lightgray')
        self.btnBrowse.grid(row=0,column=0,padx=(30,0),pady=(60,0),sticky=NE)

        self.btnBrowse2 = Button(self.master,width=12,text='Browse...',font=('Helvetica',14),fg='black',bg='lightgray')
        self.btnBrowse2.grid(row=1,column=0,padx=(30,0),pady=(20,0),sticky=NE)

        self.btnCheckForFiles = Button(self.master,width=12,height=2,text='Check for Files',font=('Helvetica',14),fg='black',bg='lightgray')
        self.btnCheckForFiles.grid(row=2,column=0,padx=(25,0),pady=(20,0),sticky=NE)

        self.btnClose = Button(self.master,width=12,height=2,text='Close Program',font=('Helvetica',14),fg='black',bg='lightgray')
        self.btnClose.grid(row=2,column=1,padx=(30,0),pady=(20,0), sticky=NE)

        self.txtFileName = Entry(self.master,text='',width='50',font=('Helvetica',16),fg='black',bg='white')
        self.txtFileName.grid(row=0,column=1,rowspan=1,padx=(30,0),pady=(60,0),ipady=3,sticky=NE)

        self.txtFileName2 = Entry(self.master,text='',width='50',font=('Helvetica',16),fg='black',bg='white')
        self.txtFileName2.grid(row=1,column=1,rowspan=1,padx=(30,0),pady=(20,0),ipady=3,sticky=NE)
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
