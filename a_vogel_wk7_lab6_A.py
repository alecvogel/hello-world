filename = input("Please enter the file name:\n")
dictionary = {}
with open(filename) as f:
    for number, line in enumerate(f, 1):
        line = line.strip("\n")
        line.strip()
        line.split(',')
        dictionary[number] = line      
def filecontent(dictionary):
    while True:
        selection = int(input("Select a search option:\nEnter \'1\' to search for a line number\nEnter \'2\' to search for a word\nEnter \'0\' to quit\n"))
        if selection == 0:
            break
        elif selection == 1:
            lineNumber = int(input("Please enter the line number: "))
            if lineNumber == 0:
                break
            else:
                if lineNumber in dictionary:
                    print(dictionary[lineNumber])
                else:
                    print("Error, line number not found.")
        elif selection == 2:
            word = input("Word: ")
            for keys, values in dictionary.items():
                for string in values.split():
                    if word in string:
                        print("Word found in line " + str(keys))
                        break
                    else:
                        print("Word not found.")
filecontent(dictionary)
