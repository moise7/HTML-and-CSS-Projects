import shutil
import os

#set where the source of the file are
source = '/C:/Users/MBNewVision/Desktop/A/'

destination = '/C:/Users/MBNewVision/Desktop/B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
