import streamlit as st
import pandas as pd
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter

nlp = spacy.load("en_core_web_lg")

st.title('Plot Matching Movie Recommender')
st.write('Welcome! This app works in two ways...')
st.write('1. Submit appropriate genres and plot keywords to find the  movie you are looking for.')
st.write('2. Submit appropriate genres and plot keywords to find movies you\'ll find interesting.')
st.write('')
st.write('')
st.write('Here is an example of an appropriate entry...')
st.write('Genres: Comedy Drama')
st.write('Keywords: wedding holiday trouble')
st.write('')
st.write('')
st.write('Please allow up to 3 minutes for predictions.')
st.write('')

df = pd.read_csv('../data/genre_groups/x_final_df.csv')

st.write('Enter Genres Here:')
genre = st.text_input('', key="Genre")

if genre == True:
    genres = []
    for g in genre.split(' '):
        genres.append(g)

    if len(genres) == 1:
        df = df.loc[df[genres[0]] == 1, :]
    if len(genres) == 2:
        df = df.loc[(df[genres[0]] == 1) & (df[genres[1]] == 1), :]
    if len(genres) == 3:
        df = df.loc[(df[genres[0]] == 1) & (df[genres[1]] == 1) & (df[genres[2]] == 1), :]



st.write('Enter Movie Keywords Here:')
entry = st.text_input('', key="Keywords")

def recommend_me(entry, genre):
    keywords = [words for words in df['user_plot_keywords']]
    scores = [(nlp(entry).similarity(nlp(word))) for word in keywords]

    hrefs = [f'imdb.com/title/{ref}' for ref in df['imdb_id']]

    df['urls'] = hrefs
    df['similarity'] = scores

    return df[['title', 'similarity', 'urls']].sort_values(by='similarity', ascending=False).head(10)

st.write(recommend_me(entry, genre))
