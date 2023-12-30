import pandas as pd
import streamlit as st
from textblob import TextBlob


# Function to get sentiment labels for each word
def get_sentiment_labels(text):
    analysis = TextBlob(text)
    sentiments = [word.sentiment.polarity for word in analysis.words]
    return sentiments


# Streamlit app
st.title("HOTEL REVIEWS")
st.sidebar.header("User Inputs")


# Define a function to collect user input features
def user_inputs():
    Name = st.sidebar.text_input("Enter your Name")
    Gender = st.sidebar.selectbox("Select the gender", ["Female", "Male"])
    Hotel = st.selectbox("Select hotel", ["Taj Hotel"])
    location = st.selectbox(
        "Select the location", ["Hyderabad", "HITEC city", "Banjara Hills"]
    )
    Rating = st.sidebar.selectbox("Select Rating", ("1", "2", "3", "4", "5"))
    Reviews = st.sidebar.text_area("Write a Review")

    data = {
        "Name": Name,
        "Gender": Gender,
        "Hotel": Hotel,
        "location": location,
        "Rating": Rating,
        "Reviews": Reviews,
    }
    features = pd.DataFrame(data, index=[0])
    return features


# Call the user_inputs() function to collect user input
df = user_inputs()

# Display the user input features as a subheader and a DataFrame
st.subheader("User Input ")
st.write(df)

# Sentiment Analysis and Word Count
if st.button("Submit"):
    if not df.empty and "Reviews" in df.columns:
        # Get sentiment labels for each word
        df["Sentiment Labels"] = df["Reviews"].apply(
            lambda x: [TextBlob(word).sentiment.polarity for word in x.split()]
        )

        # Count the number of positive, negative, and neutral words
        num_positive_words = sum(
            df["Sentiment Labels"].apply(lambda x: sum(1 for score in x if score > 0))
        )
        num_negative_words = sum(
            df["Sentiment Labels"].apply(lambda x: sum(1 for score in x if score < 0))
        )
        num_neutral_words = sum(
            df["Sentiment Labels"].apply(lambda x: sum(1 for score in x if score == 0))
        )

        # Display sentiment analysis results
        st.subheader("Sentiment Analysis Results")
        st.write(f"Number of Positive Words: {num_positive_words}")
        st.write(f"Number of Negative Words: {num_negative_words}")
        st.write(f"Number of Neutral Words: {num_neutral_words}")

        # Print "Namaste" at the end
        st.write("Thank You For Visiting Taj Hotel")
        st.write("\U0001F64F")
