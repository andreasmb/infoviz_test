
import streamlit as st
import numpy as np
import pandas as pd
import plost


st.write("# Visualization explorations and tests")

# my_range = np.arange(0, 100, 8)
# st.write(my_range)

music = pd.read_csv("music.csv")
st.dataframe(music)

plost.line_chart(
    data=music,
    x={
        "field": 'year',
        "title": "Custom x-axis title",  # <-- Custom y-axis title
        "type": "temporal"
    },
    y={
        "field": ['rock', 'jazz'],
        "title": "Custom y-axis title",  # <-- Custom y-axis title
        "type": "quantitative"
    }
)


testframe = pd.DataFrame(
     np.random.randn(5, 3),
     columns=['jazz', 'rock', 'techno'])

st.dataframe(testframe) 

plost.line_chart(
    data=testframe,
    x='jazz',
    y='rock')
    # x='my x-axis title',
    # y='this is the y-axis')


# Can't figure out how to make a dataframe with np.arange or np.random

# years = np.arange(1950, 1970, 1)

# d = {'col1': np.arange(1950, 1970, 1), 'col2': [3, 4]}

# st.write(d)
# df = pd.DataFrame(data=d)

#############

# df2 = pd.DataFrame(
#     np.array([[1950, 1951, 1952], [4, 5, 6], [7, 8, 9]]),
#     columns=['year', 'blues', 'showtunes'])

# st.dataframe(df2)


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

chart_data = pd.DataFrame(
     np.random.randn(10, 7),
     columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])



st.line_chart(chart_data)




col1, col2 = st.columns(2)

with col1:
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with col2:
    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
