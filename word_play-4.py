# Author: MOG 3/24/22

# Open files
words = open("case-study-word-play-p22mgiroux\words.txt","r")
word = words.readlines()

 # fiterates through all the letters and if a letter isnt in the word, return false, if it makes it through with all letters being in the word, return true
def uses_only(word, letters):
    letters = list(letters)
    wlist = list(word)
    for value in letters:
        if value not in wlist:
            return False
    return True

# variable to count for the output statement
count = 0 
# Input statement
input = input("Enter the only letters that can be used: ")

for value2 in word: # for loop  and function to check each character in each word
    value2 = value2.strip()
    if uses_only(value2, input) == True:
        count += 1
# Output statement that displays the number of words comprised with the goven letters
print("{0} words use only the given letters.".format(count))

words.close()