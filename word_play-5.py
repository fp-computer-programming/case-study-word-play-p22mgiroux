# Author: MOG 3/24/22

words = open("case-study-word-play-p22mgiroux\words.txt","r")
word = words.readlines()

# if a word is equal to itself, sorted, then return true
def is_abecedarian(w):
    y = list(w)
    y.sort()
    if list(w) == y:
        return True
    else:
        return False

# if a word is in alphabetical order, add it to the count
count = 0 
for value in word:
    value = value.strip()
    if is_abecedarian(value) == True:
        count += 1

print("{} words are in alphabetical order.".format(count))

words.close()