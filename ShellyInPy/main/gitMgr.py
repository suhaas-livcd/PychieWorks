# -*- coding: utf-8 -*-
#01_Jan_2019_17:52:19.txt

import subprocess
PIPE = subprocess.PIPE

class GitManager():
    ''' This class deals with various file operations that are related to git'''

    def __init__(self,dirPath):
        self.gitDirPath=dirPath

    def gitStatus(self):
        process=subprocess.Popen(["git", "status"], stdout=PIPE, stderr=PIPE, cwd=self.gitDirPath)
        self.gitCommunicate(process)

    def gitCommit(self,commitMsg):
        if not commitMsg:
            commitMsg="No Commit Message"
        process=subprocess.Popen(["git", "commit", "-m", commitMsg], stdout=PIPE, stderr=PIPE, cwd=self.gitDirPath)
        self.gitCommunicate(process)

    def gitAdd(self,file):
        if file:
            process=subprocess.Popen(["git", "add", file], stdout=PIPE, stderr=PIPE, cwd=self.gitDirPath)
        else:
            process=subprocess.Popen(["git", "add", "--all"], stdout=PIPE, stderr=PIPE, cwd=self.gitDirPath)
        self.gitCommunicate(process)

    def gitPush(self,username,password):
        if not username:
            process=subprocess.Popen(["git", "push"], stdout=PIPE, stderr=PIPE, cwd=self.gitDirPath)
        self.gitCommunicate(process)

    def gitCommunicate(self,process):
        stdoutput, stderroutput=process.communicate()
        self.stdoutput=stdoutput.decode("utf-8")
        self.stderroutput=stderroutput.decode("utf-8")
        self.gitOutputLog="\nSTD_OUT : "+self.stdoutput+"\n STD_ERR : "+self.stderroutput
        print(self.gitOutputLog)

    def gitSimpleProcess(self,commitMsg):
        self.gitStatus()
        self.gitAdd(file=None)
        self.gitCommit(commitMsg)
        self.gitPush(username=None,password=None)
        return self.gitOutputLog
#Instantiate with the directory path
#gitMgr=GitManager(dirPath="/home/suhaas/Desktop/MyPrepLogger")
#Spyder has some problem with showing up temp variable so just print dict
#temp=gitMgr.__dict__
#e.g to print the git status
#gitMgr.gitStatus()