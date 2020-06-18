import shutil
import os
import time

#set where the source of the file are
source = 'C:\\Users\\MBNewVision\\Desktop\A

destination = 'C:\Users\MBNewVision\Desktop\B
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
modification_time = os.listdir.getmtime(source,destination)
print("modified in the last 24 hours",access_time)

local_time = time.ctime(modification_time)
print("Last modification time(Local time):",local_time)
