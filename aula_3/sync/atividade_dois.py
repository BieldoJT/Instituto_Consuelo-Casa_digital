#!/usr/bin/python3

list = [x for x in range(1,51) if x%3 == 0 or x%5 == 0]
sum = 0
count = 0
for i in list:
	sum+=i
	count+=1
print("a soma é:", sum)
print("na lista tem",count,"elementos")
