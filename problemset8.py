#!/usr/bin/env Python3
import sys
import re
# Type in terminal chmod +x problemset8.py



# A very useful function made in problemset 7 Q5
def parse_fasta(fasta):
### Let's make a FASTA parser dict with gene name: gene sequence")
 
# Establish a dictionary where the parsed sequences will be stored under their gene ID
  with open (fasta, "r") as fastaFile:
    parseDict = {}

    # Go through the file lines
    for line in fastaFile:
      line = line.rstrip()
   
      # Search for headers and delineate to extract the geneIDs 
      if re.search(r">", line):
        geneInfo = re.search((r"^>(.+?)\s(.+)"), line)
        geneID = geneInfo.group(1)
 
      # Establish a dict entry for the gene id by adding the first line of the sequence     
      elif geneID in parseDict:
        parseDict[geneID] = parseDict[geneID] + line
 
      # Add to an existing entry to handle a sequence spanning multiple lines
      else:
        parseDict[geneID] = line

  # Return a dictionary key: geneID, value: full sequence
  return(parseDict)


#Question 1

# Input fasta from terminal user input to make a geneID, sequence dictionary for the nt dictionary
fastaInput = sys.argv[1]
fastaDict = parse_fasta(fastaInput)

print(f"\n\nLet's calculate the nucleotide content of the sequences in {fastaInput}:")
ntDict = {}

# Take a dictionary of geneID, sequence and calculate the ATGC count for each
for gene in fastaDict:
  
  countA = str(fastaDict[gene].count('A'))
  countT = str(fastaDict[gene].count('T'))
  countG = str(fastaDict[gene].count('G'))
  countC = str(fastaDict[gene].count('C'))
  countN = str(fastaDict[gene].count('N'))

  # Make a new multidimentional dictionary
  ntDict = {gene: {'A': countA, 'T': countT, 'C': countC, 'G': countG, 'N': countN}} 

  # print out the results as seqName\tA_count\tT_count\tG_count\C_count
  print(gene + '\t' + ntDict[gene]['A'] + '\t' + ntDict[gene]['T'] + '\t' + ntDict[gene]['G'] + '\t' + ntDict[gene]['C'] + '\t' + ntDict[gene]['N'])



#Question 3

print("\n\nFind the first open reading frame in each sequence") 
fastaDict = parse_fasta(fastaInput)

for gene in fastaDict:
  frameNum = 0
    
  # Check for an ATG and obtain its first index
  if not 'ATG' in fastaDict[gene]:
    continue
  else:
    beginATG = fastaDict[gene].find("ATG")
    
    # Generate the header for the ORFs
    frameNum = frameNum + 1
    frame = str(frameNum)
    frameHeader = (gene + "-frame-" + frame + "-codons")

    # Move along the sequence in 3 nt increments
    codonString = ""
    codonBegin = beginATG
    codonEnd = codonBegin + 3					# Non-inclusive
    codonSlice = fastaDict[gene][codonBegin:codonEnd]

    # Check that the previously added codon was not a STOP
    while 'TAG' not in codonSlice and 'TGA' not in codonSlice and 'TAA' not in codonSlice:
      
      # Check that we haven't exceeded the length of the sequence
      if codonEnd > len(fastaDict[gene]):
        print("The gene" , gene , "does not contain a valid open reading frame")
        break
      
      # Add the codon to the ORF string and prepare for the next codon
      else:
        codonString = codonString + codonSlice + " "
        codonBegin = codonBegin + 3
        codonEnd = codonBegin + 3
        codonSlice = fastaDict[gene][codonBegin:codonEnd]
 
  # Add the STOP codon that broke the while loop, note no space char
  codonString = codonString + codonSlice
 
  # Output gene header and ORF
  print(frameHeader + "\n" + codonString)
  







