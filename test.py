import tensorflow as tf

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])


print("Hello World")
print(5)
print(3.14)

print('{:3} '.format(0), end='')
print('{:3} '.format(126), end='')

print("############################")

def new_func():
    print(4*4)
    print("한글")
    print('한글'*4)

new_func()

#print(tf.reduce_sum(tf.random.normal([1000, 1000])))

plt.show()
