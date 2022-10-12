import os, re, codecs


f = codecs.open('stockinfo.txt', 'r', encoding = 'utf-8')
stockinfo = f.read()

print(stockinfo)


# line = re.findall(r'Monica:.+', script01)
# print(line[:3])

# for item in line[:3]:
#     print(item)

# f.close()

# f = open('monica.txt', 'w', encoding ='utf-8')

# monica = ''

# for i in line:
#     monica += i + '\n'

# f.write(monica)
# f.close()   


