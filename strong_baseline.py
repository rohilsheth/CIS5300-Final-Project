import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import sklearn
import sklearn.metrics as metrics
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
from numpy import dot
from numpy.linalg import norm

files = ['530finalprojectdata/530datasetV2_dev.csv', '530finalprojectdata/530datasetV2_test.csv', '530finalprojectdata/530datasetV2_train_sample.csv']

def clean_data(data):
  data = data.rename({"Unnamed: 0": "id"},axis=1)
  data['Lyrics'] = data.Lyrics.apply(lambda x : x.replace("&apos;","'"))
  data['Lyrics'] = data.Lyrics.apply(lambda x: x.lower())
  data['Lyrics'] = data.Lyrics.apply(lambda x: x.replace("<br>", " "))
  return data

def tokenize_lyrics(data):
  song_docs = [TaggedDocument(doc.split(' '), [i]) for i, doc in enumerate(data.Lyrics)]
  return song_docs

def train_model(song_docs, data):
  model = Doc2Vec(vector_size=50, min_count=1, epochs = 1)
  # build vocab
  model.build_vocab(song_docs)
  #train model
  model.train(song_docs, total_examples=model.corpus_count, epochs=model.epochs)
  song2vec = [model.infer_vector((data['Lyrics'][i].split(' '))) for i in range(0,len(data))]
  dtv= np.array(song2vec).tolist()
  data['song2vec'] = dtv
  return model, data

def load_model():
  model = Doc2Vec.load("530finalprojectdata/dtv_model")
  return model

def infer_attr_vec(model):
  female_attr = ['girl', 'hers', 'her', 'aunt', 'daughter', 'sister', 'female', 'mother', 'she', 'grandmother', 'woman']
  male_attr = ['brother', 'grandfather', 'his', 'son', 'father', 'man', 'male', 'uncle', 'he', 'him', 'boy']

  female_vec = model.infer_vector(female_attr)
  male_vec = model.infer_vector(male_attr)
  return (female_vec, male_vec)

def run_strong_baseline():
  data = pd.read_csv(files[2])
  test_data = pd.read_csv('530finalprojectdata/clean_test_data.csv')
  song_docs = [TaggedDocument(doc.split(' '), [i]) for i, doc in enumerate(data.Lyrics)]

  model, data = train_model(song_docs, data)
  song2vec = [model.infer_vector((test_data['Lyrics'][i].split(' '))) for i in range(0,len(test_data))]
  test_data['d2v'] = np.array(song2vec).tolist()

  (female_vec, male_vec) = infer_attr_vec(model)
  test_data['female_sim'] = test_data.d2v.apply(lambda x: dot(x,female_vec)/(norm(x)*norm(female_vec)))
  test_data['male_sim'] = test_data.d2v.apply(lambda x: dot(x,male_vec)/(norm(x)*norm(male_vec)))
  test_data['sexist'] = test_data.apply(lambda x: (abs(x['female_sim'] - x['male_sim']) > 0.05) + 0, axis=1)
  return list(test_data['sexist'])

def main():
  y_preds = run_strong_baseline()
  print(y_preds)
  return y_preds 

if __name__ == "__main__":
    main()