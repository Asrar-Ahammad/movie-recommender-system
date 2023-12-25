# importing dependencies
import streamlit as st
import pickle as pk
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# recommend function
def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetching poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_posters


# Title 
st.title('Movie Recommender System')

# Importing pickel files
similarity = pk.load(open('Projects/movie_recommender_system/Programs/similarity.pkl', 'rb'))
movies_dict = pk.load(open('Projects/movie_recommender_system/Programs/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

selected_movie_names = st.selectbox(
    'Enter Movie you like',
    movies['title'].values
)

if st.button('Recommend'):
    st.header('These are the movies you may like :')
    names,poster = recomend(selected_movie_names)
    col1, col2, col3,col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])