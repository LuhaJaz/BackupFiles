import os
import shutil
source= input("Enter Source File Name")
destination=input("Enter Destination Folder Name")
source= source+"/"
destination= destination+"/"
listoffiles= os.listdir(source)
for file in listoffiles: 
    shutil.move((source+file), destination)
