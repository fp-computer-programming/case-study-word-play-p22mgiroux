# Author: MOG 3/24/22

# Open files
words = open("case-study-word-play-p22mgiroux\words.txt","r")
greater = open("case-study-word-play-p22mgiroux\greater_than_20.txt","a")

while True:
# Iterate through all the lines of words and if the length of the word is greater than 20 (plus the newline char) put it in the greater_than_20.txt
    line = words.readline()
    if len(line) > 21:
        greater.write(line)
        continue
    if len(line) == 0:
        break

# Close files
words.close()
greater.close()