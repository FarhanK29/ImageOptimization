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
        shutil.move(path, endPath)
print('All Files Transferred!')


