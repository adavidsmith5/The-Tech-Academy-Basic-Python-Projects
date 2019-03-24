import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import shutil

import drill3_gui

import sqlite3

conn = sqlite3.connect('dBPractice.db')



def sourceFileDirectory(self):
    self.txtSourceName.delete(0,END)
    fileDirectory = filedialog.askdirectory()
    self.txtSourceName.insert(0,fileDirectory)
    widget_width = len(self.txtSourceName.get())
    self.txtSourceName.config(width=widget_width)


def destinationFileDirectory(self):
    self.txtDestinationName.delete(0,END)
    fileDirectory = filedialog.askdirectory()
    self.txtDestinationName.insert(0,fileDirectory)
    widget_width = len(self.txtDestinationName.get())
    self.txtDestinationName.config(width=widget_width)

def transferFiles(self):
    source = self.txtSourceName.get()
    destination = self.txtDestinationName.get()
    print(os.listdir(source))
    print(os.listdir(destination))
    #check files in source for .txt
    sourceTxtFiles = []
    time = []
    sourceFiles = os.listdir(source)
    for file in sourceFiles:
        if file.endswith('.txt'):
            sourceTxtFiles.append(file)
            time.append(os.path.getmtime(os.path.join(source,file)))
        

    #move files from source to destination
    for file in sourceTxtFiles:
        shutil.move(os.path.join(source,file),os.path.join(destination,file))


    #create dictionary for files and timestamps
    filesWithTime = {}
    i=0
    while i < len(sourceTxtFiles):
        filesWithTime[sourceTxtFiles[i]]=time[i]
        i+=1

    
    #create database
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_transferTxtFiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT, \
        col_modifiedDate TEXT \
        )")
        conn.commit()

    #add files to database
        

    for file, time in filesWithTime.items():
        cur.execute("INSERT INTO tbl_transferTxtFiles(col_fileName,col_modifiedDate) VALUES (?,?)", \
                ('{}'.format(file),'{}'.format(time)))
        conn.commit()
    
    conn.close()



    #print files that were transferred
    for file in filesWithTime:
        print('{}: {}'.format(file,filesWithTime[file]))
