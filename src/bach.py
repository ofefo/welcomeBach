from sys import argv, exit
from os import chdir
from collections import OrderedDict
import csv
import argparse
import random
import urllib.request
import datetime
import re

catalogue = {}
with open('dict.csv', newline='') as f:
    catalogue = dict(filter(None, csv.reader(f)))

keys = list(catalogue.keys())

parser = argparse.ArgumentParser(description='welcomeBach: Your daily dose of counterpoint')
parser.add_argument('-v', 
        '--verbosity', 
        help='Increase/decrease output verbosity (default = 3)', 
        type=int, 
        default=3)
parser.add_argument('-r',
        '--relisten',
        help='Relisten to the last BWV',
        action='store_true',
        default=False)
parser.add_argument('-c',
        '--composer',
        choices=keys,
        help='Choose the composer you want to listen to',
        type=str,
        default='Bach')
args = parser.parse_args()

#if no argument is passed, print 3 links as default
number = args.verbosity

#if no argument is passed, Bach is the desired composer
composer = args.composer
composer = composer.title()

#set the seed for random as the difference in days from today and January 1st, 2020
start = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
end = datetime.datetime.utcnow()
diff = abs((end - start).days)
random.seed(diff)

#set .txt file name according to dictionary
chdir('../catalogues')
txtName = str(catalogue[composer] + '.txt')

#choose today's opus
with open(txtName) as f:
    opus = f.readlines()
    count = len(opus)
n = random.randint(1, count)
piece = opus[n] 

#if passed with argv -r, for "relisten", get the last item from the listened list
#else, check if it has already been heard, if so, choose another pice 
chdir('../listens')
listened = str(catalogue[composer] + 'listened.txt')
if args.relisten == True:
    with open(listened, 'r') as f:
        for line in f:
            pass
        piece = line
else:
    with open(listened, 'r+') as f:
        while True:
            for line in f:
                if piece in line:
                    n = random.randint(1, count)
                    piece = opus[n]
                    continue
            else:
                f.write(piece)
                break

print("Today's %s is: \n " % composer, piece)

#look for it on youtube
query = urllib.parse.quote(composer + ' ' + piece)
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