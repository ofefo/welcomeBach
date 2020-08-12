#DOWNLOAD NEW CATALOGUES FROM A WIKIPEDIA PAGE
from bs4 import BeautifulSoup
import urllib.request
from os import chdir

chdir('../catalogues')

fileName = input('What is your filename? (E.g.: \"bwv.txt\")\n ')
url = input('What is your url?\n ')
opusOrNot = input('Is it by Opus? (y/n)\n ')
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
    
with open(fileName, 'w') as f:
    for i in catalogueLine:
        f.write(i + "\n")

chdir('../listens')
f = open(fileName.replace('.txt', '') + 'listened.txt', 'w+')
f.close()

print("Done!")
