#!/usr/bin/env python3
import sys

# variables for personal info
myName = "Carin"
myColor = "red"
myHobby = "gardening"
myAnimal = "hummingbird"

# To print personal info as separate statements
#print("My name: Carin")
#print("My favorite color: red")
#print("My favorite activity" , myHobby)
#print("My favorite animal" , myAnimal)

# To print as a single statement in the command line
name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]
print("Hi, my name is " + name + ". My favorite color, activity and animal are " +  color + ", " + activity + " and " + animal)

