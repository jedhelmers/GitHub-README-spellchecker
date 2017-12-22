import urllib2
from bs4 import BeautifulSoup

from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")

personal_dictionary = ['URL', 'URLS', 'Simpliest', 'github']

#d2 = enchant.DictWithPWL("en_US","mywords.txt")

#get URLs
urls = ["https://github.com/aandryashin/urls/blob/master/README.md", "https://github.com/jedhelmers/GitHub-README-spellchecker/blob/master/README.md"]

#iterate through URLs
for url in urls:
    #Scrape site
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

    #extract unwanted tags HERE
    [s.extract() for s in soup(['code', 'a'])]

    text = ''
    p = ''
    bodyCopies = soup.find_all(class_ = 'markdown-body')

    for body in bodyCopies:
        texts = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
        for text in texts:
            p = text.getText().upper()
            chkr.set_text(p)
            try:
                for err in chkr:
                    for x in personal_dictionary:
                        if err.word == x.upper():
                            break
                        else:
                            print "ERROR", err.word, x.upper()
                            
            except:
                print ""

            #print p.getText()
    print '\n'
    #Get meaningful text within Class .readme
    #Check paragraph tags. This should ignore all code-based text on the page

#print text
