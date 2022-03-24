# Author: MOG 3/24/22

# Open files
words = open("case-study-word-play-p22mgiroux\words.txt","r")
no_es = open("case-study-word-play-p22mgiroux\words_without_e.txt","a")

def no_e(words, no_es):
    while True:
        es = 0
        total = 0
# Iterate through all the lines of words and if the word doesnt have an e in it put it in the words_without_e.txt
        line = words.readline()
        total += 1
        if "e" not in line:
            no_es.write(line)
            es += 1
            continue
        if len(line) == 0:
#print percentage
            print("Percentage of words without 'e' in them: {}%".format(total / es))
            break
# Call function
no_e(words, no_es)

# Close files
words.close()
no_es.close()