"""
-----------------------------------------------------------------------------
Filter out the images (remove duplicate urls and text images)  
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
"""

from tqdm import tqdm
import numpy as np
import pandas as pd
from collections import OrderedDict
from shutil import copyfile

import craft
import cv2

from input_output import *

input_datapath = 'dataset/all/'
input_filename = 'images_source_info.xlsx'

# read images source info file
df_image_source = pd.read_excel(''.join([input_datapath, input_filename]))
dict_image_source = OrderedDict()
for key in df_image_source.keys():
    dict_image_source[key] = df_image_source[key].tolist()
dict_image_source['unique_url'] = [False]*len(df_image_source['url_info'])
dict_image_source['text_present'] = [False]*len(df_image_source['url_info'])

# find unique urls
url_info = [url.split("//")[-1] for url in df_image_source['url_info']]
unique_url_info, ids = np.unique(url_info, return_index=True)
for i in ids:
    dict_image_source['unique_url'][i] = True

# find images which has some text
for i in tqdm(ids):
    try:
        img = cv2.imread(''.join([input_datapath, dict_image_source['image_filename'][i]]))
        # run the text detector
        bboxes, polys, heatmap = craft.detect_text(img)
        if len(bboxes):
            dict_image_source['text_present'][i] = True
    except:# assuming unable to read the image or has some problem (so remove those)
        dict_image_source['text_present'][i] = True
        
    # save a local copy
    pd.DataFrame.from_dict(dict_image_source).to_excel(''.join([input_datapath, 'unique_', input_filename]), index=False)

# remove duplicate urls and images contains text 
df_image_source = pd.DataFrame.from_dict(dict_image_source)
df_image_source = df_image_source[(df_image_source['unique_url']==True) & (df_image_source['text_present']==False)]
df_image_source.to_excel(''.join([input_datapath, 'unique_', input_filename]), index=False)

# save filtered images in a separate directory
output_datapath = create_folder(''.join([input_datapath, 'clean/']))
for img in df_image_source['image_filename']:
    src_filemame = ''.join([input_datapath, img])
    dst_filename = ''.join([output_datapath, img])
    copyfile(src_filemame, dst_filename)
df_image_source.to_excel(''.join([output_datapath, 'unique_', input_filename]), index=False)   


# save filtered text-images in a separate directory
df_image_source = pd.DataFrame.from_dict(dict_image_source)
df_image_source = df_image_source[(df_image_source['unique_url']==True) & (df_image_source['text_present']==True)]
output_datapath = create_folder(''.join([input_datapath, 'text_images/']))
for img in df_image_source['image_filename']:
    src_filemame = ''.join([input_datapath, img])
    dst_filename = ''.join([output_datapath, img])
    copyfile(src_filemame, dst_filename)
df_image_source.to_excel(''.join([output_datapath, 'text_images_', input_filename]), index=False)    




        
    