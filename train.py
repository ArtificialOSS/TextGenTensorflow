import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN, Dense
from keras.preprocessing.text import Tokenizer
import json
import os
import numpy as np

# Check if the model exists
def CheckModel():
    cwd = os.getcwd()
    try:
        with open(cwd + filename, "r"):
            print("Model Exists")
        return True
    except Exception:
        print("Model Not Found")
        return False

doesModelExist = CheckModel()

# Hyperparameters
rnn_units = 64
batchsize = 32
embedding_dim = 300
epoches = 20

# Modelfile

filename = "cvtlai"
save_path = f"{os.getcwd()}\\{filename}"