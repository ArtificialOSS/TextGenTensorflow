# Text Generation Tensorflow Template

This repository is a template to create a Text Generation Artificial Inteligence with **Tensorflow**. This repository includes a pretrained model called `aflmtg.h5` inside the `models` folder and a dataset `/data/1.artidata`

This project is inspired from [**NeuralNine's** Text Generation AI - Next Word Prediction in Python](https://www.youtube.com/watch?v=tEV_Jtmx2cc) youtube video.

# Installation

using this template is easy:

```ps
$ git clone https://github.com/ArtificialOSS/TextGenTensorflow.git
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install nltk

$ python3 setup.py
```

or run `build.sh`

Then you can use the AI
```ps
$ python3 main.py
```

# Achiving the Best Results:

**Achiving perfect results requires high computing power (RAM)**

The bigger the `charsize` the better are the results but takes more time to train
```diff
+ charsize = 100000
- charsize = 30000
```
Lowering the `creativity=` parameter brings better results if the charsize is over `50000`
```diff
+ print(generateResponse(msg, 120, 3))
- print(generateResponse(msg, 120, 5))
```
The more epochs the more accurate and better is the model
```diff
+ Train(next_tokens, unique_tokens, train_x, train_y, epochs=30, batch_size=128)
- Train(next_tokens, unique_tokens, train_x, train_y, epochs=12, batch_size=128)
```

# Contribution

You're welcome to contribute to this template! open a pull request and do your stuff