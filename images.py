"""
-----------------------------------------------------------------------------
Download images from bing search (parallelly) using diff. key words
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
"""

from bing_image_downloader import downloader
from multiprocessing import Pool


def image_download_parallel(query):
    downloader.download(query, limit=10, timeout=30, verbose=False)

    
query = ['cat', 'dog', 'cow', 'lion', 'tiger']
# multiple queries in parallel 
if __name__ == '__main__':
    with Pool(len(query)) as p:
        p.map(image_download_parallel, query)