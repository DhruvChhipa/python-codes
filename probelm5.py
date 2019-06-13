import time
name=input("enter your name/n")
currenttime=time.strftime("%t")
for i in currenttime:
	if i>5 and i<12:
		print("Good morning"+name)
	elif i>=12 and i<16:
		print("Good afternoon"+name)
	elif i>=16 and i<21:
		print("Good evening"+name)
	else:
		print("Good night")
