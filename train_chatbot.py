import numpy as np                                  #for numpy
from keras.models import Sequential                 #sequential model
from keras.layers import Dense, Activation, Dropout #layers
from keras.optimizers import SGD                    #optimization algorithm
import random                                       #random module
import nltk                                         #natural language toolkit
from nltk.stem import WordNetLemmatizer             #Lemmatization
lemmatizer = WordNetLemmatizer()                    #Lemmatization
import json                                         #json module
import pickle                                       #pickle module
intents_file = open('intents.json').read()
intents = json.loads(intents_file)


#Part 2: Preprocessing the Data
words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.']
for intent in intents['intents']:
    for pattern in intent['patterns']:
        #tokenize each word
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        #add documents in the corpus
        documents.append((word, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)