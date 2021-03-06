from sys import argv
from os import chdir, system
from collections import OrderedDict
import csv, argparse, random, urllib.request, datetime, re

catalogue = {}
with open('dict.csv', newline='') as f:
    catalogue = dict(filter(None, csv.reader(f)))

keys = list(catalogue.keys())
keys.sort()

parser = argparse.ArgumentParser(description='welcomeBach: Your daily dose of counterpoint')
parser.add_argument('-v', help='Increase/decrease verbosity (default = 3)', type=int, default=3)
parser.add_argument('-r', help='Relisten to the last piece', action='store_true', default=False)
parser.add_argument('-c', choices=keys, help='Choose the composer you want to listen to', type=str, default='Bach')
parser.add_argument('-d', help='Download a new catalogue', action='store_true', default=False)
parser.add_argument('-m', help='Run with mpv', action='store_true', default=False)
args = parser.parse_args()

def videoFinder(n, composer, piece):
    query = urllib.parse.quote(composer + ' ' + piece)
    url = "https://www.youtube.com/results?search_query=" + query
    html = urllib.request.urlopen(url).read().decode('utf-8')
    pattern = re.compile('videoId":"(\w{11})"')
    matches = []
    for vid in re.findall(pattern, html):
        v = 'https://www.youtube.com/watch?v=' + vid
        matches.append(v)
    links = list(OrderedDict.fromkeys(matches))
    link_list = [links[i] for i in range(n)]

    return link_list


def main():

    if not args.d:

        #if no argument is passed, print 3 links as default
        number = args.v

        #if no argument is passed, Bach is the desired composer
        composer = args.c
        composer = composer.title()

        start = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
        end = datetime.datetime.utcnow()
        diff = abs((end - start).days)
        random.seed(diff)

        chdir('../catalogues')
        txtName = str(catalogue[composer])

        #choose today's opus
        with open(txtName) as f:
            opus = f.readlines()
            count = len(opus)
        n = random.randint(0, (count - 1))
        piece = opus[n]

        #if passed with argv -r, for "relisten", get the last item from the listened list
        #else, check if it has already been heard, if so, choose another pice
        chdir('../listens')
        listened = str(catalogue[composer] + '_listens')
        if args.r == True:
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
        if not args.m:

            return print("\n".join(videoFinder(number, composer, piece)))
        else:
            link_list = videoFinder(number, composer, piece)
            numbered_list = ["[{}] ".format(i+1) for i in range(number)]
            numbered_links = [x + y for x,y in zip(numbered_list, link_list)]
            print("\n".join(numbered_links))
            selection = int(input("\nPlease select a link: "))

            return system('setsid -f mpv {}'.format(link_list[selection-1]))
    else:
       system('python3 catalogue_dl.py')


if __name__ == '__main__':
    main()
