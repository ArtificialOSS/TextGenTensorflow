import os
import random

import numpy as np
from nltk.tokenize import RegexpTokenizer

from keras.models import load_model
from nntrain import Train

# Filter out Tensorflow Warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

txtds = open(f'./data/1.artidata', "r", errors='replace').read() # The Dataset

# Parameters
charsize = 30000
training_size = txtds[:charsize]

# Tokenizer
tokenizer = RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(training_size.lower())
unique_tokens = np.unique(tokens)
unique_token_index = {token: id for id, token in enumerate(unique_tokens)} # give all unique tokens (words) a id

next_tokens = 15 # predict the next words oooohhh
inp_words = [] # train_x
next_words = [] # train_y

# feed the training data to the train x & y
for i in range(len(tokens) - next_tokens):
    inp_words.append(tokens[i:i + next_tokens])
    next_words.append(tokens[i + next_tokens])

# ACTUALL FEEDING THE DATA TO THE VARIABLES TRAIN_X & TRAIN_Y
train_x = np.zeros((len(inp_words), next_tokens, len(unique_tokens)), dtype=bool)
train_y = np.zeros((len(next_words), len(unique_tokens)), dtype=bool)

for i, words in enumerate(inp_words):
    for j, word in enumerate(words):
        train_x[i, j, unique_token_index[word]] = 1
    train_y[i, unique_token_index[next_words[i]]] = 1

# Trains the model
Train(next_tokens, unique_tokens, train_x, train_y, epochs=12, batch_size=128)

# Now we can load the model here again since it always train itself when loading
model = load_model("models/aflmtg.h5")

def predNextWord(inp : str, n_best):
    inp = inp.lower()
    train_x = np.zeros((1, next_tokens, len(unique_tokens)))
    for i, word in enumerate(inp.split()):
        train_x[0, i, unique_token_index[word]] = 1
    
    pred = model.predict(train_x, verbose=0)[0]
    return np.argpartition(pred, -n_best)[-n_best:]

def generateResponse(inp : str, txtlen : int, creativity = 5):
    word_seq = inp.split()
    current = 0
    for _ in range(txtlen):
        sub_seq = " ".join(tokenizer.tokenize(" ".join(word_seq).lower()))[current:current+next_tokens]

        try:
            choice = unique_tokens[random.choice(predNextWord(sub_seq, creativity))]
        except:
            choice = random.choice(unique_tokens)

        word_seq.append(choice)
        current += 1

    return " ".join(word_seq)

while True:
    try:
        msg = input(">>> ")
        print(generateResponse(msg, 120, 5))
    except KeyError as e:
        print("KeyError: " + str(e))