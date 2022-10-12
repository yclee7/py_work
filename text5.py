from lib2to3.pgen2.pgen import DFAState
import os, re, codecs
import pandas as pd

data = {'name' : ['Mark', 'Jane', 'Chris', 'Ryan'],
         'age' : [33, 32, 44, 41],
         'score' : [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)

print("============ df ==================")
print(df)
print("==================================")

print("============ sum =================")
print(df.sum())
print("==================================")

print("============= min  ===============")
print(df.mean())
print("==================================")

print("=============df.age ==============")
print(df.age)
print("==================================")

print("=============df[agg]  ============")
print(df['age'])
print("==================================")


df1 = pd.read_csv('apt.csv', encoding = 'cp949')

print(len(df1))

print(df1.head())

print(df1.면적 > 130 )
print(df1[df1.면적 > 160] )



# f = codecs.open('friendscript1.txt', 'r', encoding = 'utf-8')
# script01 = f.read()
# #print(script01[:500])

# character = re.compile(r'[A-Z][a-z]+:')
# line = set(re.findall(character, script01))
# #print(line[:3])
# print(line)

# line1 = list(line)

# character1 = []

# for ii in line1:
#     character1 += [ii[:-1]]

# print(character1)






# for item in line[:3]:
#     print(item)

# f.close()



# f = open('monica.txt', 'w', encoding ='utf-8')
# monica = ''
# for i in line:
#     monica += i + '\n'

# f.write(monica)
# f.close()   


