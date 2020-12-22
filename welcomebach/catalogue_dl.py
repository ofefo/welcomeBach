"""
Catalogue Downloader
Generate new catalogues from wikipedia pages
"""
from bs4 import BeautifulSoup
from os import chdir
import urllib.request, csv, re

composerName = input('What is the composer last name?\n ')
fileName = input('What is your filename? (E.g.: \"bwv.txt\")\n ')
symbol = fileName
haveSymbol = int(input('Is it organized by symbol, opus or neither? (symbol=1; opus=2; neither=3)\n '))
url = input('What is your url?\n ')
listOrTable = int(input('Is it a list or a table? (list=1; table=2)\n '))

if listOrTable == 2:
    if haveSymbol == 1 or haveSymbol == 2:
        colNumber = int(input('What is the index of the column in which the work number is located?\n '))-1
        colName = int(input('What is the index of the column in which the work name is located?\n '))-1
    else:
        colName = int(input('What is the index of the column in which the work name is located?\n '))-1
else:
    pass

html = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
data = []

def has_no_class_and_no_id(tag):
    return not tag.has_attr('class') and not tag.has_attr('id')

def get_from_list():
    catalogue = []
    for heading in soup.find_all('span', {'class':"mw-headline"}):
        uls = heading.find_all_next('ul')
        for ul in uls:
            for li in ul.find_all('li'):
                catalogue.append(li.get_text())
        break
    chdir('../catalogues')
    with open(fileName, 'w') as f:
        for i in catalogue:
            f.write(i + "\n")
    
    return catalogue 

def find_tables():
    if soup.find_all('table', {'class': re.compile('(.*wikitable.*)')}) is not None:
        tables = soup.find_all('table', {'class': re.compile('(.*wikitable.*)')})
    else:
        tables = soup.find_all('table')

    return tables

def get_from_table(tables):
    catalogue = []
    opusName = []
    opusNumber = []
    
    for table in tables:
        if table is not None:
            body = table.find('tbody')
            if body == None:
                rows = table.find_all('tr')            
            else:
                rows = body.find_all('tr')
        else:
            break

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
        
    for i in data:
        if len(i) > 0:
            opusName.append(i[colName])
        else:
            pass
        
    for i in data:
        if haveSymbol == 1 and len(i) > 0:
            opusNumber.append(fileName.replace('.txt', ' ').replace('\"', '').upper() + i[colNumber] + ' ')
            catalogue = [x + y for x,y in zip(opusNumber, opusName)]
        elif haveSymbol == 2 and len(i) > 0:
            opusNumber.append('Op. ' + i[colNumber] + ' ')
            catalogue = [x + y for x,y in zip(opusNumber, opusName)]
        else:
            catalogue = opusName

    chdir('../catalogues')
    with open(fileName, 'w') as f:
        for i in catalogue:
            f.write(i + "\n")

    return catalogue

#Add the composer name to the csv dictionary
with open('dict.csv', 'a', newline='') as csvfile:
    fieldnames = ['composer', 'symbol']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'composer': composerName, 'symbol': symbol})

if listOrTable == 1:
    get_from_list()
elif listOrTable == 2:
    get_from_table(find_tables())
else:
    print("Error: select '1' or '2'")

chdir('../listens')
f = open(symbol + '_listens', 'w+')
f.close()

print("\nDone!")
