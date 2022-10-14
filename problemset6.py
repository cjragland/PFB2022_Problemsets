#!/usr/bin/env python3
import sys
import re



#Question 1

#This method splits the str into separate terms
mySet = set('ATGTGGG')

#This method makes the input an entry in the set
#Reassigning just overwrites
mySet2 = {'ATGCCT'}
mySet2 = {'AGCCCC'}

#Compare sets
print(mySet, mySet2)



#Question 2
setA = {3,14,15,9,26,5,35,9}
setB = {60,22,14,0,9}
print("Original sets:", setA, setB)

#Intersection
print("Sets intersection:\t", setA.intersection(setB))

#Difference
print("Difference:\t", setA.difference(setB))
print("Difference:\t", setB.difference(setA))
#These are different

#Union
print("Union:\t", setA.union(setB))

#Symmetrical difference
print("Symm difference:\t", setA.symmetric_difference(setB))
print("Symm difference:\t", setB.symmetric_difference(setA))
#These are the same



#Question 3
seqSet = set("GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC")
print("Making a set with a DNA sequence looks like:", seqSet)



#Question 4
seq = "GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA"
setSeq = set(seq)
print("The uniquie characters in this DNA sequence are:", setSeq)

#Establish all outputs
ntDict = {}

#Go though the sequence and count the number of each NT
for nt in setSeq:
  ntCount = seq.count(nt) 

#Store the count in a dictionary
  ntDict[nt] = ntCount
  print(ntCount)
print(ntDict)

countA = ntDict['A']
countT = ntDict['T']
countG = ntDict['G']
countC = ntDict['C']
countAll = len(seq)
portionGC = (seq.count('G') + seq.count('C')) / countAll * 100

#Report NT composition and report %GC
print("This sequence is:" , countA , "% A," , countT , "% T," ,  countG , "% G," , countC , "% C, and" , portionGC , "% GC.") 



#Question 5,6
with open ("Python_06.txt", "r") as lowerFile, open ("Python_06_upper.txt", "w") as upperFile:
  for line in lowerFile:
    line = line.rstrip()
    line = line.upper()
    upperFile.write(line + "\n")



#Question 7
with open ("Python_06.seq.txt", "r") as forFile:
  seqDict = {}
  #Got thru the file and store in a dictionary
  for line in forFile:
    seqName, seq = line.split()                  #seq still has a new line
    seqDict[seqName] = seq.rstrip().lower()      #lowercase to help conversion

#Convert to reverse complement
print("This is a list of reverse complement sequences for file Python_06.seq.txt")
for gene in seqDict:
  complement = seqDict[gene].replace("a", "T")
  complement = seqDict[gene].replace("t", "A")
  complement = seqDict[gene].replace("g", "C")
  complement = seqDict[gene].replace("c", "G")
  complement[::-1]
  print(">" + gene + "\n" + complement)

#Captured to output to a file in the terminal
#student@info-02 pfb_problemsets % ./problemset6.py > Python_06_complement.txt
#Then printed to the terminal using cat Python_06_complement.txt


 



















