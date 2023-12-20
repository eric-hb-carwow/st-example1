import streamlit as st
import requests

def fetch_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("Random Joke Generator")
    st.write("Click the button to generate a random joke!")

    if st.button("Generate Joke"):
        joke = fetch_joke()
        if joke:
            st.write(f"**{joke['setup']}**")
            st.write(f"*{joke['punchline']}*")
        else:
            st.error("Failed to fetch joke. Please try again later.")

if __name__ == "__main__":
    main()