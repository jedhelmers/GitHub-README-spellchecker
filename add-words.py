# Add words to dictionary
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")

words = ['url', 'urls', 'github', 'html', 'http', 'https', 'BeautifulSoup', 'etcd', 'pip', 'sudo', 'readme', 'spellchecker']

for word in words:
    chkr.add(word)
