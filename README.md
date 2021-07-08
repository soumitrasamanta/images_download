# Image download based on different key words using a [bing image downloader](https://github.com/soumitrasamanta/bing_image_downloader.git).

# Overview

This repo contains three items:

- [images](images.py) - download images based on the key words
- [combine](combine.py) - combine images from all the searched keys words
- [clean](clean.py) - filter out the images (remove duplicate urls and text images) 

# Prerequisites
- python >= 3.7
- pandas
- [opencv](https://pypi.org/project/opencv-python/)
- [bing image downloader](https://github.com/soumitrasamanta/bing_image_downloader.git)
- [text detector from image](https://github.com/arj7192/CRAFT-pytorch)


# Usage:
Set your key words at [images.py](images.py#L17). 
```bash
python images.py
```

Combine all the images in one file (set your key words at [combine.py](combine.py#L18) and other options).
```bash
python combine.py
```

Filter out text images and duplicate urls (set paths and others at [clean.py](clean.py#L20)).
```bash
python clean.py
```
