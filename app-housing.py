import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Califonia Housing Data(1990) by Yuchen Chang')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price:', 0, 500001, 200000)

st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize = (10, 10))
df.median_house_value.hist(bins=30)
st.pyplot(fig)

location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

radio = st.radio('Choose income level', ('Low', 'Medium', 'High'))

df = df[df.price >= price_filter]

df = df[df.capital.isin(location_filter)]

if radio <= 2.5:
    st.write('Low')
else:
    if radio > 4.5:
        st.write('High')
    else:
        st.write('Medium')