from sys import argv
import argparse
import random
import urllib.request
import datetime
import re
from collections import OrderedDict

parser = argparse.ArgumentParser(description='welcomeBach: Your daily dose of counterpoint')
parser.add_argument("-v", 
        "--verbosity", 
        help="Increase/decrease output verbosity (default = 3)", 
        type=int, 
        default=3)
parser.add_argument("-r",
        "--relisten",
        help="Relisten to the last BWV",
        action="store_true",
        default=False)
args = parser.parse_args()

#if no argument is passed, print 3 links as default
number = args.verbosity

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

#if passed with argv -r, for "relisten", get the last item from the listened list
#else, check if it has already been heard, if so, choose another pice 
if args.relisten == True:
    with open('listened.txt', 'r') as f:
        for line in f:
            pass
        piece = line
else:
    with open('listened.txt', 'r+') as f:
        while True:
            for line in f:
                if piece in line:
                    n = random.randint(1, 1105)
                    piece = bwv[n]
                    continue
            else:
                f.write(piece)
                break

print("Today's Bach is: \n ", piece)

#look for it on youtube
query = urllib.parse.quote(piece)
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
