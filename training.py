import numpy as np
import keras
import tensorflow as tf
from tensorflow.keras import optimizers
from tensorflow.keras import metrics
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense,Dropout, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
from keras import regularizers
import itertools
import os
import random
import shutil
import glob
import warnings
import matplotlib.pyplot as plt
import string
from tensorflow.python.ops.gen_array_ops import pad
warnings.simplefilter(action='ignore', category=FutureWarning)

#Enabling GPU
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
print("Num GPU's Available:", len(physical_devices))
print(physical_devices)

#Image Plotting Function
def plotImages(img_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip(img_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

#Defining Classes For DataSet
labels = [i for i in string.ascii_uppercase]
eps = 20
label_classes = ['0']
for i in labels:
    label_classes.append(i)


#Directory For DataSet
train_path = 'data/train'
test_path = 'data/test'
valid_path = 'data/valid'


#Generating Batches From The Data
train_batches = ImageDataGenerator(rescale=1/255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True) \
    .flow_from_directory(directory=train_path, target_size=(224, 224), classes=label_classes, batch_size=10, color_mode='grayscale')

valid_batches = ImageDataGenerator(rescale=1/255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True) \
    .flow_from_directory(directory=valid_path, target_size=(224, 224), classes=label_classes, batch_size=10, color_mode='grayscale')

test_batches = ImageDataGenerator(rescale=1/255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True) \
    .flow_from_directory(directory=test_path, target_size=(224, 224), classes=label_classes, batch_size=10, color_mode='grayscale', shuffle=False)

#Getting Images For Plotting
img, labels = next(train_batches)

#Plotting Images
plotImages(img.squeeze())
print(labels)

#Initializing VGG16 Model
vgg16_model = tf.keras.applications.vgg16.VGG16()


#Changing Output Layers according to labels
new_model = Sequential()
for layer in vgg16_model.layers[:-1]:
  new_model.add(layer)
new_model.add(Dense(units=27, activation='softmax'))
new_model.summary()

#Changing Input Layer for Black & White Images
model = Sequential()
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', input_shape=(224,224,1), padding='same'))
for layer in model.layers:
    layer.name = 'block1_conv1'
for layer in new_model.layers[1:]:
    model.add(layer)
    
#Summary of newly created model
model.summary()


#Compiling Model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

#Training The Model
model.fit(x=train_batches, validation_data=valid_batches, epochs = eps, verbose=1)

#Saving The Model
if os.path.isfile('model/translator-updated-bw-vgg16.h5') is False:
    model.save('model/translator-updated-bw-vgg16.h5')

hist = model.history.history
#Plotting Loss Graph
loss_train = hist['loss']
loss_val = hist['val_loss']
epochs = range(1,eps+1)
plt.plot(epochs, loss_train, 'g', label='Training loss')
plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

#Plotting Accuracy Graph
acc_train = hist['accuracy']
acc_val = hist['val_accuracy']
epochs = range(1,eps+1)
plt.plot(epochs, acc_train, 'g', label='Training Accuracy')
plt.plot(epochs, acc_val, 'b', label='validation Accuracy')
plt.title('Training and Validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


#Predicting the Test Images
pred = model.predict(x=test_batches, verbose=1)
test_batches.classes

#Plotting Confusion Matrix
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt

cm = confusion_matrix(y_true=test_batches.classes, y_pred=np.argmax(pred, axis=-1))
test_batches.class_indices

#Labels For Confusion Matrix
cm_plot_labels = ['0','A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Confusion Matrix Plotting Function
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure(figsize=(20, 20))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

#Plotting Confusion Matrix
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')

