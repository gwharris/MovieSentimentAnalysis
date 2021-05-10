# Movie Sentiment Analysis Project

## Contents
- [Contributors](#contributors)
- [Acknowledgements](#acknowledgements)
- [Abstract](#abstract)
- [Data Set](#data-set)

## Contributors
* [Graham Harris](https://github.com/gwharris)
* [Judy Zheng](https://github.com/IamJudyZ)
* [Christine Ma](https://github.com/christine-ma)
* [Jong Heon Han](https://github.com/hjh527)

## Acknowledgements
Final project for NYU's Spring 2021 undergraduate course CSCI-UA.0480 Natural Language Processing with Prof. Adam Meyers. Special thanks to Tin B. Luu for advising the team!

## Abstract
In this experiment, five different types of tokens were used to determine what components are necessary for sentiment analysis. Movie reviews from an IMDb data set containing 50,000 reviews were parsed into different tokens, which were then run through a model. By testing all of the tokens, casting to lowercase, removing punctuation, using adjectives only, and lemmatizing, the research team tested what parts of a given movie review are necessary for the sentiment to remain intact. 

Each tokenization method was run through a machine learning model to evaluate the accuracy of the system on a binary classification model (0 for neg- ative, 1 for positive). The team found that the trial containing all tokens per- formed the best, likely because each of the subsequent trials removed informa- tion important to determine sentiment, such as capitalization and punctuation. The adjectives-only trial performed the worst; since adjectives are not the only part of speech that contains sentiment, it is proposed that more than just one part of speech is necessary for sentiment analysis. 

All the tokenization methods performed under 90% accuracy, probably due to using a unigram model and data set error. The discovered accuracies lie in the 80-90% range as opposed to state of the art (XLNet as of the writing of this paper) at 96.21%.

## Data Set
The data set consists of [50,000 IMDb movie reviews](https://ai.stanford.edu/~amaas/data/sentiment/) (Stanford University) divided into a validation set, test set, and training set. 

The validation set contains 5,000 reviews with randomly selected sentiments (both positive and negative) from a corpus of 25,000 balanced data sentiments, the training set contains the 20,000 remaining reviews, and the test set contains 25,000 balanced reviews. Also included is a set of all 50,000 unlabeled balanced reviews.
