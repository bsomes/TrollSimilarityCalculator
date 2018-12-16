# TrollSimilarityCalculator
CS410 Course Project

This is Brian Somes's submission for the CS 410 course project. 
The main script is troll_similarity.py, which takes a command line argument that is the suspected account's username and returns
the percentage of normal users who have less similar posts when compared to known Russian troll accounts than this user.

##Setup

This project is built in Python, and requires an installation of Python 3.6 or later. The Anaconda distribution is preferred.
The following packages also need to be installed:
 *sklearn
 *nltk
 *praw
 *numpy
 *scipy

After installation, run "nltk.download('punkt') in your python interpreter to download tokenizers and the Porter Stemmer.

Run the file with "python troll_similarity.py <username>" 

A video tutorial on how to run the script can be seen [here](https://youtu.be/JyyMUm5GRNI)
