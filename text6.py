# 명언 수집  (Do it 파이썬 생활프로그래밍) 초판 2020: 218페이지
#import os , re, usecsv
import os , re
import urllib.request as ur

from bs4 import BeautifulSoup as bs
url = 'http://quotes.toscrape.com/' 
html = ur.urlopen(url)
soup=bs(html.read(), 'html.parser')

#명언 하나만 가져오기
print(soup.find_all('span')[0].text)

# quote 명언 하나만 가져오기
print(soup.find_all('div',{"class":"quote"})[0])

# 해당 페이지의 명언 모두 출력하기
for i in soup.find_all('div',{"class":"quote"}):
	print(i.text)