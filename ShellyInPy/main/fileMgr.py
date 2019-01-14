# -*- coding: utf-8 -*-
from datetime import datetime
import os
import json

class FileManager:
    """ This class deals with various file operations like reading and writing"""
    
    def __init__(self):
        print(" > __init__")    
    
    def createFile(self,data,json):
        todayIs=datetime.now().strftime('%d_%b_%Y_%H:%M:%S')
        monthIs=datetime.now().strftime('%b')
        yearIs=datetime.now().strftime('%Y')
        mountPathIs="/home/suhaas/Desktop/MyPrepLogger/diary"
        
        #Checking if year exists
        yearList=os.listdir(mountPathIs)
        mountPathIs=mountPathIs+"/"+yearIs
        if yearIs not in yearList:
            self.createDirectory(mountPathIs)
                    
        #Checking if month dir exists
        monthList=os.listdir(mountPathIs)
        mountPathIs=mountPathIs+"/"+monthIs
        if monthIs not in monthList:
            self.createDirectory(mountPathIs)
            
        #Creating File
        
        if json:
            self.fileNameIs=mountPathIs+"/"+todayIs+".json"
        else:
            self.fileNameIs=mountPathIs+"/"+todayIs+".txt"

        with open(self.fileNameIs,'w') as file:
            print("File created : "+self.fileNameIs)
            file.close()
            if data:
                self.writeToFile(self.fileNameIs,data,json)
                
        return self.fileNameIs
    
    def writeToFile(self,filePath,dataToWrite,isJson):
        if isJson:
            with open(filePath, 'w') as outfile:
                json.dump(dataToWrite, outfile)
        else:
            with open(filePath,'w') as outfile:
                outfile.write(dataToWrite)
    
    def createDirectory(self,dirName):
        os.makedirs(dirName, exist_ok=True)

#How to use file manager
#fileMgr=FileManager()
#currentFile=fileMgr.createFile()
#currentFile_1=fileMgr.createFile(data="")
#currentFile_2=fileMgr.createFile(data="{sdfsdf}",json=None)