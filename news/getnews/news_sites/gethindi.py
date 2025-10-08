from gettext import find
from ...models import Headline
from bs4 import BeautifulSoup
import requests

def hindi_getcbs(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read').text
    soup = BeautifulSoup(cbs_html, 'lxml')

    cbs_list = soup.find_all('div',attrs={"class":"PmX01nT74iM8UNAIENsC"})

    cbs_count = 0
    for art in cbs_list:
        if cbs_count < per_site:
            try:
                headline = Headline()
                headline.leaning = 'left'
                
                # Get title with error handling
                title_element = art.find('span',attrs={"class":"ddVzQcwl2yPlFt4fteIE"})
                headline.title = title_element.text if title_element else "No title available"
                
                # Get image with error handling
                image_div = art.find('div', class_='r_CK6OaFsecGqhiNxLQR')
                if image_div and image_div.find('div'):
                    style_attr = image_div.find('div').get('style', '')
                    if 'url(' in style_attr:
                        headline.img = style_attr.split('url(')[1][:-2]
                    else:
                        headline.img = ""
                else:
                    headline.img = ""
                
                # Get content with error handling
                content_element = art.find('div',attrs={"class":"KkupEonoVHxNv4A_D7UG"})
                headline.content = content_element.text if content_element else "No content available"
                
                # Get date with error handling
                date_element = art.find(class_='date')
                headline.date = date_element.text if date_element else ""

                headline.save()
                cbs_count += 1
            except Exception as e:
                print(f"Error processing Hindi article: {e}")
                continue


def hindi_business(per_site):
    
    bus_html = requests.get('https://inshorts.com/hi/read/business').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            bus_count += 1

def hindi_sports(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/sports').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1

def hindi_indin(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/national').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1



def hindi_world(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/world').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1



def hindi_politics(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/politics').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1


def hindi_technology(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/technology').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1


def hindi_startup(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/startup').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1


def hindi_entertainment(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/entertainment').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1


def hindi_miscellaneous(per_site):
    
    cbs_html = requests.get('https://inshorts.com/hi/read/miscellaneous').text
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
            headline.date = art.find(class_='date').text

            headline.save()
            cbs_count += 1


