# -*- coding: utf-8 -*-
#01_Jan_2019_17:52:19.txt

import subprocess
PIPE = subprocess.PIPE

class GitManager:
    ''' This class deals with various file operations that are related to git'''

    def __init__(self):
        print(" > __init__")        
    
    def gitManager(self):
        print(" > gitManager")
        process=subprocess.Popen(["git", "status"], stdout=PIPE, stderr=PIPE)
        stdoutput, stderroutput=process.communicate()
        stdoutput=stdoutput.decode("utf-8")
        stderroutput=stderroutput.decode("utf-8")

obj=GitManager()
print(obj.__doc__)