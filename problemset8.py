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

# Find the first open reading frame in each sequence 
fastaDict = parse_fasta(fastaInput)

for gene in fastaDict:
  frameNum = 0
  
  # Check for an ORF and obtain its indices
  if 'ATG' in fastaDict[gene]:
    if 'TAG' in fastaDict[gene] or 'TGA' in fastaDict[gene] or 'TAA' in fastaDict[gene]:
      beginStart = fastaDict[gene].find("ATG")
    
    if 'TAG' in fastaDict[gene]:
      beginStop = fastaDict[gene].find("TAG")
    elif 'TAG' in fastaDict[gene]:
      beginStop = fastaDict[gene].find("TGA")
    elif 'TAG' in fastaDict[gene]:
      beginStop = fastaDict[gene].find("TAA")

  # Check that start and stop codon are in a sensible order
  if not beginStart < beginStop:
    continue
  else:  
    endStop = beginStop + 3
    orf = fastaDict[gene][beginStart:endStop] 		# End is non-inclusive
    
    # Generate the header for the ORFs
    frameNum = frameNum + 1
    frame = str(frameNum)
    frameHeader = (gene + "-frame-" + frame + "-codons")

    # Move along the sequence in 3 nt increments and print the codons
    strCodons = ""
    codonStart = beginStart
    
    for n in range(int(len(orf)+1)):
      if not codonStart == endStop:
        nextCodon = orf[codonStart:codonStart+2]
        strCodons = strCodons + nextCodon		# Concatenate
        codonStart = codonStart + 3
 
  # Format output
  print(frameHeader , "\n" , strCodons , "Expected length:", len(orf))
  



