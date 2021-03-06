#########
#Imports#
#########

from bs4 import BeautifulSoup
import os,__main__

###########
#Variables#
###########
steps_removed = []

exludes = ['<h4>','<ul>','</li>','</div>','</ol>','</ul>','</img></br></li>', '<ol>', '<li>',
           '</br></li>','<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">',
           '<div class="markdown-body">',
           '<div class="wiki-footer gollum-markdown-content boxed-group" id="wiki-footer">',
           '<div class="boxed-group-inner wiki-auxiliary-content markdown-body">',
           '<hr/>', '~<br/>', '<h5>', '\n', '']


files = ['Part-1-(Homebrew).html',
         'Part-2-(9.2.0-Downgrade).html',
         'Part-3-(RedNAND).html',
         'Part-4-(2.1.0-Downgrade).html',
         'Part-5-(arm9loaderhax).html',
         'DSiWare-Downgrade.html']

#Functions
def html_file_list():
    global links
    links = []
    for item in os.listdir(__main__.html_directory):
        if item.endswith(".html"):
            links.append(item)
        else:
            pass

#Main

def parse(html_file):
    del steps_removed[:]
    print 'Cleared steps_removed'
    soup = BeautifulSoup(open(__main__.html_directory+html_file), "lxml")
    print 'BS4'
    steps = str(soup.find("div", class_="wiki-body gollum-markdown-content instapaper_body"))
    print 'Soup Find'
    step = steps.split("\n")
    print 'Split'

    for item in step:
        if item not in exludes:
            steps_removed.append(item.strip('\n'))
            print item+'\n'
        else:
            pass