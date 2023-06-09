import streamlit as st
import requests
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="WALFRAMALPHA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6159-U.N.V RAVITEJA"]
st.title("WALFRAMALPHA")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)


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
