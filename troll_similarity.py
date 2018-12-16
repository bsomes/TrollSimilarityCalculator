import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import stats
import string
import suspect_retrieval
import numpy as np
import os
import csv
import argparse


_stemmer = nltk.stem.porter.PorterStemmer()


def get_user_comments(name):
    r = suspect_retrieval.get_instance()
    submissions = np.array([submission.title for submission in r.redditor(name).submissions.top()])
    return submissions


def stem(tokens):
    return [_stemmer.stem(token) for token in tokens]


def tokenize(text):
    return stem(nltk.word_tokenize(text.translate(string.punctuation)))


def get_vectorizer(training_set):
    return TfidfVectorizer(tokenizer=tokenize,
                            max_df=30000.0,
                            ngram_range=(1, 2),
                            sublinear_tf=True).fit(training_set)


def get_troll_titles():
    return pd.read_csv(os.path.normpath('./suspicious_accounts/data/submissions.csv')).title.values


def get_normal_titles():
    users = []
    titles = []
    with open(os.path.normpath('./normal_submission_titles_new.csv'), 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) == 0:
                pass
            elif len(row) < 2:
                users.append("")
                titles.append(row[0])
            else:
                users.append(row[0])
                titles.append(row[1])
    return np.array(users), np.array(titles)


def group_titles(users, titles):
    grouped = {}
    for index, user in enumerate(users):
        if user in grouped:
            grouped[user].append(titles[index])
        else:
            grouped[user] = [titles[index]]
    return grouped


def get_vectors(model, titles):
    return model.transform(titles)


def user_similarity(user_vectors, troll_vectors):
    return (user_vectors * troll_vectors.T).A.mean()


def random_user_similarity(model, grouped_data, troll_data):
    random_similarities = []
    for subs in grouped_data.values():
        submission_vectors = get_vectors(model, subs)
        random_similarities.append(user_similarity(submission_vectors, troll_data))
    return random_similarities


def user_troll_percentile(name):
    troll_data = get_troll_titles()
    users, normal_data = get_normal_titles()
    training_data = np.concatenate((troll_data, normal_data))
    grouped = group_titles(users, normal_data)
    model = get_vectorizer(training_data)
    troll_vectors = get_vectors(model, troll_data)
    user_comments = get_user_comments(name)
    if len(user_comments) == 0:
        print('User Has No Submissions!')
        return 0.0
    user_vectors = get_vectors(model, user_comments)
    normal_similarities = random_user_similarity(model, grouped, troll_vectors)
    similarity = user_similarity(user_vectors, troll_vectors)
    return stats.percentileofscore(normal_similarities, similarity)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take a redditor\'s username' +
     'and return the percent of normal users that are less similar to known trolls than the given user')
    parser.add_argument('username', type=str, help='the username (without the leading /u/) of the suspect account')
    args = parser.parse_args()
    print('Percentage of normal users whose recent submissions are less similar than known Russian trolls are is:')
    print(user_troll_percentile(args.username))