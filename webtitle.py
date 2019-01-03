from urllib import urlopen

from BeautifulSoup import BeautifulSoup

import re
def gettitle(url):
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()

    # Grab everything that lies between the title tags using a REGEX
    patFinderTitle = re.compile('')


    soup2 = BeautifulSoup(webpage)

    #print soup2.findAll("title")

    titleSoup = soup2.findAll("title")

    descSoup = soup2.findAll("p")
    titleSoup = str(titleSoup).strip('[<title>')
    titleSoup = titleSoup.strip('</title>]')
    titleSoup = re.sub("&#(\d+);", lambda m: chr(int(m.group(1))), titleSoup)
    print titleSoup
    return titleSoup 
