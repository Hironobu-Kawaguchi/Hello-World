import tensorflow as tf
#from tensorflow.python.client import device_lib

def main():
    print("Hello TensorFlow")
    print("tf.__version__", tf.__version__)
#    print(device_lib.list_local_devices())

    c = tf.constant(3)
    with tf.Session() as sess:
        print()
        print("sess.run", sess.run(c))

if __name__ == '__main__':
    main()