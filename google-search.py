import spellcheck

try:
    from google import search
except ImportError:
    print("No module named 'google' found")



# Search: Dump what you would say in a normal google search
query = 'site:https://github.com AND url:README.md'

for j in search(query, tld="co.in", num=10, stop=4, pause=0):
    spellcheck.spellCheck(j)
    #print(j)

#for url in urls:
#    spellcheck.spellCheck(url)
    #print(url)

#print "\n"
