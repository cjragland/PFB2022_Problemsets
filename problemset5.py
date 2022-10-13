#!/usr/bin/env python3
import sys


#Question 1
dictFavs = {'fiction' : 'East of Eden', 'artist' : 'Misch', 'tree' : 'jacaranda'}
print(dictFavs)

#Question 2
print("Un favorito libro es:", dictFavs['fiction'])
#
##Question 3
#favThing = 'fiction'
#print("Una favorita libro (variable) es:", dictFavs[favThing])
#
##Question 4
#arbole = 'tree'
#print("Mi favorita arbole es:", dictFavs[arbole])
#
##Questin 5
#dictFavs['organism'] = 'duckweed'
#print(dictFavs)
#print("Yo pongo una cosa nueva:", dictFavs['organism'])
#print(dictFavs)
#favThing = 'organism'
#print("Yo cambia un variable:", dictFavs[favThing])
#
##Question 6
## Pass in and store command line input
##favInput = sys.argv[1]
#print("My favorite", favInput, "is", dictFavs[favInput])
#print("Ask me about my favorite:", [key for key in dictFavs])
##print("Ask me about my favorite:", dictFavs.keys())
#
####Why doesn't the alternate listing method work?
#### Returns Ask me about my favorite: dict_keys(['fiction', 'artist', 'tree', 'organism'])
#
##Question 7
#dictFavs['organism'] = 'hummingbird'
#print("Changed my animal:", dictFavs['organism'])

#Question 8
dictFavs = {'fiction' : 'East of Eden', 'artist' : 'Misch', 'tree' : 'jacaranda'}
print("\n\n", dictFavs)

#Load in user input
fromTerminal = input("Type in a type of option and your favorite thing:")
fromTerminal = fromTerminal.split()
favKey = fromTerminal[0]
favValue = fromTerminal[1]

#Reassign dict entries using user input
dictFavs[favKey] = favValue

#Print the updated dict as a list of (key,value)
print(dictFavs)
print("Updated dictionary with your input:", [(key,dictFavs[key]) for key in dictFavs])



