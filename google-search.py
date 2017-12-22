try:
    from google import search
except ImportError:
    print("No module named 'google' found")

# to search
query = 'site:https://github.com AND url:README.md'

for j in search(query, tld="co.in", num=100, stop=1, pause=2):
    print(j)
