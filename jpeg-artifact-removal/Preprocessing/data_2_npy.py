import os
from glob import glob
from tqdm import tqdm

import numpy as np
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

dir_path= '../Data/train/'

low_quality_images= sorted(glob(dir_path+'low_quality/*'))
high_quality_images= sorted(glob(dir_path+'high_quality/*'))

# Set some parameters
im_width = 256
im_height = 256

X_train = np.zeros((len(low_quality_images), im_height, im_width, 3), dtype=np.uint)
y_train = np.zeros((len(high_quality_images), im_height, im_width, 3), dtype=np.uint)

for i, low_quality_path in tqdm(enumerate(low_quality_images), total=len(low_quality_images)):
    
    low_img= load_img(low_quality_path, target_size= (im_width, im_height, 3))
    low_img= img_to_array(low_img)
    low_img= low_img/255.
    X_train[i] = low_img
    
    high_quality_path= high_quality_images[i]
    high_img= load_img(high_quality_path, target_size= (im_width, im_height, 3))
    high_img= img_to_array(high_img)
    high_img= high_img/255.
    y_train[i] = high_img

np.save('../Data/train/low_quality.npy', X_train)
np.save('../Data/train/high_quality.npy', y_train)
