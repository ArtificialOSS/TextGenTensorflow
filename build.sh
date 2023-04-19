#!/bin/bash

echo Building Tensorflow-Template...
sudo apt install python3 python3-pip git

sudo git clone https://github.com/ArtificialOSS/TextGenTensorflow.git
sudo pip install --upgrade pip
sudo pip install tensorflow
sudo pip install nltk

python3 setup.py
echo Finished