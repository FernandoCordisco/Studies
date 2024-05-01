import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df_reviews = pd.read_csv ('Datasets/customer reviews.csv')
df_top100_books = pd.read_csv ('Datasets/Top-100 Trending Books.csv')


#Price Filter
price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()

max_price = st.sidebar.slider('Maximum Price', price_min, price_max, price_max)

df_books = df_top100_books[df_top100_books['book price'] <= max_price]

#Rating Filter

rating_max = df_books['rating'].max()
rating_min = df_books['rating'].min()

max_rating = st.sidebar.slider('Maximun Rating', rating_min, rating_max, rating_max)

df_books = df_books[df_books['rating'] <= max_rating]

#Front

df_books

fig = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)