#!/bin/bash

echo Building Tensorflow-Template...
sudo apt install python3 python3-pip git

sudo git clone https://github.com/ArtificialOSS/TensorflowTemplate.git
sudo pip install --upgrade pip
sudo pip install tensorflow

echo Training the bot
python3 train.py
python3 model.py
echo Finished