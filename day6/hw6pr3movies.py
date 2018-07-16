## Import all of the libraries and data that we will need.
import nltk
import textblob
from nltk.corpus import names  # see the note on installing corpora, above
from nltk.corpus import opinion_lexicon
from nltk.corpus import movie_reviews
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import random
import math

from sklearn.feature_extraction import DictVectorizer
import sklearn
import sklearn.tree
from sklearn.metrics import confusion_matrix

from datamuse import datamuse
import itertools
import string
api = datamuse.Datamuse()

def get_list(dictionary):
    rel_words = []
    for d in dictionary:
        w = d['word']
        rel_words.append(w)
    return rel_words

def get_antonym(key_word):
    try:
        antonym = get_list(api.words(rel_ant = key_word,max = 1))[0]
    except IndexError:
        antonym = key_word
    return antonym

def clear_not_ambiguity(TB):
    for sentence in TB.sentences:
        sentence_ind = TB.sentences.index(sentence)
        word_list = sentence.split(" ")
        for word in word_list:
            if word == 'not':
                w_ind = word_list.index(word)
                ind = w_ind+1
                found_punc = False
                list_ant = []

                while found_punc == False:
                    key_word = word_list[ind]
                    antonym = get_antonym(key_word)
                    list_ant.append(antonym)
                    ind+=1
                    if key_word in string.punctuation:
                        found_punc = True

                new_words = word_list[0:w_ind] + list_ant + word_list[ind:len(word_list)]
                text_blob_sentence = textblob.TextBlob(' '.join(new_words)).sentences[0]
                TB.sentences[sentence_ind]=text_blob_sentence
    return TB


#####################
#
## Problem 4: Movie Review Sentiment starter code...
#
#####################

