import tensorflow as tf
from Keras.models import Sequential
from Keras.layers import Embedding, SimpleRNN, Dense
from Keras.Processing.text import Tokenizer
import json
import os
import numpy as np

doesModelExist = False

# Hyperparameters
rnn_units = 64
batch_size = 32
embedding_dmm = 300
epoches = 20

# Modelfile

filename = "cvtlai"
save_path = f"{os.getcwd()}/models/{filename}"

# Check if the model exists
def CheckModel():
    cwd = os.getcwd()
    try:
        with open(cwd + "/model/" + filename, "r") as json_data:
            print("Model Exists")
        return True
    except FileNotFoundError:
        print("Model Not Found")
        return False