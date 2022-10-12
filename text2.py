import os, re, codecs


f = codecs.open('friendscript1.txt', 'r', encoding = 'utf-8')
script01 = f.read()

print(script01[:500])

line = re.findall(r'Monica:.+', script01)
print(line[:3])

for item in line[:3]:
    print(item)

f.close()

f = open('monica1.txt', 'w', encoding ='utf-8')

monica = ''

for i in line:
    monica += i + '\n'

f.write(monica)
f.close()   


