import requests
from bs4 import BeautifulSoup

#Begin Scraping
req = requests.get('http://www.examplewebsite.com')
soup = BeautifulSoup(req.text, "lxml")

#Find all div tags with class entry-content
body = soup.body
for div in body.find_all('div', class_='entry-content'):
        #Log output and remove \n & \t then encode for txt output in term
        print(div.text.replace('\n', '').replace('\t', '').encode('utf-8'))
