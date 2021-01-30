import os
import sys 
from PIL import Image
from glob import glob
from multiprocessing import Pool

def compressImage(image_file): 
    
    file_name= os.path.basename(image_file).split('.')[0]
    # open the image 
    picture = Image.open(image_file) 
      
    picture.save(os.path.join(base_save+file_name+'.jpeg'),  
                 "JPEG",  
                 optimize = True,  
                 quality = 70) 
    return

base_save= 'Data/train/low_quality/'
images= glob('Data/train/high_quality/*')

p= Pool(10)
p.map(compressImage, images)