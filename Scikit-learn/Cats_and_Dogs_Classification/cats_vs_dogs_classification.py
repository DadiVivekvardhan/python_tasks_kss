import os
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import random
#import plotly.express as px
#import scipy as sp

#from scipy import ndimage
from shutil import copyfile
from tensorflow.keras.layers import Conv2D,Add,MaxPooling2D, Dense, BatchNormalization,Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class_names = ['Cat', 'Dog']
CAT_DIR = r"C:\Users\DELL\OneDrive\Documents\Python Tasks\Scikit-learn\Cats_and_Dogs_Classification\archive\PetImages\Cat"
DOG_DIR = r"C:\Users\DELL\OneDrive\Documents\Python Tasks\Scikit-learn\Cats_and_Dogs_Classification\archive\PetImages\Dog"

n_cats = len(os.listdir(CAT_DIR))
n_dogs = len(os.listdir(DOG_DIR))

n_images = [n_cats, n_dogs]

print("Number of Cat images:", n_cats)
print("Number of Dog images:", n_dogs)
print("Total images:", n_cats + n_dogs)

#px.pie(names=class_names, values=n_images)

DATASET_DIR = r"C:\Users\DELL\OneDrive\Documents\Python Tasks\Scikit-learn\Cats_and_Dogs_Classification\archive\PetImages"


"""**Great the data is perfectly balanced**

<a name="2-1"></a>
## create directories for training and validation
"""
BASE_DIR = r"C:\Users\DELL\OneDrive\Documents\Python Tasks\Scikit-learn\Cats_and_Dogs_Classification\cats_dogs_data"

TRAINING_DIR = os.path.join(BASE_DIR, "training")
VALIDATION_DIR = os.path.join(BASE_DIR, "validation")

TRAINING_CATS = os.path.join(TRAINING_DIR, "cats")
TRAINING_DOGS = os.path.join(TRAINING_DIR, "dogs")

VALIDATION_CATS = os.path.join(VALIDATION_DIR, "cats")
VALIDATION_DOGS = os.path.join(VALIDATION_DIR, "dogs")

os.makedirs(TRAINING_CATS, exist_ok=True)
os.makedirs(TRAINING_DOGS, exist_ok=True)
os.makedirs(VALIDATION_CATS, exist_ok=True)
os.makedirs(VALIDATION_DOGS, exist_ok=True)

print("Directories are ready!")


# Define whether to include test split or not
INCLUDE_TEST = False

print("Training cats:", len(os.listdir(TRAINING_CATS)))
print("Training dogs:", len(os.listdir(TRAINING_DOGS)))

print("Validation cats:", len(os.listdir(VALIDATION_CATS)))
print("Validation dogs:", len(os.listdir(VALIDATION_DOGS)))


"""**Now let's create  a function to split the   data**"""

def split_data(main_dir, training_dir, validation_dir,
               test_dir=None, include_test_split = True,
               split_size=0.9):
   
    files = []
    for file in os.listdir(main_dir):
        if  os.path.getsize(os.path.join(main_dir, file)): # check if the file's size isn't 0
            files.append(file) # appends file name to a list
    files = files[:1000]

    shuffled_files = random.sample(files,  len(files)) # shuffles the data
    split = int(split_size * len(shuffled_files)) #the training split casted into int for numeric rounding
    train = shuffled_files[:split] #training split
    split_valid_test = int(split + (len(shuffled_files)-split)/2)

    if include_test_split:
        validation = shuffled_files[split:split_valid_test] # validation split
        test = shuffled_files[split_valid_test:]
    else:
        validation = shuffled_files[split:]

    for element in train:
        copyfile(os.path.join(main_dir,  element), os.path.join(training_dir, element)) # copy files into training directory

    for element in validation:
        copyfile(os.path.join(main_dir,  element), os.path.join(validation_dir, element))# copy files into validation directory

    if include_test_split:
        for element in test:
            copyfile(os.path.join(main_dir,  element), os.path.join(test_dir, element)) # copy files into test directory
    print("Split sucessful!")

"""**Now let's call the function to create the  training/validation data**"""

split_data(
    CAT_DIR,
    TRAINING_CATS,
    VALIDATION_CATS,
    None,
    INCLUDE_TEST,
    0.9
)

split_data(
    DOG_DIR,
    TRAINING_DOGS,
    VALIDATION_DOGS,
    None,
    INCLUDE_TEST,
    0.9
)

"""**As a sanity check let's check the data directories**"""
print("Training cats:", len(os.listdir(TRAINING_CATS)))
print("Training dogs:", len(os.listdir(TRAINING_DOGS)))

