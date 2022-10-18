#!/usr/bin/env python3
import sys
import re
fasta = sys.argv[1]
# Type in terminal chmd +x problemset8.py to run on the command line

class NotFASTAError(Exception):
  pass



# A very useful function made in problemset 7 Q5
### Let's make a FASTA parser dict with gene name: gene sequence")
def parse_fasta(aFastaFile):

  try:
    print("User provided file name: " + aFastaFile)
    #if aFastaFile == "":
      #raise
    if not re.search(r"\.fasta$|\.fa$", aFastaFile):
      print("evaluated")
      raise NotFASTAError ("Not a FASTA file")
 
    # Establish a dictionary where the parsed sequences will be stored under their gene ID
    with open (aFastaFile, "r") as fastaObject:
      parseDict = {}

      # Go through the file lines
      for line in fastaObject:
        line = line.rstrip()
   
        # Search for headers and delineate to extract the geneIDs 
        if re.search(r">", line):
          geneInfo = re.search(r"^>(.+?)\s(.+)", line)
          geneID = geneInfo.group(1)
          print(geneID)
        # Add to an existing entry to handle a sequence spanning multiple lines
        elif geneID in parseDict:
          parseDict[geneID] = parseDict[geneID] + line
 
        # Establish a dict entry for the gene id by adding the first line of the sequence     
        else:
          parseDict[geneID] = line

    # Return a dictionary key: geneID, value: full sequence
    return(parseDict)

  except NotFASTAError:
    print("Please provide a valid file name with extension .fa or .fasta in fasta format")
    exit(1)


returnedDict = parse_fasta(fasta)
for key in returnedDict:
  print(key, returnedDict[key])


