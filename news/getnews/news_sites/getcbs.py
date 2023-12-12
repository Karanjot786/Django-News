from gettext import find
from ...models import Headline
from bs4 import BeautifulSoup
import requests

def getcbs(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def business(per_site):
    
    bus_html = requests.get('https://www.inshorts.com/en/read/business').text
    soup = BeautifulSoup(bus_html, 'lxml')

    bus_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    bus_count = 0
    for art in bus_list:
        if bus_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            bus_count += 1

def sports(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/sports').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1

def indin(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/national').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1



def world(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/world').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1



def politics(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/politics').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def technology(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/technology').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def startup(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/startup').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def entertainment(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/entertainment').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1


def miscellaneous(per_site):
    
    cbs_html = requests.get('https://inshorts.com/en/read/miscellaneous').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            headline = Headline()
            headline.leaning = 'left'
            headline.title = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"}).text
            image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
            headline.img = image_div.find('div')['style'].split('url(')[1][:-2]
            # headline.url = art.find(class_='read-more').find('a').get('href')
            headline.content = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"}).text
            headline.date = art.find(clas='date').text

            headline.save()
            cbs_count += 1












