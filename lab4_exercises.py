'''
File: wordgame.py
Authors: put your last names here
Description:
    Implements a word guessing game similar to Hangman
'''

# Import statement: DO NOT delete these! DO NOT write code above this!
import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import words for the game

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # infile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."

    # print the number of words that start with letter 'a'
    a_words = []
    new_wordlist = []
    for a1 in wordlist:
        if a1[0] == "a":
            a_words.append(a1)
        else:
            new_wordlist.append(a1)
    number_a_words = len(a_words)

    print "There are", number_a_words, "that start with 'a'."
    print len(new_wordlist)
    print len(wordlist)

    return None
            

def load_words_modified(textfile):
    """
    Receives a text file.
    Returns a list of words in the file.
    """
    
    namehandle = open(textfile, 'r')
    line = namehandle.read()  
    wordlist = line.split()
    print wordlist

    a_words = []
    non_a = []
    for a1 in wordlist:
        if a1[0] == "a":
            a_words.append(a1)
        else:
            non_a.append(a1)
    number_of_words = len(a_words)
    print len(a_words)

    return None
    
#textfile = raw_input("Which text file do you want to use: ")
#load_words_modified(textfile)



   
