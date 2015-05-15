'''
File:Huang_Ramirez_textanalysis.py
Author:Yinya Huang and Nicol Ramirez
Description:
    Prompts for the name of a text file
    Puts the unique words in the text file in a list 
    Tracks the number of times a unique word occurs in the text
    Prints the number of unique words
    Prints the unique word and its frequency.
'''
unique_words=[]
times_unique_word=[]


def textanalysis(text_file):
    '''
    Prints the number of unique words and each unique word with its frequency.
    Receives the name of a text file.
    Returns a list of words (allwords) in the file.
    '''
    #open the text document 
    infile = open(text_file, 'r')

    #line is single string 
    line = infile.read()

    #makes sures that there are no non-letter characters in the string and
    #replaces non-letter characters with a space
    for c in line:
        if c.isalpha():
            pass
        else:
            line = line.replace(c,' ')

    #make a list of all the individual words
    allwords = line.split()

    #calls the function find_unique to print statements
    print_unique = find_unique(allwords)
    
    return None

def find_unique(allwords):
    '''
    Puts unique words in a list & puts their frequency in another list.
    Prints the number of unique words and each unique word with it frequency.
    Receives a list of words (allwords).
    Returns the printed statements.
    '''
    #loop for each word the list allwords
    for word in allwords:

        #makes each word in lowercase 
        word=word.lower()

        #adds word to list of unique words if not already in
        #adds 1 to list times_unique_word
        #index same for word in unique_words and 1 in times_unique_word
        if word not in unique_words:
            unique_words.append(word)
            times_unique_word.append(1)

        #add 1 to frequency in times_unique_word if occurs again
        else:
            index = unique_words.index(word)
            times_unique_word[index]= times_unique_word[index]+1

    #print statements         
    print "Number of unique words in the text is",str(len(unique_words))
    print "Below is a list of the unique words with their frequency."

    #print each unique word with its frequency
    for word in unique_words:
        print word, ",", times_unique_word[unique_words.index(word)]
    return None


#prompts for the name of a text file
text_file = raw_input('Please enter the name of a text file: ')
textanalysis(text_file)
