import os
import PIL
import shutil
from PIL import Image

path = os.getcwd()
path = path.replace('ImageOptimization', 'OptimizedImages')

name = input(f"Enter the product name: ")
asin = input(f"Enter the ASIN: ")
for file in os.listdir(path):
    path = os.getcwd()
    path = path.replace('ImageOptimization', 'OptimizedImages')

    path = path + "/" + file

    if(not('DS_Store' in file)):
        file_name, file_extension = os.path.splitext(path)

        img = PIL.Image.open(path)
        width, height = img.size
        resolution = (f"{width}x{height}")

        os.rename(path, path.replace(file, f"{name}_{asin}_{resolution}{file_extension}"))
        print('Success!')




print('All Files Renamed!')