print("Validation cats:", len(os.listdir(VALIDATION_CATS)))
print("Validation dogs:", len(os.listdir(VALIDATION_DOGS)))

"""<a name="2-2"></a>

## Create Generators
"""

train_gen = ImageDataGenerator(
        rescale=1./255)


validation_gen =  ImageDataGenerator(
        rescale=1./255.)

if INCLUDE_TEST:
    test_gen =  ImageDataGenerator(
            rescale=1./255.)

train_generator = train_gen.flow_from_directory(
    TRAINING_DIR,
    target_size=(150, 150),
    batch_size=64,
    class_mode='binary'
)

validation_generator = validation_gen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(150, 150),
    batch_size=64,
    class_mode='binary'
)   



if INCLUDE_TEST:
    test_generator = test_gen.flow_from_directory(
        VALIDATION_DIR,
        target_size=(150, 150),
        batch_size=64,
        class_mode='binary')

"""**Now let's make sure we got the correct data**"""

class_names = ['Cat', 'Dog']
def plot_data(generator, n_images):
    """
    Plots random data from dataset
    Args:
    generator: a generator instance
    n_images : number of images to plot
    """
    i = 1
    images, labels = generator.next()
    labels = labels.astype('int32')

    plt.figure(figsize=(14, 15))

    for image, label in zip(images, labels):
        plt.subplot(4, 3, i)
        plt.imshow(image)
        plt.title(class_names[label])
        plt.axis('off')
        i += 1
        if i == n_images:
            break

    plt.show()

plot_data(train_generator,7)

plot_data(validation_generator,7)

if INCLUDE_TEST:
    plot_data(test_generator, 10)

"""**Great, now that the data is ready let's train our model**

<a id="3"></a>
<h1 style='background:#FFD700;border:0; color:black;
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    transform: rotateX(10deg);
    '><center style='color: black;'>Model</center></h1>
    
# Model
"""
inputs = tf.keras.layers.Input(shape=(150, 150, 3))

x = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)

x = tf.keras.layers.Conv2D(64, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)

