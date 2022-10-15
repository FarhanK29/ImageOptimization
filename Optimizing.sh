#!/bin/bash
#Optimizing The Files


cd ~/Desktop/ImageOptimization
python3 imageSort.py
cd ~/Desktop/ImagesForOptimization
optipng *.png
optimize-images ./

cd ~/Desktop/ImageOptimization
python3 fileTransfer.py

