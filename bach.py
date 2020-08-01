from sys import argv
import random
import urllib.request
import datetime
import re
from collections import OrderedDict

#if no argument is passed, prints 3 links as default
if len(argv) < 2:
    number = 3
else:
    number = int(argv[1])

#set the seed for random as the difference in days from today and January 1st, 2020
start = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
end = datetime.datetime.utcnow()
diff = abs((end - start).days)
random.seed(diff)

#choose today's piece
with open('bwv.txt') as f:
    bwv = f.readlines()

n = random.randint(1, 1105)
piece = bwv[n] 

#if it has already been heard, get the next one on the list
with open('listened.txt', 'r+') as f:
    while True:
        for line in f:
            if piece in line:
                n += 1
                piece = bwv[n]
                continue
        else:
            f.write(piece)
            break

print("Today's Bach is: \n ", piece)

#looks for it on youtube
textToSearch = piece
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
html = urllib.request.urlopen(url).read().decode('utf-8')
pattern = re.compile('videoId":"(\w{11})"')

#print N video links based on input argument
def videoFinder(n):
    matches = []
    for vid in re.findall(pattern, html):
        v = 'https://www.youtube.com/watch?v=' + vid
        matches.append(v)
    links = list(OrderedDict.fromkeys(matches))
    for i in range(n):
        print(links[i])

videoFinder(number)
