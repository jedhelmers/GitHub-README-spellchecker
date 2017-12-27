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


    # Iterate through text
    for body in bodyCopies:
        # Tag list to look through
        # Check paragraph tags. This should ignore all code-based text on the page
        texts = body.find_all(['p', 'h1', 'h2', 'h3', 'h4'])
        for text in texts:
            p = text.getText().upper()
            chkr.set_text(p)
            try:
                for err in chkr:
                    errorList.append(err.word.upper())
            except:
                print ""


    errorList.sort()
    error_last = ''
    cnt = 0
    for error in errorList:
        if error != error_last:
            cnt += 1
            if cnt == 1:
                # Output header
                print 'Site: %s' % url
                print "Mispelled words: "
                f.write('%s\nMispelled words: \n' % url)
            f.write('%s \n' % error.lower())
            print error.lower()
        error_last = error
    print '\n'
    f.write('\n')
    f.close()
