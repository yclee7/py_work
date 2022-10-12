import os, re

cpath = os.getcwd()
print( cpath )

f = open('a.txt', 'w')
f.write("I am a boy. You are a Girl")
f.close()

clist = os.listdir()
print( clist )

f = open('a.txt', 'r')
a = f.read()
print(a)
f.close()

