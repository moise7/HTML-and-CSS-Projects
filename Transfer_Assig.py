import shutil
import os
import time
import tkinter
from tkinter import*



#set where the source of the file are
source = 'C:\\python_projects\\Transfer\\A'

destination = 'C:\\python_projects\\Transfer\\B'
files = os.listdir(source)

for i in files:
    if i.endswith(".txt"):
        abspath= os.path.join(source, i)
        time = os.path.getmtime(abspath)
        print(i, time)
    #we are saying move the files represented by 'i' to their new destination
        shutil.move(abspath, destination)
         


#Creating UI that contain the files to be checked daily
        #First
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)


if __name__ == "__main__main":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
#Second 
win = Tk()
f = Frame(win)
b1 = Button(f, text="Check")
b2 = Button(f, text= "")
b1.configure(text="Check Work")
b1.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()
