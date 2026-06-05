# IntelliRead 📚

**Personalized Book Discovery Engine** — Get smart book recommendations powered by collaborative filtering and cosine similarity.

## How to get Started

```bash
#Clone the repository
git clone https://github.com/Cashlin3/IntelliRead-Personalized-Book-Discovery-Engine.git
cd IntelliRead-Personalized-Book-Discovery-Engine

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## ✨ What It Does

- **Personalized Recommendations** → Suggests books based on the genre selected
- **Collaborative Filtering** → Uses cosine similarity to find similar books and readers
- **Goodreads Integration** → Linked with Goodreads for top-rated books and ratings
- **Genre Exploration** → Discover gems in your favorite genres
- **Interactive UI** → Beautiful, user-friendly interface built with Streamlit
- **Data-Driven Insights** → ML-powered recommendations, not random suggestions

---

## 🛠️ Tech Stack

| Tool - Purpose |
|----------------|
| **Python** - Core programming language |
| **Pandas** - Data processing & analysis |
| **Scikit-learn** - Collaborative filtering & cosine similarity |
| **Streamlit** - Interactive web interface |
| **Goodreads API** - Book data & ratings |

---

## 🎯 How It Works

### 1. Collaborative Filtering
```python
from sklearn.metrics.pairwise import cosine_similarity

# Find similar books based on user ratings
similarity_matrix = cosine_similarity(user_rating_matrix)
```

### 2. Recommendation Process
- User selects preferred genres 
- System finds similar readers using cosine similarity
- Recommends top-rated books from similar users
- Displays Goodreads ratings and links

---

## 📸 Features

| Feature - Description |
|-----------------------|
| **Smart Filtering** - Collaborative filtering finds books you'll love |
| **Genre Filters** - Browse by Fiction, Non-Fiction, Sci-Fi, Romance, etc. |
| **Goodreads Integration** - See real ratings and book details |
| **Quick Search** - Find books instantly by title or author |
| **Recommendation Score** - See match percentage for each book |

---

## 🎓 Perfect For

- Avid readers looking for their next favorite book
- Book lovers tired of random recommendations
- People exploring new genres
- Goodreads users wanting smarter suggestions

---

## 🤝 Contributing

Contributions welcome! Feel free to fork, suggest changes, and submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
   
---

## 📬 Connect

🔗 [LinkedIn](https://linkedin.com/in/cashlin-tech/) | 🐙 [GitHub](https://github.com/Cashlin3)

**Project Link**: [https://github.com/Cashlin3/IntelliRead-Personalized-Book-Discovery-Engine](https://github.com/Cashlin3/IntelliRead-Personalized-Book-Discovery-Engine)

---

*Built with ❤️ for book lovers*  
⭐ **Star this repo** if you find it helpful!
