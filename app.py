import streamlit as st
import pickle
import pandas as pd
import os

st.markdown(
    """
    <style>
    .stApp {
        background-color: #2B547E;
    }
    .stButton > button {
        color: white;
        background-color: #4CAF50;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton > button:hover {
        background-color: #006A4E;
        color:white;
    }
    .stSelectbox:hover {
        cursor: pointer;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #040720;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Check current working directory
st.write(os.getcwd())

# Load the data
movies = pickle.load(open("movies_list.pkl", 'rb' ))
similarity = pickle.load(open("similarity.pkl", 'rb' ))

movies_list = movies['title'].values

st.header("Movie Recommender System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    for i in distance[1:6]:  # Skip the first movie since it is the selected movie itself
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button('Show Recommend'):
    recommended_movies = recommend(selectvalue)
    
    # Added a subheader for the recommendations section
    st.subheader("Recommended Movies:")  # New line to add a subheader
    
    # Loop through each recommended movie and display it vertically
    for movie in recommended_movies:  # New loop to iterate through recommended movies
        st.write(movie)  # New line to display each movie vertically

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>Developed by Ather Ahmed</p>
    </div>
    """,
    unsafe_allow_html=True
)