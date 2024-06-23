from sklearn.neighbors import NearestNeighbors
import pandas as pd
import streamlit as st
import numpy as np


st.header("Cellphone Recommender System")

model: NearestNeighbors = pd.read_pickle(open("artifacts/model.pkl", "rb"))
phone_names = pd.read_pickle(open("artifacts/phone_names.pkl", "rb"))
final_rating = pd.read_pickle(open("artifacts/final_rating.pkl", "rb"))
user_phone_matrix = pd.read_pickle(open("artifacts/user_phone_matrix.pkl", "rb"))


def fetch_poster(suggestion) -> tuple[list, list]:
    phone_name = []
    ids_index = []
    poster_url = []
    price_list = []

    for book_id in suggestion:
        phone_name.append(user_phone_matrix.index[book_id])

    for name in phone_name[0]:
        ids = np.where(final_rating["title"] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]["image"]
        price = final_rating.iloc[idx]["price"]
        poster_url.append(url)
        price_list.append(price)

    return (poster_url, price_list)


def recommend_book(phone_name) -> tuple[list, list, list]:
    phones_list = []
    phone_id = np.where(user_phone_matrix.index == phone_name)[0][0]
    (distance, suggestion) = model.kneighbors(
        user_phone_matrix.iloc[phone_id, :].values.reshape(1, -1),
        n_neighbors=6,
    )

    (poster_url, price_list) = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        phones = user_phone_matrix.index[suggestion[i]]
        for j in phones:
            phones_list.append(j)
    return phones_list, poster_url, price_list


selected_books = st.selectbox("Type or select a book from the dropdown", phone_names)

if st.button("Show Recommendation"):
    recommended_books, poster_url, price_list = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
        st.text(f"Price: {price_list[1]} $$")
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
        st.text(f"Price: {price_list[2]} $$")
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
        st.text(f"Price: {price_list[3]} $$")
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
        st.text(f"Price: {price_list[4]} $$")
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
        st.text(f"Price: {price_list[5]} $$")
