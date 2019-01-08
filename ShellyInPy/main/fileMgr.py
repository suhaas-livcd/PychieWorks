# -*- coding: utf-8 -*-
from datetime import datetime
import os

class FileManager:
    """ This class deals with various file operations like reading and writing"""
    
    def __init__(self):
        print(" > __init__")    
    
    def fileHandling(self):
        print(" >  fileHandling")
        todayIs=datetime.now().strftime('%d_%b_%Y_%H:%M:%S')
        monthIs=datetime.now().strftime('%b')
        yearIs=datetime.now().strftime('%Y')
        mountPathIs="/home/suhaas/Desktop/MyPrepLogger/diary"
        yearList=os.listdir(mountPathIs)
        if yearIs in yearList:
            mountPathIs=mountPathIs+"/"+yearIs
            monthList=os.listdir(mountPathIs)
            if monthIs in monthList:
                mountPathIs=mountPathIs+"/"+monthIs
                fileNameIs=mountPathIs+"/"+todayIs+".txt"
                with open(fileNameIs,'w') as f:
                    f.write("write in this the content of the diary")
            else:
                os.mkdir(monthIs)
        else:
            os.mkdir(yearIs)

fileMgr=FileManager()