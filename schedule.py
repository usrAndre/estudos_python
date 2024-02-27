# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import schedule 
def call_me(): 
  print("I am invoked")
schedule.every(1).seconds.do(call_me)
while True: 
  schedule.run_pending()
