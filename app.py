# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('sakila.csv')

# Display data head and tail
st.title('Project 4')
st.subheader('Load our data:')
st.dataframe(df.head())
st.dataframe(df.tail())

# Display data shape and info
st.subheader('Data Shape:')
st.write(df.shape)

st.subheader('Data Info:')
st.write(df.info())

# Drop NaN values
df.dropna(inplace=True)

# Display updated data info
st.subheader('Updated Data Info:')
st.write(df.info())

# Descriptive statistics
st.subheader('Descriptive Statistics:')
st.write(df.describe())

# Display film_rental_rate statistics
st.subheader('Film Rental Rate Statistics:')
st.write("Mean:", df['film_rental_rate'].mean())
st.write("Median:", df['film_rental_rate'].median())

# Plot film_rental_rate density and bar chart
st.subheader('Film Rental Rate Analysis:')
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(df['film_rental_rate'], kde=True, ax=ax[0])
ax[0].set_title('Film Rental Rate Density')
ax[1].bar(df['film_rental_rate'].value_counts().index, df['film_rental_rate'].value_counts().values)
ax[1].set_ylabel('Number of Rentals')
ax[1].set_xlabel('Rate')
ax[1].set_title('Number of Rentals per Rate')
st.pyplot(fig)

# Plot rental gain return density and statistics
st.subheader('Rental Gain Return Analysis:')
df['rental_gain_return'] = df['film_rental_rate'] / df['film_replacement_cost'] * 100
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(df['rental_gain_return'], kde=True, ax=ax[0])
ax[0].set_title('Rental Gain Return Density')
ax[1].axvline(df['rental_gain_return'].mean().round(3), color='red', label='Mean')
ax[1].axvline(df['rental_gain_return'].median().round(3), color='green', label='Median')
sns.histplot(df['rental_gain_return'], kde=True, ax=ax[1])
ax[1].set_title('Rental Gain Return with Mean and Median')
ax[1].legend()
st.pyplot(fig)

# Display selected customer data
st.subheader('Selected Customer Data:')
selected_customers = df.loc[(df['customer_lastname'] == 'HANSEN') | (df['customer_lastname'] == 'HUNTER'), 'film_title'].unique()
st.write(selected_customers)

# Display film_replacement_cost max and corresponding film titles
st.subheader('Film Replacement Cost Analysis:')
max_replacement_cost = df['film_replacement_cost'].max()
st.write("Max Film Replacement Cost:", max_replacement_cost)
max_cost_titles = df.loc[df['film_replacement_cost'] == max_replacement_cost, 'film_title'].unique()
st.write("Titles with Max Replacement Cost:", max_cost_titles)

# Display data for PG and PG-13 films
st.subheader('PG and PG-13 Film Data:')
pg_pg13_data = df.loc[(df['film_rating'] == 'PG') | (df['film_rating'] == 'PG-13')]
st.dataframe(pg_pg13_data)
st.write("Number of PG and PG-13 films:", pg_pg13_data.shape[0])
