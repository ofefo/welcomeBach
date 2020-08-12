#DOWNLOAD NEW CATALOGUES FROM WIKIPEDIA PAGES
#NEEDS BEAUTIFUL SOUP
from bs4 import BeautifulSoup
from os import chdir
import urllib.request
import csv

composerName = input('What is the composer last name?\n ')
fileName = input('What is your filename? (E.g.: \"bwv.txt\")\n ')
symbol = fileName.replace('.txt', '')
url = input('What is your url?\n ')
opusOrNot = input('Is it by Opus? (y/n)\n ')
opusOrNot = opusOrNot.lower()
colNumber = int(input('What is the index of the column in which the work number is located?\n '))
colNumber -= 1
colName = int(input('What is the index of the column in which the work name is located?\n '))
colName -= 1

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs={'class':'wikitable sortable'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

opusName = []
for i in data:
    if len(i) > 0:
        opusName.append(i[colName])
    else:
        pass

opusNumber = []
for i in data:
    if opusOrNot == 'y':
        if len(i) > 0:
            opusNumber.append('Op. ' + i[colNumber] + ' ')
        else:
            pass
    else:
        if len(i) > 0:
            opusNumber.append(fileName.replace('.txt', ' ').replace('\"', '').upper() + i[colNumber] + ' ')
        else:
            pass

catalogueLine = [x + y for x,y in zip(opusNumber, opusName)]

with open('dict.csv', 'a', newline='') as csvfile:
    fieldnames = ['composer', 'symbol']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'composer': composerName, 'symbol': symbol})

chdir('../catalogues')
with open(fileName, 'w') as f:
    for i in catalogueLine:
        f.write(i + "\n")

chdir('../listens')
f = open(symbol + 'listened.txt', 'w+')
f.close()

print("Done!")