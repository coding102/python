# Create a script that counts how many times a word appears using a dictionary
# Punctuation marks should be removed
# Exclude irrelavent/uninterested words: THE, TO, IF, OR, AH
# Input should be a text file
import sys
import io
import fileupload
from IPython.display import display
from matplotlib import pyplot as plt
import numpy as np
import wordcloud
#!pip install wordcloud
#!pip install fileupload
#!pip install ipywidgets
#!jupyter nbextension install - -py - -user fileupload
#!jupyter nbextension enable - -py fileupload


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    # LEARNER CODE START HERE
    frequencies = {}
    sentence = file_contents.split()

    for word in sentence:
        if word in uninteresting_words:
            pass
        else:
            for letter in word:
                if letter in punctuations:
                    letter.replace(punctuations, "")
            if word not in frequencies.keys():
                frequencies[word] = 0
            else:
                frequencies[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
