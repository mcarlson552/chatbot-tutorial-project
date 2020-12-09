import numpy as np                                  #for numpy
from keras.models import Sequential                 #sequential model
from keras.layers import Dense, Activation, Dropout #layers
from keras.optimizers import SGD                    #
import random
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
intents_file = open('intents.json').read()
intents = json.loads(intents_file)