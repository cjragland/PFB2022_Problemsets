#!/usr/bin/env python3
import sys



# Question 1
#a,b
myFavs = ["shrimp", "beach", "swimming", "gardens", "coladas"]
print(myFavs)

#c
print(myFavs[2])

#d,e
myFavs[2] = "hummingbirds"
print(myFavs)

#f,g,h
myFavs.append("cooking")
myFavs.insert(0, "trees")
myFavs.insert(5, "racquetball")
print(myFavs)

#i,j,k,
myFavs.pop()
myFavs.pop(0)
myFavs.pop(3)
print(myFavs)

#l
myFavs = ",".join(myFavs)
print(myFavs)



#Question 2
taxa = "sapjnkjfbkjjkfnkjb, erectus, neanderthals"
print(taxa)
print(taxa[1])
print(type(taxa))

species = taxa.split(",")
print(species[1])
print(species)
print( type(species))

species.sort()
print(species)

speciesSort = sorted(species, key=lambda s: len(s))
print("Species sorted by length:", speciesSort) 


#Question 3
my_list = ['a', 'bb', 'ccc']
print(my_list)
yourList = my_list.copy()
print(yourList)
yourList.append("dd")
print("My list", my_list)
print("Your list modified", yourList)



#Question 4
counter = 1
while counter < 101 and counter > 0:
  print(counter)
  counter+=1

#Question 5
product = 1000
multiplier = product - 1

while multiplier > 0:
  product = multiplier * product
  multiplier-=1
print(product)


#Question 6
nums = [101,2,15,22,95,33,2,27,72,15,52]

for n in nums:
  if n%2 == 0:
    print("These is an even number in the list:", n)



#Question 7
print(nums)
numsSorted = sorted(nums)
print(numsSorted)

sumEvens = 0
sumOdds = 0
for n in numsSorted:
  if n%2 > 0:
    sumOdds += n
  else:
    sumEvens += n
print("Sum of evens:", {sumEvens}, "Sum of odds:", {sumOdds})



#Question 8/9
for n in range(101):
  print(n)

#Question 10
startNum = int(sys.argv[1])
endNum = int(sys.argv[2])
print("Your input:", startNum, endNum)
print("Your input type:", type(startNum), type(endNum))
print("Your input range:", [n for n in range(startNum, endNum+1)])



#Question 11

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for s in seqs:
  print(str(len(s)) + "\t" + s)

#Question 12
print([(seqs.index(s),len(s),s) for s in seqs])






