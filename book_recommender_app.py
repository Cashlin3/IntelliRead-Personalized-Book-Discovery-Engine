import streamlit as st
st.set_page_config(page_title="📚 AI Book Recommender", layout="centered")  # ✅ FIRST

import pandas as pd
import joblib
import ast
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Dell\Downloads\goodreads_data.csv")
    df = df.dropna(subset=['Book', 'Genres', 'Avg_Rating'])

    # Extract main genre safely
    def extract_main_genre(genre_str):
        try:
            genres = ast.literal_eval(genre_str)
            if genres and isinstance(genres, list):
                return genres[0]
        except:
            return None
        return None

    df['Main_Genre'] = df['Genres'].apply(extract_main_genre)
    df = df.dropna(subset=['Main_Genre'])
    return df

df = load_data()

# Encode genres
genre_encoder = LabelEncoder()
df['Genre_Label'] = genre_encoder.fit_transform(df['Main_Genre'])

# Train simple model to predict rating
X = df[['Genre_Label']]
y = df['Avg_Rating']
model = LinearRegression()
model.fit(X, y)

# Streamlit App Interface
st.title("📘 ML-Powered Book Recommendation System")
st.markdown("Get smart book suggestions powered by **Machine Learning** and **Data Science**. Just pick your favorite genre!")

# Genre selection
genres = sorted(df['Main_Genre'].unique())
selected_genre = st.selectbox("📂 Select a Genre", genres)

if selected_genre:
    label = genre_encoder.transform([selected_genre])[0]
    predicted_rating = model.predict([[label]])[0]
    st.success(f"📊 Predicted average rating for **{selected_genre}** books: **{predicted_rating:.2f}**")

    # Recommend books
    top_books = df[df['Main_Genre'] == selected_genre].sort_values(by='Avg_Rating', ascending=False).head(3)
    st.subheader("📚 Top Recommended Books")
    for _, row in top_books.iterrows():
        st.markdown(f"""
        ### 📖 {row['Book']}
        - 👨‍💼 Author: {row['Author']}
        - ⭐ Rating: {row['Avg_Rating']}
        - 🔗 [View on Goodreads]({row['URL']})
        - 📝 _{row['Description'][:250]}..._
        """)

st.markdown("---")
st.caption("Made with 💡 ML + ❤️ by [CASHLIN]")