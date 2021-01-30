import os
import sys 
from PIL import Image 

def compressImage(image_file, verbose = False): 
    
    file_name= os.path.basename(image_file).split('.')[0]
    # open the image 
    picture = Image.open(image_file) 
      
    picture.save(os.path.join(base_save+file_name+'.jpg'),  
                 "JPEG",  
                 optimize = True,  
                 quality = 10) 
    return

base_save= 'Data/train/low_quality/'
compressImage('Data/train/high_quality/im_1.bmp')