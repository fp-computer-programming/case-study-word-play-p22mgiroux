# Author: MOG 3/24/22

# Open files
words = open("case-study-word-play-p22mgiroux\words.txt","r")
line = words.readline().strip()

def avoid(text):
    count = 0
# if any of the letters are not in the word, add it to the count
    for line in words:
        if text not in line:
            count += 1
    return count
            
# input the characters to exclude
forbidden = input("Enter the charaters to exclude: ")

# print statement and call function
print("{} words found.".format(avoid(forbidden)))

words.close()