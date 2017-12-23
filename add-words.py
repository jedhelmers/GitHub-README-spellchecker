# Add words to dictionary
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")

# Read from mywords
with open('mywords.txt') as f:
    words = f.readlines()

# Iterate through word list and remove whitespace
for word in words:
    chkr.add(word.strip())
    print word.strip()
