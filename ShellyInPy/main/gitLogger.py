# -*- coding: utf-8 -*-
#01_Jan_2019_17:52:19.txt
from datetime import datetime
import os

todayIs=datetime.now().strftime('%d_%b_%Y_%H:%M:%S')
monthIs=datetime.now().strftime('%b')
yearIs=datetime.now().strftime('%Y')
print(type(yearIs))
print(todayIs)
print(monthIs,yearIs)
print(os.path.isdir("/home/el"))
print(os.path.exists("/home/el/myfile.txt"))
print(os.listdir("/home/suhaas/Desktop/MyPrepLogger/diary"))
mountPathIs="/home/suhaas/Desktop/MyPrepLogger/diary"
yearList=os.listdir(mountPathIs)
if yearIs in yearList:
    mountPathIs=mountPathIs+"/"+yearIs
    monthList=os.listdir(mountPathIs)
    if monthIs in monthList:
        mountPathIs=mountPathIs+"/"+monthIs
        filesList=os.listdir(mountPathIs)    
else:
    print("Not exist")