#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 06:52:41 2019

@author: suhaas
"""
from PyQt5.QtCore import QThread, pyqtSignal
from gitMgr import GitManager

class gitProcess(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, dirPath, commitMsg):
        QThread.__init__(self)
        self.dirPath=dirPath
        self.commitMsg=commitMsg

    # run method gets called when we start the thread
    def run(self):
        print("Thread : git process running")
        gitStatus=GitManager(dirPath=self.dirPath).gitSimpleProcess(commitMsg=self.commitMsg)
        self.signal.emit("Finished the process Suhaas"+"--"+gitStatus)