#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import nltk
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.title("Sentiment Analysis")
st.header("Real Time Sentiment Analysis using NLTK")
st.write("To analyze feelings in real-time, we need to request input from the user and then "
         "analyze user feelings given by him/her as input. So for this real-time sentiment "
         "analysis task using Python, I will be using the NLTK library in Python which is a "
         "very useful tool for all the tasks of natural language processing. So let’s import "
         "the NLTK library and start with sentiment analysis:")
st.code("from nltk.sentiment.vader import SentimentIntensityAnalyzer\n"
        "import nltk\n"
        "nltk.download('vader_lexicon')\n")

st.write("So, I will be using the SentimentIntensityAnalyzer() class provided by the NLTK library in Python. "
         "Now let’s take a user input and have a look at the sentiment score:")

st.code("user_input = input(""Write a Review: "")\n"
        "sid = SentimentIntensityAnalyzer() \n"
        "score = sid.polarity_scores(user_input)\n"
        "print(score)\n")

st.code("Write a Review: great \n"
        "{'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.6249}")

st.write("So the sentiments score looks like a dictionary with keys as ‘neg’, ‘neu’, ‘pos’, ‘compound’. "
         "The above output says that the sentiment of the user is 100% positive. So we can use an if-else statement "
         "by passing a condition that if the value of the key(neg) is not 0.0 then the sentiment is negative"
         " and otherwise it’s positive. So here is the complete Python code for real-time sentiment analysis:")

st.code("user_input = input(""Write a Review:\n "
        "sid = SentimentIntensityAnalyzer()\n"
        "score = sid.polarity_scores(user_input)\n"
        "if score[""neg""] != 0:\n"
        "   print(""Negative"")\n"
        "else:\n"
        "   print(""Positive"")\n")
st.success("You did it")

st.subheader("Try it yourself:")

user_input = st.text_input("Write a Review: ")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.subheader("Result")
    st.balloons()
    st.write("Neutral")
elif score["neg"] != 0:
    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.subheader("Result")
    st.balloons()
    st.write("The sentiment is Negative")
elif score["pos"] != 0:
    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.subheader("Result")
    st.balloons()
    st.write("The sentiment is Positive")




