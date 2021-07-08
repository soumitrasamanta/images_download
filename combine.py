"""
-----------------------------------------------------------------------------
Combine images from all the searched keys words  
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
"""

import numpy as np
import pandas as pd
from collections import OrderedDict
from shutil import copyfile

from input_output import *


# combine images from all queries
query = ['cat', 'dog', 'cow', 'lion', 'tiger']
output_datapath = create_folder('dataset/all/')
output_filename = 'images_source_info.xlsx'
decimal_place = 6
count_img = 1# global image count
dict_image_source = OrderedDict({
    'key_word': [], 
    'image_filename': [], 
    'url_info': []
})

for i, q in enumerate(query):
    input_datapath = ''.join(['dataset/', q.replace(' ', '_'), '/'])
    input_filename = ''.join([q.replace(' ', '_'), '_images_source_info.xlsx'])
    # read images source info file
    df_image_source = pd.read_excel(''.join([input_datapath, input_filename]))
    print('-'*70)
    print('#images with key word "{}" is: {}' 
          .format(q, len(df_image_source['image_filename'].tolist())))
    count_local_img = 0
    for img, url in zip(df_image_source['image_filename'].tolist(), df_image_source['url_info'].tolist()): 
        if url not in dict_image_source['url_info']:
            src_filemame = ''.join([input_datapath, img])
            dst_filename = ''.join([
                output_datapath, 
                'image', str(count_img).zfill(decimal_place), 
                '.jpg'
            ])
            copyfile(src_filemame, dst_filename)
            dict_image_source['key_word'].append(q)
            dict_image_source['url_info'].append(url)
            dict_image_source['image_filename'].append(dst_filename.split('/')[-1])
            count_img += 1
            count_local_img += 1
    print('#unique images with key word "{}" is: {}' 
          .format(q, count_local_img))

df_image_source = pd.DataFrame.from_dict(dict_image_source)
df_image_source.to_excel(
    ''.join([output_datapath, output_filename]), 
    index=False
)