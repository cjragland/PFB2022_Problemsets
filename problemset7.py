#!/usr/bin/env python3
import sys
import re



#Moved text files from course repository to my repository while in course sub-directory 'files'
#Example
#cp Python_07_nobody.txt /Users/student/pfb_problemsets



#Question 1
#First did cat file_name to print the file in the terminal to look at it

#Establish the counter and open the file
with open("Python_07_nobody.txt", "r") as nobodyFile:
  nobodyCount = 0

#Go through the file, homogenize, look for term and add to count  
  for line in nobodyFile:
    line = line.lower()
    if 'nobody' in line:
      nobodyCount = nobodyCount + 1
#Output is the final count
print(nobodyCount)



#Question 2

#Open the file to read, make the file to write
with open("Python_07_nobody.txt", "r") as nobodyFile, open ("Rolobody.txt", "w") as roloFile:
  
  # Look for the word regardless of case
  for line in nobodyFile: 
    if re.search(r"[Nn]obody", line):
      
      # Replace with Rolobody and write to the new file
      line = re.sub(r"[Nn]obody", "Rolo", line)			#This line has an issue
      roloFile.write(line)
    
    # Excute if there is no nobody in the line
    else: 
      roloFile.write(line)

# Indicate the method ran in the STDOUT
print("Wrote RoloFile.txt, cat to print to output!")



#Question 3
#Return a list of the headers in a .fasta file
with open ("Python_07.fasta", "r") as fastaFile:
  fastaHeaders = []
  for line in fastaFile:
    line = line.rstrip()
    # Search for the > that indicates a header line and add that line
    if re.search(r">", line):
      fastaHeaders.append(line) 			### How to remove the > to look prettier?

  print("\nHere are the genes and descriptors in this fasta file\n", fastaHeaders)



#Question 4
print("\nHere we split the header into gene name and gene description:") 
with open ("Python_07.fasta", "r") as fastaFile:
  for line in fastaFile:
    #line = line.rstrip()
    #Idetify a header line
    if re.search(r">", line):
      
      # Search the sequence and delineate 
      geneInfo = re.search((r"^>(.+?)\s(.+)"), line)
      
      # Obtain the gene name/ID and gene description and store in seperate variables
      geneID = geneInfo.group(1)
      geneDescript = geneInfo.group(2)
      print("id:" + geneID + "\t" + "desc:" + geneDescript)




#Question 5
def parse_fasta(fasta):
  ### Let's make a FASTA parser dict with gene name: gene sequence")
  
  #Establish a dictionary where the parsed sequences will be stored under their gene ID
  with open (fasta, "r") as fastaFile:
    parseDict = {}

    # Go through the file lines
    for line in fastaFile:
      line = line.rstrip()
    
      # Search for headers and delineate to extract the geneIDs 
      if re.search(r">", line): 
        geneInfo = re.finditer((r"^>(.+?)\s"), line)
        print(geneInfo)
        geneID = geneInfo.group(0) 			### Why is this throwing an error? ###
    
      # Establish a dict entry for the gene id by adding the first line of the sequence     
      elif geneID in parseDict:
        parseDict[geneID] = parseDict[geneID] + line
    
      # Add to an existing entry to handle a sequence spanning multiple lines
      else:
        parseDict[geneID] = line

  return(parseDict)



#Question 6
print("\n\nLet's find all the ApoI cut sites in a sequence from a fasta file:")
# ApoI: R^AATTY		R=AorG	Y=CorT 

# Parse the fasta file into a dictionary and check the output
seqDict = parse_fasta("Python_07_ApoI.fasta")
print(seqDict)

# Go thru the sequence dictionary
# Find and creat a list of the cut sites for each gene
#for gene in seqDict:
  #cutSites = re.finditer((r"[AG]AATT[CT]"), seqDict[gene])
  
  # Print the positions of the cut sites  
  #for site in cutSites:
      #print(site.start(), site.end())
    




