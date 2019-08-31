# Erik Macik
# To run, please use "$ python3 wordCount.py <name-of-input-file>.txt <name-of-output-file>.txt"

# This Python program reads an input file and outputs a new file containing each word and the number of occurrences
# of each word. The output file sorts words lexicographically.

import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists

# User must provide only two arguments
if len(sys.argv) is not 3:
    print("ERROR! Incorrect usage. Please use $ wordCount.py <input text file> <output file>")
    exit()

# Store the names of input and output files provided by user
textFileInputName = sys.argv[1]
outputFileName = sys.argv[2]

# Exit if input file doesn't exist
if not os.path.exists(textFileInputName):
    print("ERROR! " + textFileInputName + " doesn't exist! Exiting")
    exit()

# Empty dictionary
wordDictionary = {}

# Open input file and record instances of words
with open(textFileInputName, 'r') as inputFile:
    for line in inputFile:
        # Remove new line characters
        line = line.strip()
        # Split by anything that is not a letter and optional new line character: removes punctuation and whitespace
        words = re.split('[^A-Za-z]+', line)
        for word in words:
            # Ignore blank space words
            word = word.lower()
            if word == '':
                continue
            if word in wordDictionary:
                wordDictionary[word] += 1
            else:
                wordDictionary[word] = 1

# Open output file or create it if it doesn't exist
outputFile = open(outputFileName, 'w')

# Write all words and occurences to file
for key in sorted(wordDictionary):
    outputFile.write(key + " " + str(wordDictionary[key]) + "\n")
