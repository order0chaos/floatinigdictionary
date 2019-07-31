from bs4 import BeautifulSoup
import requests

source = requests.get('https://pythontutor.com')

soup = BeautifulSoup(source, 'lxml')
print(source.prettify())
# search = soup.find('div', class_='BNeawe deIvCb AP7Wnd')
# print(search.text)
# pronounce = soup.find('div', class_="BNeawe tAd8D AP7Wnd")
# print(pronounce.text)
# grammar = soup.find('div', class_="BNeawe s3v9rd AP7Wnd").span
# print(grammar.text)
# c = 0
# for definition in soup.find('div', class_="BNeawe s3v9rd AP7Wnd"):
#     if not c==0:
#         print(" ", c, ":", definition.text)
#     c+=1
# for article in soup.find_all('div'):
    
#     print(article.prettify())

# print(article.h2.a.text)
# match = soup.find('div', class_='vmod')
# meaning = match.text
# print(meaning)