# a boolean to turn on/off the movie-review-sentiment portion of the code...
RUN_MOVIEREVIEW_CLASSIFIER = True
if RUN_MOVIEREVIEW_CLASSIFIER == True:

    ## Read all of the opinion words in from the nltk corpus.
    #
    pos=list(opinion_lexicon.words('positive-words.txt'))
    neg=list(opinion_lexicon.words('negative-words.txt'))

    ## Store them as a set (it'll make our feature extractor faster).
    #
    pos_set = set(pos)
    neg_set = set(neg)



    ## Read all of the fileids in from the nltk corpus and shuffle them.
    #
    pos_ids = [(fileid, "pos") for fileid in movie_reviews.fileids('pos')[:20]]
    neg_ids = [(fileid, "neg") for fileid in movie_reviews.fileids('neg')[:20]]
    labeled_fileids = pos_ids + neg_ids

    ## Here, we "seed" the random number generator with 0 so that we'll all
    ## get the same split, which will make it easier to compare results.
    random.seed(0)   # we'll use the seed for reproduceability...
    random.shuffle(labeled_fileids)



    ## Define the feature function
    #  Problem 4's central challenge is to modify this to improve your classifier's performance...
    #
    def opinion_features(fileid):
        """ starter feature engineering for movie reviews... """
        # many features are counts!
        positive_count=0
        negative_count=0
        for word in movie_reviews.words(fileid):
            if word in pos_set:
                positive_count += 1
            elif word in neg_set:
                negative_count += 1
        #Here's some sentiment analysis stuff
        sid = SentimentIntensityAnalyzer()

        # Note:  movie_reviews.raw(fileid) is the whole review!
        # create a TextBlob with
        rawtext = movie_reviews.raw(fileid)
        TB_amb = textblob.TextBlob( rawtext )
        TB = clear_not_ambiguity(TB_amb)
        # now, you can use TB.words and TB.sentences...
        total_sub = 0 #initializing subjectivity
        total_pol = 0 #initializing polarity
        total_pos = 0
        total_neg = 0
        total_neu = 0
        total_compound = 0
        for sentence in TB.sentences:
            total_sub += sentence.sentiment.polarity
            total_pol += sentence.sentiment.polarity
            ss = sid.polarity_scores(str(sentence))
            total_pos += ss['pos']
            total_neg += ss['neg']
            total_compound += ss['compound']
            total_neu += ss['neu']

        avg_sub = total_sub/len(TB.sentences)
        avg_pol = total_pol/len(TB.sentences)
        avg_pos = total_pos/len(TB.sentences)
        avg_neg = total_neg/len(TB.sentences)
        avg_compound = total_compound/len(TB.sentences)
        avg_neu = total_neu/len(TB.sentences)

        # here is the dictionary of features...
        features = {}   # could also use a default dictionary!

        # features['positive'] = positive_count
        # features['negative_count'] = negative_count
        # features['avg_pol'] = avg_pol
        features['avg_sub'] = avg_sub
        features['avg_neg'] = avg_neg
        features['avg_pos'] = avg_pos
        features['avg_compound'] = avg_compound
        features['avg_neu'] = avg_neu
        # try:
        #     features['ratio'] = negative_count/positive_count
        # except ZeroDivisionError:
        #     features['ratio'] = 1000
        # try:
        #     features['ratio'] =avg_neg/avg_pos
        # except ZeroDivisionError:
        #     features['ratio'] = 1000
        return features


    #
    ## Ideas for improving this!
    #
    # count both positive and negative words...
    # is the ABSOUTE count what matters?
    #
    # other ideas:
    #
    # feature ideas from the TextBlob library:
    #   * part-of-speech, average sentence length, sentiment score, subjectivity...
    # feature ideas from TextBlob or NLTK (or just Python):
    # average word length
    # number of parentheses in review
    # number of certain punctuation marks in review
    # number of words in review
    # words near or next-to positive or negative words: "not excellent" ?
    # uniqueness
    #
    # many others are possible...


    ## Extract features for all of the movie reviews
    #
    print("Creating features for all reviews...", end="", flush=True)
    features = [opinion_features(fileid) for (fileid, opinion) in labeled_fileids]
    labels = [opinion for (fileid, opinion) in labeled_fileids]
    fileids = [fileid for (fileid, opinion) in labeled_fileids]
    print(" ... feature-creation done.", flush=True)


    ## Change the dictionary of features into an array
    #
    print("Transforming from dictionaries of features to vectors...", end="", flush=True)
    v = DictVectorizer(sparse=False)
    X = v.fit_transform(features)
    print(" ... vectors completed.", flush=True)

    ## Split the data into train, devtest, and test

    X_test = X[:5,:]
    Y_test = labels[:5]
    fileids_test = fileids[:5]

    X_devtest = X[5:10,:]
    Y_devtest = labels[5:10]
    fileids_devtest = fileids[1:2]

    X_train = X[10:20,:]
    Y_train = labels[10:20]
    fileids_train = fileids[10:20]

    ## Train the decision tree classifier - perhaps try others or add parameters
    #
    dt = sklearn.tree.DecisionTreeClassifier()
    dt.fit(X_train,Y_train)

    ## Evaluate on the devtest set; report the accuracy and also
    ## show the confusion matrix.
    #
    print("Score on devtest set: ", dt.score(X_devtest, Y_devtest))
    Y_guess = dt.predict(X_devtest)
    CM = confusion_matrix(Y_guess, Y_devtest)
    print("Confusion Matrix:\n", CM)

    ## Get a list of errors to examine more closely.
    #
    errors = []

    for i in range(len(fileids_devtest)):
        this_fileid = fileids_devtest[i]
        this_features = X_devtest[i:i+1,:]
        this_label = Y_devtest[i]
        guess = dt.predict(this_features)[0]
        if guess != this_label:
            errors.append((this_label, guess, this_fileid))

    PRINT_ERRORS = False
    if PRINT_ERRORS == True:
        num_to_print = 15    # #15 is L.A. Confidential
        count = 0

        for actual, predicted, fileid in errors:
            print("Actual: ", actual, "Predicted: ", predicted, "fileid:", fileid)
            count += 1
            if count > num_to_print: break

    PRINT_REVIEW = False
    if PRINT_REVIEW == True:
        print("Printing the review with fileid", fileid)
        text = movie_reviews.raw(fileid)
        print(text)

    ## Finally, score on the test set:
    print("Score on test set: ", dt.score(X_test, Y_test))


    #
    # ## Reflections/Analysis
    #
    # Include a short summary of
    #   (a) how well your final set of features did!
    #   (b) what other features you tried and which ones seemed to
    #       help the most/least
    #
