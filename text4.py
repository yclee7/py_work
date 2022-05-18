import os, re, codecs


f = codecs.open('friendscript1.txt', 'r', encoding = 'utf-8')
script01 = f.read()
#print(script01[:500])

character = re.compile(r'[A-Z][a-z]+:')
line = set(re.findall(character, script01))
#print(line[:3])
print(line)

line1 = list(line)

character1 = []

for ii in line1:
    character1 += [ii[:-1]]

print(character1)






# for item in line[:3]:
#     print(item)

f.close()



# f = open('monica.txt', 'w', encoding ='utf-8')
# monica = ''
# for i in line:
#     monica += i + '\n'

# f.write(monica)
# f.close()   


