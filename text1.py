import os, re

samptxt = 'tttt kindly test  culy (park, 2008)  lovely kkkkkkkkkk  (lee, 2019)   ssssssss  (kim, 2021)'

result = re.findall ( r'\([A-Za-z가-힣]+, \d+\)', samptxt )
print(result)

result1 = re.findall(r'\w+ly', samptxt)
print(result1)