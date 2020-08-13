import re
import nltk
import pickle
import numpy as np
import tensorflow as tf

# helper utilities
replacements = """aren't    are not
can't   cannot
couldn't    could not
didn't  did not
doesn't does not
don't   do not
hadn't  had not
hasn't  has not
haven't have not
he'd    he would
he'll   he will
he's    he is
i'd i would
i'll    i will
i'm i am
i've    i have
isn't   is not
it's    it is, it has
let's   let us
mustn't must not
shan't  shall not
she'd   she would
she'll  she will
she's   she is
shouldn't   should not
that's  that is
there's there is
they'd  they would
they'll they will
they're they are
they've they have
we'd    we would
we're   we are
we've   we have
weren't were not
what'll what will
what're what are
what's  what is
what've what have
where's where is
who'd   who would
who'll  who will
who're  who are
who's   who is
who've  who have
won't   will not
wouldn't    would not
you'd   you would
you'll  you will
you're  you are
you've  you have"""

# expand words with apostrophe
splitted = []
for r in replacements.split('\n'):
    splitted.append(re.split(r'\s', r, maxsplit=1))

# load stopwords
stopwords = []
with open('stopwords.txt', 'r') as f:
    stopwords = f.read().lower().split('\n')

def expand_sent(sent):
    for split in splitted:
        sent = re.sub(split[0], split[1], sent)
    return sent

def remove_stopwords(tokens):
    new_tokens = []
    for word in tokens:
        if word not in stopwords:
            new_tokens.append(word)
    return new_tokens

def clean_text(sent):
    sent = expand_sent(sent.lower())
    # removes 's eg: Amy's will become Amy
    sent = re.sub(r"'s", "", sent)
    # removes words joined together by hyphen
    sent = re.sub(r'(.*?)-(.*?)', r'\1 \2', sent)
    # removes puntuations, extra characters and html tages and text inside parentheses
    sent = re.sub(r'[\'"!@:.,?#*\n()]|(<.*?>)', " ", sent)
    # replaces 2 consecutive numbers with NUM token
#     sent = re.sub(r'\d+', " NUM ", sent)
    # removes more than 2 consecutive same characters with just 2
    sent = re.sub(r'(.)\1+', r'\1\1', sent)
    # removes 2 or more spaces
    sent = re.sub(r' +', " ", sent)
    return sent.strip()

# define the pipeline
def predict_sentiment(text):
    text = remove_stopwords(nltk.word_tokenize(clean_text(text)))
    X = np.zeros([1, max_len], dtype=np.int32)
    for i, word in enumerate(text):
        X[0, i] = word2idx.get(word, 0)
    y_pred = model.predict(X)
    return y_pred

# load metadata
metadata = pickle.load(open("metadata.pickle", 'rb'))

vocab = metadata["vocab"]
word2idx = metadata["word2idx"]
pad_id = metadata["pad_id"]
unk_id = metadata["unk_id"]
max_len = metadata["max_len"]
vocab_size = len(vocab)

# load the model
model = tf.keras.models.load_model('model.h5')

print()
review = '> The acting was very good and the direction was even better.'
print(review)
print('Sentiment score:', predict_sentiment(review))
print()
print('Type reviews and wait for the score. Press q to quit...', '\n')

while True:
    review = input('> ')
    if review != 'q':
        print('Sentiment score:', predict_sentiment(review), '\n')
    else:
        break
