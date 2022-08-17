from gettext import find
from ...models import Headline
from bs4 import BeautifulSoup
import requests

def hindi_getcbs(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def hindi_business(per_site):
    
    bus_html = requests.get('https://inshorts.com/hi/read/business').text
    soup = BeautifulSoup(bus_html, 'lxml')

    bus_list = soup.find_all(class_='news-card')

    bus_count = 0
    for art in bus_list:
        if bus_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            bus_count += 1

def hindi_sports(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/sports').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1

def hindi_indin(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/national').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1



def hindi_world(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/world').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1



def hindi_politics(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/politics').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def hindi_technology(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/technology').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def hindi_startup(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/startup').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def hindi_entertainment(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/entertainment').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def hindi_miscellaneous(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/miscellaneous').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all(class_='news-card')

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find(class_='news-card-title').find('a').text
            headline.img = art.find(class_='news-card-image')['style'].split("'")[1]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find(class_='news-card-content').find('div').text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


