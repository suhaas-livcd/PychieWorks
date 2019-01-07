# -*- coding: utf-8 -*-

class Database:
    def __init__(self):
        print("__init__ function called")
    
    def function2(self):
        print(" __function2 is called")

testObj = Database()
testObj.function2()