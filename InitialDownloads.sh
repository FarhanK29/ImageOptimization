#!/bin/bash
#Initial downloads

cd ~/Desktop
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade Pillow
pip3 install pillow optimize-images
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
brew install optipng

mkdir ImagesForOptimization
mkdir OptimizedImages



