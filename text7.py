
import os , re
import urllib.request as ur

from bs4 import BeautifulSoup as bs

a = []    # 빈 리스트 생성

for i in range(3):
    line = []
    K=0              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        
        line.append(K)     # 안쪽 리스트에 0 추가
        K = K + 1
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가

print(a)
print ('\\2')
print (r'\1')
name = 'Kim'
age = 10
print ( '{0} was {1} years old when he wrote this book'.format(name, age) )
print ( '{} was {} years old when he wrote this book'.format(name, age) )
print ('{0:.4f} {1:.4f}'.format(1.0/3, 23))
print ( dir())

aa = 7
bb = 5
cc = aa & bb
print( 'cc = {}'.format(cc) )

dd = aa | bb
print( 'dd = {}'.format(dd) )

kk = input("숫자를 입력하세요")
print(kk)