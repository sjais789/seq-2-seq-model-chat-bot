Created on Fri Jun  1 17:09:39 2018

@author: Shubham Jaiswal

import tensorflow as tf 


def modelinput():
    input=tf.placeholder(tf.int32,[None,None],name='Input')
    target=tf.placeholder(tf.int32,[None,None],name='Target')
    learning_rate=tf.placeholder(tf.float32,name='learning_rate')
    keep_probe=tf.placeholder(tf.float32,name='keepprobe')
    return input,target,learning_rate,keep_probe

