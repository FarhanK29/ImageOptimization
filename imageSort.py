import os
import PIL
import shutil
from PIL import Image

path = os.getcwd()
path = path.replace('ImageOptimization', 'ImagesForOptimization')


for file in os.listdir(path):
    path = os.getcwd()
    path = path.replace('ImageOptimization', 'ImagesForOptimization')

    endPath = os.getcwd()
    endPath = endPath.replace('ImageOptimization', 'OptimizedImages')


    path = path + "/" + file
    if(not('DS_Store' in file)):

        size = os.path.getsize(path)/1000
        img = PIL.Image.open(path)
        width, height = img.size

        
        condition1 = ((((300,250) == (width,height)) or ((728,90) == (width,height)) or ((160,600) == (width,height)) or ((300,600) == (width,height))and (size < 50)))
        condition2 = ((((1940,500) == (width,height)) or ((970,250) == (width,height)) or ((640,100) == (width,height)) or ((1242,375) == (width,height)) or ((600,500) == (width,height)) or ((1456,180) == (width,height))and (size<200)))

        if(condition1 or condition2):
            shutil.move(path, endPath)
print('Success!')


