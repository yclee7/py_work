import tensorflow as tf


hello = tf.constant('Hello Tensorflow World!!!')

sess = tf.Session()

print(sess.run(hello))
