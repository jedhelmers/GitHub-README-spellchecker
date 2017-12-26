import urllib2
from bs4 import BeautifulSoup

# Terminal Absolute clear: clear && printf '\e[3J'
# VERY HANDY!

# Spellcheck function that brings in a URL then processes
def spellCheck(url):
    f = open('TyposList.txt', 'a')

    from enchant.checker import SpellChecker
    chkr = SpellChecker("en_US")

    #Scrape site
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

    # Extract unwanted tags HERE
    [s.extract() for s in soup(['code', 'a'])]

    # Clear local variables
    errorList = []
    text = ''
    p = ''
    # Get meaningful text within Class .markdown-body
    bodyCopies = soup.find_all(class_ = 'markdown-body')

    # Output header
    print 'Site: %s' % url
    print "Mispelled words: "

    # Iterate through text
    for body in bodyCopies:
        # Tag list to look through
        # Check paragraph tags. This should ignore all code-based text on the page
        texts = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
        for text in texts:
            p = text.getText().upper()
            chkr.set_text(p)
            try:
                for err in chkr:
                    # Cleanse duplicates
                    errorList.append(err.word)
                    for error in errorList:
                        if err.word.upper() != error:
                            f.write(err.word)
                            print err.word
                            break
            except:
                print ""
    print '\n'
    f.close()
