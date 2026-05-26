import pandas as pd
import numpy as np
import ast
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------
# LOAD DATASETS
# --------------------------------

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# --------------------------------
# MERGE DATA
# --------------------------------

movies = movies.merge(credits, on='title')

# --------------------------------
# SELECT IMPORTANT COLUMNS
# --------------------------------

movies = movies[[
    'movie_id',
    'title',
    'overview',
    'genres',
    'keywords',
    'cast',
    'vote_average',
    'release_date'
]]

# --------------------------------
# CONVERT JSON COLUMNS
# --------------------------------

def convert(text):

    L = []

    for i in ast.literal_eval(text):
        L.append(i['name'])

    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# --------------------------------
# TOP CAST
# --------------------------------

def top_cast(text):

    L = []

    counter = 0

    for i in ast.literal_eval(text):

        if counter != 5:

            L.append(i['name'])
            counter += 1

        else:
            break

    return L

movies['cast'] = movies['cast'].apply(top_cast)

# --------------------------------
# CLEAN OVERVIEW
# --------------------------------

movies['overview'] = movies['overview'].fillna('')

movies['overview'] = movies['overview'].apply(
    lambda x: x.split()
)

# --------------------------------
# REMOVE SPACES
# --------------------------------

for feature in ['genres', 'keywords', 'cast']:

    movies[feature] = movies[feature].apply(
        lambda x: [i.replace(" ", "") for i in x]
    )

# --------------------------------
# CREATE TAGS
# --------------------------------

movies['tags'] = (
    movies['overview'] +
    movies['genres'] +
    movies['keywords'] +
    movies['cast']
)

# --------------------------------
# FINAL DATAFRAME
# --------------------------------

new_df = movies[[
    'movie_id',
    'title',
    'tags',
    'vote_average',
    'release_date',
    'genres'
]]

# --------------------------------
# CONVERT TAGS TO STRING
# --------------------------------

new_df['tags'] = new_df['tags'].apply(
    lambda x: " ".join(x)
)

new_df['tags'] = new_df['tags'].apply(
    lambda x: x.lower()
)

# --------------------------------
# TF-IDF VECTORIZATION
# --------------------------------

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = tfidf.fit_transform(
    new_df['tags']
).toarray()

# --------------------------------
# SIMILARITY
# --------------------------------

similarity = cosine_similarity(vectors)

# --------------------------------
# SAVE FILES
# --------------------------------

pickle.dump(
    new_df,
    open('movies.pkl', 'wb')
)

pickle.dump(
    similarity,
    open('similarity.pkl', 'wb')
)

print("✅ movies.pkl created")
print("✅ similarity.pkl created")