# Add words to dictionary
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")

chkr.add('STRIKETHROUGH')

with open('mywords.txt') as f:
    words = f.readlines()

for word in words:
    chkr.add(word.strip())
    print word.strip()
