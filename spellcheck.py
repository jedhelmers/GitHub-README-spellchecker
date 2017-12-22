import urllib2
from bs4 import BeautifulSoup

#get URLs
urls = ["https://github.com/aandryashin/urls/blob/master/README.md", "https://github.com/jedhelmers/GitHub-README-spellchecker/blob/master/README.md"]

#iterate through URLs
for url in urls:
    #Scrape site
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

    text = ''
    p = ''
    bodyCopies = soup.find_all(class_ = 'container')
    for body in bodyCopies:
        texts = body.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
        for text in texts:
            p = text

            #ERROR: it's currently grabbing code divs within p tags
            print p.getText()
        print '\n'
    #Get meaningful text within Class .readme
    #Check paragraph tags. This should ignore all code-based text on the page

#print text
