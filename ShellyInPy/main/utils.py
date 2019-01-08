# -*- coding: utf-8 -*-
from datetime import datetime

class definedUtils:
   """
   This is class with different functionalities defined that are used most frequently
   """ 
   def todayDate(self):
#       %d_%b_%Y_%H:%M:%S
       return datetime.now().strftime('%d %B %Y')
    