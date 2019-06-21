#!/usr/bin/python3
import time
name=input("enter name")
age=int(input("age"))
todaydate=time.strftime("%Y")
remyear=95-age+int(todaydate)
print(remyear)
print(name+"is 95 year old"+str(remyear))
