adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
adhoc1=[]
adhoc2=[]
for i in adhoc:
	if i>5:
	   adhoc1.append(i)

	if i<=2:
	   adhoc2.append(i)

print("no greater then 5")
print(adhoc1)
print("no less thenor equal to 2")
print(adhoc2)
	
