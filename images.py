"""
-----------------------------------------------------------------------------
Download images from bing search (parallelly) using diff. key words
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
"""

from bing_image_downloader import downloader
from multiprocessing import Pool


def image_download_parallel(query, num_images, save_path):
    downloader.download(
        query, 
        limit=num_images, 
        output_dir=save_path, 
        timeout=30, 
        verbose=False
    )

    
query = ['cat', 'dog', 'cow', 'lion', 'tiger']
num_images = 5
save_path = 'dataset/'
# multiple queries in parallel 
if __name__ == '__main__':
    with Pool(len(query)) as p:
        p.starmap(
            image_download_parallel, 
            [(q, num_images, save_path) for q in query]
        )