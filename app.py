import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index =movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]# this is the array of distances
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_list = pickle.load(open('movies.pickle','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    #("Email", "Home phone", "Mobile phone"),
    movies['title'].values )

#st.button("Reset", type="primary")
if st.button("Recommend"):
    # recommend naam ka ek function bna jo ki baki ke kaam kr rha hai
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


