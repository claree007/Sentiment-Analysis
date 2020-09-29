[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/claree007/Sentiment-Analysis/binder?urlpath=%2Fvoila%2Frender%2Finference.ipynb)

# Sentiment Analysis
Sentiment analysis on the Large Movie Review Dataset

<p>In this project, I perform sentiment analysis on a dataset of movie reviews, i.e. predict whether a reivew is positive or negative. I have used pre-trained word2vec embeddings from wikipedia2vec. </p>

Dataset: [https://ai.stanford.edu/~amaas/data/sentiment/](https://ai.stanford.edu/~amaas/data/sentiment/)

Pre-trained embeddings: [https://wikipedia2vec.github.io/wikipedia2vec/pretrained/](https://wikipedia2vec.github.io/wikipedia2vec/pretrained/)

## Sample Output

```
'The movie was long and left much to be desired.'
Prediction: Negative  Sentiment score: 1.94

'the action waS out of the world. And such details to the story line'
Prediction: Positive  Sentiment score: 4.47

'even with a star studded cast, the movie lacked in flair. A meaningless plot stretched over 2 hours'
Prediction: Negative  Sentiment score: 1.61
```

## Setup

1. <p><b>Run the requirements.txt for 64-bit python installation.</b> <br/> <code>py -m pip install -r requirements.txt</code><br/></p>
2. <p><b>Download the dataset and embeddings from the above links and uncompress them.</b></p>

3. <p><b>Run Sentiment Analysis.ipynb notebook to prepare the dataset, train the model and save it.</b><br/><code>jupyter notebook "Sentiment Analysis.ipynb"</code><br/><br/></p>
