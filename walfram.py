import streamlit as st
import requests

# Define your Wolfram Alpha app ID
WOLFRAM_APP_ID = 'GWA72H-LYA2A5LG4V'

# Streamlit app title
st.title("Wolfram Alpha Telegram Bot")

# Input box for user query
query = st.text_input("Enter your query")

# Button to submit the query
if st.button("Submit"):
    # Make a request to the Wolfram Alpha API
    url = f'http://api.wolframalpha.com/v1/result?appid={WOLFRAM_APP_ID}&i={query}'
    response = requests.get(url)
    result = response.text

    # Display the result
    st.write(result)
