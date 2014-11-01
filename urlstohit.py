from bs4 import BeautifulSoup
import urllib2
import re
from yoamisafe.models import Incident
import django

django.setup()

url = "http://www.newhavencrimelog.org"
htmltext = urllib2.urlopen(url).read()
soup = BeautifulSoup(htmltext)

##Description coordinate date

links = []

dates = []

data = {}

counter = 0

for link in soup.findAll('table')[2].find_all('a'):
    links.append(url + link.get("href"))

###
## From murder to reckless endangerement data
###
def add_incident(latitude, longitude, date, description):
    i = Incident.objects.get_or_create(latitude=latitude, longitude=longitude, date=date, description=description)[0]
    return i

for link in range(0, 75):

    coordinates = []

    page_html = urllib2.urlopen(links[link]).read()
    new_soup = BeautifulSoup(page_html)

    text = new_soup.find_all('script')

    temp = re.findall('([+-]?\d+\.?\d+)\s*,\s*([+-]?\d+\.?\d+)', str(text))

    for x in temp:
        if '.' not in x[0] or '.' not in x[1]:
            continue
        else:
            coordinates.append((float(x[0]),float(x[1])))

    for date in new_soup.findAll('span', {'class': 'listing_label'}):
        if(date.text=="date:"):
            dates.append(str(date.next_sibling).strip())
         #print date.text, date.next_sibling



    description = new_soup.findAll('span', {"class": "title_val"})[1].text
    #print description

    for point in range(0, len(coordinates)):
        data[counter] = {"longitude": coordinates[point][0], "latitude": coordinates[point][1], "date": dates[point], "description": description}
        counter += 1

    for key in data.keys():
        print data[key]['longitude']
        print data[key]['latitude']
        print data[key]['date']
        print data[key]['description']
        add_incident(data[key]['latitude'], data[key]['longitude'], data[key]['date'], data[key]['description'])


    print "====================================="
