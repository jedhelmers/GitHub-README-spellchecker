import spellcheck

try:
    from google import search
except ImportError:
    print("No module named 'google' found")



# Search: Dump what you would say in a normal google search
query = 'site:https://github.com AND url:README.md'

for j in search(query, tld="co.in", num=10, lang='en', start=201, stop=300, pause=0):
    try:
        spellcheck.spellCheck(j)
    except:
        print ""
    #print(j)

#for url in urls:
#    spellcheck.spellCheck(url)
    #print(url)

#print "\n"
