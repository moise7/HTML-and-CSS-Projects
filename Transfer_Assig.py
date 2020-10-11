import shutil
import os
import time
import tkinter as tk
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
def Browser1(txtBrowser1):{
    askdirectory()
    }
    
        
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
    

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,300))
        self.master.title('Transfer')
    
        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.lblDisplay = Label(self.master,text='Daily', font=("Helvetica", 14))
        self.lblDisplay.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowse1 = Button(self.master,text='Receive', font=("Helvetica", 14), command=self.Browser1)
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(30,0), sticky=W)

        self.btnBrowse2 = Button(self.master,text='File Check', font=("Helvetica", 14), command=self.Browser2)
        self.btnBrowse2.grid(row=4, column=0, padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=3, column=2, padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=4, column=2, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Check for daily Files", font=("", 14), command=self.submit) 
        self.btnSubmit.grid(row=6, column=0, padx=(30,0), pady=(30,0), sticky=SW)
                                 
        self.btnCancel = Button(self.master, text="Close Program", font=("", 14), command=self.cancel)
        self.btnCancel.grid(row=6, column=2, padx=(0,0), pady=(30,0), sticky=SE)

        def submit(self):
            browser = self.varBrowse1.get()
            browser1 = self.varBrowse2.get()
            self.lblDisplay.config(text='Hello {} {}'.format(fn,ln))

    def cancel(self):
        self.master.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

