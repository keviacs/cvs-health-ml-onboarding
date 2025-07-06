# -*- coding: utf-8 -*-
# """Fashion MNIST Dataset

import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels),(test_images,test_labels) = fashion_mnist.load_data()
#train images set 60,000 images
#10 thousand set of images to verify how the model performs
#label indicates the class type of clothing with a number
#it uses a number to avoid bias, facilitate the use in different languages and computers deal better with numbers

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),#input shape 28 by 28 represent the size of an image
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10,activation=tf.nn.softmax)# output layer, last layer is 10 represent the number of items of clothing in the Dataset

])

#The NN will act like filter which will 28 by 28 set of pixels and will output 1 out of 10 values
#128 represent the number of functions with parameters inside
#when the pixel of the image are feded one by one the combination of all the functions will output the correct value
#The computer will need to get the parameters in each function to get a result
#It will extend to the rest of the items and once it's done it must be able to reconize items
#Activation functions
#relu located on the line of 128 activation functions
#RELU Rectified linear unit
#RELU returns a value if it's rgeater than 0
#Softmax picks the biggest number in a set
#Softmax in the ouput every item has a probability of been the item
# Softmax sets the biggest as 1 and set the rest to 0 to facilitate the identification
#

model.compile(optimizer=tf.keras.optimizers.Adam(),
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
#The neural networ will be initialized with random values
#The loss funtion will measure how good or bad the results were
#The optimizer will generate new parameters for the functions to see if it can improve

###Training of the model

model.fit(train_images,train_labels,epochs=5)
#The Test_images and test_labels can be used to check the perfomance as the model hasn't seen the images
#We can pass those images and lables to the evaluate method
test_loss, test_acc = model.evaluate(test_images, test_labels)

###to get predictions
#predictions = model.predict(my_images)
#my_images is a personal dataset not previously loaded.