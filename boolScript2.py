#!/usr/bin/env python3
import sys

myNum = int(sys.argv[1])
print("Fool, you have entered" , myNum)

# Check whether odd or even 
if myNum%2 > 0:
 even = False
 print("This is an odd number")
else:
  print("This is an even number")


# Then evaluate myNum
if myNum > 0:

# Handle positive cases
  print("This number is positive")
  if myNum <= 49:
    if even:
      print("it is an even number that is smaller than 50")
    else:
      print("and it is smaller than 50")	
  elif myNum >= 51: 
    greater50 = "it is larger than 50"
    if myNum%3 == 0:
      greater50 = greater50 + " and it is divisible by 3"
    print(greater50)

# Handle the negative cases
elif myNum < 0:
  print("This number is negative")

# Handle the zero case
else:
  print("This number is probably zero")







