import random
import urllib.request
import datetime
from bs4 import BeautifulSoup

start = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
end = datetime.datetime.utcnow()
diff = abs((end - start).days)

with open('bwv.txt') as f:
    bwv = f.readlines()

random.seed(diff)

n = random.randint(1, 1129)

textToSearch = bwv[n]
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

def printLinks():
    linkList = []
    for i in range(3):
        for vid in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
            v = 'https://www.youtube.com' + vid['href']
            linkList.append(v)
        print(linkList[i])

print("Today's Bach is: \n ", bwv[n])
printLinks()