x = tf.keras.layers.Conv2D(128, (3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)

x = tf.keras.layers.GlobalAveragePooling2D()(x)

x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = Model(inputs=inputs, outputs=x)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

r = model.fit(
    train_generator,
    epochs=5,
    validation_data=validation_generator
)
"""<a id="4"></a>
<h1 style='background:#FFD700;border:0; color:black;
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    transform: rotateX(10deg);
    '><center style='color: black;'>Evaluation</center></h1>
    
# Evaluation

<a name="4-1"></a>

## Evaluate the model on the test set
"""

if INCLUDE_TEST:
    model.evaluate(test_generator)

"""<a name="4-2"></a>

## Visualize the predicitons
"""

def plot_prediction(generator, n_images):

    i = 0

    images, labels = generator.next()

    # Get model predictions
    preds = model.predict(images, verbose=0)

    # Convert probability to Cat(0) or Dog(1)
    predictions = (preds > 0.5).astype('int32').flatten()

    labels = labels.astype('int32')

    plt.figure(figsize=(14, 15))

    for image, label in zip(images, labels):

        plt.subplot(4, 3, i + 1)
        plt.imshow(image)

        # Correct prediction
        if predictions[i] == label:
            title_obj = plt.title(
                "Predicted: " + class_names[predictions[i]]
            )
            plt.setp(title_obj, color='g')

        # Wrong prediction
        else:
            title_obj = plt.title(
                "Predicted: " + class_names[predictions[i]]
            )
            plt.setp(title_obj, color='r')

        plt.axis('off')

        i += 1

        if i == n_images:
            break

    plt.show()
    
if INCLUDE_TEST:
    plot_prediction(test_generator, 10)

plot_prediction(validation_generator, 10)

"""<a name="4-3"></a>

## Visualize class activation maps
"""
"""
# Create a  model to visualize activation maps
gp_weights =  model.get_layer('dense').get_weights()[0]
activation_model = Model(model.inputs, outputs=(model.get_layer('conv2d_5').output, model.get_layer('dense_1').output))

# Use the model to make predictions on the test generator
images, _ = test_generator.next()
features, results = activation_model.predict(images)


def show_cam(image_index, features, results):
    Shows activation maps
    Args:
    image_index: index of image
    features: the extracted features
    results: model's predictions


    # takes the features of the chosen image
    features_for_img = features[image_index,:,:,:]

    # get the class with the highest output probability
    prediction = np.argmax(results[image_index])

    # get the gap weights at the predicted class
    class_activation_weights = gp_weights[:,prediction]

    # upsample the features to the image's original size (150 x 150)
    class_activation_features = sp.ndimage.zoom(features_for_img, (150/30, 150/30, 1), order=2)

    # compute the intensity of each feature in the CAM
    cam_output  = np.dot(class_activation_features,class_activation_weights)

    print('Predicted Class = ' +str(class_names[prediction])+ ', Probability = ' + str(results[image_index][prediction]))

    # show the upsampled image

    plt.imshow(images[image_index])

    # strongly classified (95% probability) images will be in green, else red
    if results[image_index][prediction]>0.95:
        cmap_str = 'Greens'
    else:
        cmap_str = 'Blues'

    # overlay the cam output
    plt.imshow(cam_output, cmap=cmap_str, alpha=0.5)

    # display the image
    plt.show()

#def show_maps(desired_class, num_maps):
    '''
    goes through the first 10,000 test images and generates Cam activation maps
    Args:
    desired_class: class to show the maps for
    num_maps: number of maps to be generated
    '''
    counter = 0
    # go through the first 10000 images
    for i in range(0,10000):
        # break if we already displayed the specified number of maps
        if counter == num_maps:
            break

        # images that match the class will be shown
        if np.argmax(results[i]) == desired_class:
            counter += 1
            show_cam(i,features, results)

#show_maps(desired_class=1, num_maps=5)

#show_maps(desired_class=0, num_maps=5)

"""

"""<a name="4-4"></a>
"""
## Visualize training process


results = pd.DataFrame(r.history)
results.tail()

plt.figure(figsize=(6, 4))
plt.plot(results['accuracy'], label='Training Accuracy')
plt.plot(results['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(results['loss'], label='Training Loss')
plt.plot(results['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


"""**Let's try using data augmentation**

<a id="5"></a>
<h1 style='background:#FFD700;border:0; color:black;
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    transform: rotateX(10deg);
    '><center style='color: black;'>Trying Data Augmentation </center></h1>

# Trying Data Augmentation
"""
"""
train_gen_aug = ImageDataGenerator(
        rescale=1./255,fill_mode='nearest',horizontal_flip=True,
        rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
)


validation_gen_aug =  ImageDataGenerator(
        rescale=1./255.)

train_generator = train_gen_aug.flow_from_directory(
        '/tmp/cats-v-dogs/training',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')
validation_generator = validation_gen_aug.flow_from_directory(
        '/tmp/cats-v-dogs/validation',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

inputs = tf.keras.layers.Input(shape=(150,150,3))
x =  tf.keras.layers.Conv2D(32, (3,3), activation='relu')(inputs)
x = tf.keras.layers.Conv2D(64, (3,3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2,2)(x)

x = tf.keras.layers.Conv2D(64, (3,3), activation='relu')(x)
x = tf.keras.layers.Conv2D(128, (3,3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2,2)(x)

x = tf.keras.layers.Conv2D(128, (3,3), activation='relu')(x)
x = tf.keras.layers.Conv2D(256, (3,3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(2,2)(x)


x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dense(2, activation='softmax')(x)

model_aug = Model(inputs=inputs, outputs=x)

model_aug.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics = ['accuracy'])

r = model_aug.fit(
        train_generator,
        epochs=10,#Training longer could yield better results
        validation_data=validation_generator)

results = pd.DataFrame(r.history)
results.tail()

fig = px.line(results,y=[results['accuracy'],results['val_accuracy']],template="seaborn",color_discrete_sequence=['#fad25a','red'])
fig.update_layout(
    title_font_color="#fad25a",
    xaxis=dict(color="#fad25a",title='Epochs'),
    yaxis=dict(color="#fad25a")
 )
fig.show()

fig = px.line(results,y=[results['loss'],results['val_loss']],template="seaborn",color_discrete_sequence=['#fad25a','red'])
fig.update_layout(
    title_font_color="#fad25a",
    xaxis=dict(color="#fad25a",title='Epochs'),
    yaxis=dict(color="#fad25a")
 )
fig.show()
"""
"""<a id="5"></a>
<h1 style='background:#FFD700;border:0; color:black;
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    transform: rotateX(10deg);
    '><center style='color: black;'>Conclusion </center></h1>

# Conclusion

**Using data augmentation with these hyper-parameters gave us worse results**


**We can Use [transfer learning](https://www.kaggle.com/code/fareselmenshawii/introdution-to-transfer-learning/edit/run/109466477) or a more complex architecture to solve this problem**

**We'll discuss these topics in later notebooks**

<a id="7"></a>
<h1 style='background:#FFD700;border:0; color:black;
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    transform: rotateX(10deg);
    '><center style='color: black;'>Thank You </center></h1>


    
# Thank You

**Thank you for taking your time and going through this notebook**

**Please let me know if you have any feedback**
"""
