from setuptools import setup
import nltk

# NLTK Nessesary
nltk.download('punkt')
nltk.download('wordnet')

setup(
    name="TextGenTensorflow",
    author="Artificial",
    maintainer="Copy",
    url="https://github.com/ArtificialOSS/TextGenTensorflow",
    description="Text generation with tensorflow",
    version="1.0.0-dev",
    install_requires=[
        "setuptools>=45.0",
        "h5py>=3.8.0",
        "keras>=2.12.0",
        "numpy>=1.23.5",
        "tensorflow>=2.12.0",
        "nltk>=3.8.1"
    ],
)