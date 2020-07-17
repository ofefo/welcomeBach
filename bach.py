import random
import urllib.request
import datetime
import re
from collections import OrderedDict

start = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
end = datetime.datetime.utcnow()
diff = abs((end - start).days)

with open('bwv.txt') as f:
    bwv = f.readlines()

random.seed(diff)
n = random.randint(1, 1105)
print("Today's Bach is: \n ", bwv[n])

textToSearch = bwv[n]
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
html = urllib.request.urlopen(url).read().decode('utf-8')
pattern = re.compile('videoId":"(\w{11})"')

def videoFinder(n):
    matches = []
    for vid in re.findall(pattern, html):
        v = 'https://www.youtube.com/watch?v=' + vid
        matches.append(v)
    links = list(OrderedDict.fromkeys(matches))
    for i in range(n):
        print(links[i])

videoFinder(3)
