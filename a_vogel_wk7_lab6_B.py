filename = input("Please enter the file name:\n")       #ask for a file
from collections import Counter                         #import counter from collections library
count = Counter()                                       #assign counter function
dictionary = {}                                         #initialize dictionary
for line in open(filename, 'r'):                        #iterate over lines in open file
    line = line.split()                                 #split lines
    for word in line:                                   #iterate through words of each line
        word = word.lower()                             #lowercase each word so capitlized words are counted the same as lowecase words
        count[word] += 1                                #count each word occurence and increment for each new occurence
        dictionary[word] = count[word]                  #assign the words and their frequency to the dictionary
for key, value in sorted(dictionary.items()):           #sort dictionary alphabetically
    print("%s: %s" % (key, value))                      #print the dictionary
