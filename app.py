import streamlit as st
import pickle
import pandas as pd
from difflib import get_close_matches

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------
# LOAD DATA
# --------------------------------

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --------------------------------
# RECOMMEND FUNCTION
# --------------------------------

def recommend(movie_name, genre_filter=None):

    movie_name = movie_name.lower()

    all_titles = movies['title'].tolist()

    matched = get_close_matches(
        movie_name,
        all_titles,
        n=1,
        cutoff=0.5
    )

    if not matched:
        return []

    matched_title = matched[0]

    idx = movies[movies['title'] == matched_title].index[0]

    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommendations = []

    for i in movie_list:

        movie_data = movies.iloc[i[0]]

        title = movie_data.title

        rating = movie_data.vote_average

        year = str(movie_data.release_date)[:4]

        genres = movie_data.genres

        if genre_filter:
            if genre_filter not in genres:
                continue

        recommendations.append({
            'title': title,
            'rating': rating,
            'year': year,
            'genres': genres
        })

    return recommendations


# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("🎬 Movie Recommender")

st.sidebar.markdown("### Features")

st.sidebar.write("✅ AI Recommendation")
st.sidebar.write("✅ Genre Filtering")
st.sidebar.write("✅ Ratings")
st.sidebar.write("✅ Trending Movies")
st.sidebar.write("✅ Fast Search")

# --------------------------------
# MAIN TITLE
# --------------------------------

st.title("🎥 Advanced Movie Recommendation System")

st.markdown(
    "Find movies similar to your favorite movies using Machine Learning."
)

# --------------------------------
# TRENDING MOVIES
# --------------------------------

st.subheader("🔥 Top Trending Movies")

trending = movies.sort_values(
    by='vote_average',
    ascending=False
).head(10)

trend_cols = st.columns(5)

for idx, (_, row) in enumerate(trending.iterrows()):

    with trend_cols[idx % 5]:

        st.markdown(f"### 🎬 {row['title']}")
        st.write(f"⭐ Rating: {row['vote_average']}")
        st.write(f"📅 {str(row['release_date'])[:4]}")

# --------------------------------
# MOVIE SEARCH
# --------------------------------

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎞️ Select or Search Movie",
    movie_list
)

# --------------------------------
# GENRE FILTER
# --------------------------------

all_genres = set()

for genre_list in movies['genres']:

    if isinstance(genre_list, list):

        for g in genre_list:
            all_genres.add(g)

all_genres = sorted(list(all_genres))

selected_genre = st.selectbox(
    "🎭 Filter by Genre (Optional)",
    ['None'] + all_genres
)

# --------------------------------
# BUTTON
# --------------------------------

if st.button('Recommend Movies'):

    with st.spinner('Finding best movies for you...'):

        if selected_genre == 'None':
            selected_genre = None

        results = recommend(
            selected_movie,
            selected_genre
        )

        if not results:

            st.error("Movie not found")

        else:

            cols = st.columns(2)

            for index, movie in enumerate(results):

                with cols[index % 2]:

                    st.subheader(movie['title'])

                    st.write(f"⭐ Rating: {movie['rating']}")

                    st.write(f"📅 Year: {movie['year']}")

                    st.write(
                        "🎭 Genres: " +
                        ", ".join(movie['genres'])
                    )

                    st.markdown("---")

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.markdown(
    "Made with ❤️ using Python, Streamlit, and Machine Learning"
)