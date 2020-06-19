import shutil
import os
import time
from tkinter import*
import tkinter as tk
from tkinter import messagebox

#set where the source of the file are
source = 'C:\python_projects\Transfer\A'

destination = 'C:\python_projects\Transfer\B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
modification_time = os.listdir.getmtime(source,destination)
print("modified in the last 24 hours",access_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):",local_time)

#Creating UI that contain the files to be checked daily
window=Tk()
var = StringVar()
var.set("Daily")
data=('C:\python_projects\Transfer\A')
mgb = messagebox(windows, values=data)
mgb.place(x=60, y=150)
#Creating UI for Receiving and file checking
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Receive", variable=v0,value=1)
r2=Radiobutton(window, text="File Check", variable=v0,value=2)



if __name__ == "__main__main":
    pass()
