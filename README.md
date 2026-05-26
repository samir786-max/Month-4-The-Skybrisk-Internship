# 🎬 Advanced Movie Recommendation System

An AI-powered Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**.

This project recommends movies similar to the movie selected by the user using **TF-IDF Vectorization** and **Cosine Similarity**. The recommendation engine analyzes movie genres, keywords, overview, and cast information to suggest the most relevant movies.

---

# 🚀 Features

✅ AI-Based Movie Recommendations  
✅ Genre Filtering  
✅ Trending Movies Section  
✅ Movie Ratings & Release Year  
✅ Fast Search System  
✅ Dark Modern UI  
✅ Streamlit Web Application  
✅ Machine Learning Recommendation Engine  
✅ Dataset-Based Recommendations (No API Required)  
✅ Similar Movie Matching  
✅ Responsive Layout  
✅ User-Friendly Interface  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Pandas | Data Handling |
| NumPy | Numerical Computation |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| TF-IDF Vectorizer | Text Vectorization |
| Cosine Similarity | Recommendation Algorithm |

---

# 🧠 Machine Learning Algorithm Used

The recommendation system works using:

- **TF-IDF Vectorization**
- **Cosine Similarity Algorithm**

The model analyzes:

- Movie Overview
- Genres
- Keywords
- Cast Information

to recommend movies similar to the selected movie.

---

# 📂 Project Structure

```bash
movie-recommender/
│
├── app.py
├── model_builder.py
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

# 📥 Dataset Download

## TMDB 5000 Movie Dataset

### Kaggle Dataset

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## Direct CSV Download Links

### Movies Dataset

https://raw.githubusercontent.com/krishnaik06/Recommendation-Systems/main/tmdb_5000_movies.csv

### Credits Dataset

https://raw.githubusercontent.com/krishnaik06/Recommendation-Systems/main/tmdb_5000_credits.csv

---

# ⚙️ Installation

## Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
```

---

## Step 2 — Open Project Folder

```bash
cd movie-recommender
```

---

## Step 3 — Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run Project

## Step 1 — Generate Model Files

Run:

```bash
python model_builder.py
```

This will generate:

- movies.pkl
- similarity.pkl

---

## Step 2 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📦 requirements.txt

Create a file named `requirements.txt` and paste:

```txt
streamlit
pandas
numpy
scikit-learn
```

---

# 🎯 How Recommendation Works

1. Dataset is loaded using Pandas
2. Important features are extracted
3. Text data is converted using TF-IDF Vectorizer
4. Cosine similarity is calculated
5. Similar movies are recommended to users

---

# 📸 Application Features

## 🔥 Trending Movies

Displays top-rated trending movies from the dataset.

## 🎭 Genre Filtering

Users can filter movie recommendations based on genres.

## ⭐ Ratings & Release Year

Each movie recommendation displays:
- Movie Rating
- Release Year
- Genres

## 🎥 Smart Recommendations

The recommendation engine suggests movies based on similarity score.

---

# 📈 Future Improvements

- Movie Posters
- Trailer Integration
- Voice Search
- User Authentication
- Watchlist Feature
- Netflix Style UI
- AI Chatbot Assistant
- Deep Learning Recommendation Engine
- Recommendation History
- Database Integration

---

# 💻 Screenshots

## Main Dashboard

- Dark Theme UI
- Trending Movies
- Search & Recommendation System

## Recommendation Section

- Similar Movie Suggestions
- Ratings
- Genres
- Release Year

---

# 🌐 Streamlit Deployment

To deploy online:

## Streamlit Cloud

https://streamlit.io/cloud

Upload your GitHub repository and deploy easily.

---

# 🧪 Example Movies to Search

- Avatar
- Batman Begins
- Spectre
- The Dark Knight
- Interstellar
- Titanic
- Inception

---

# 📚 Learning Outcomes

This project helps understand:

- Recommendation Systems
- Machine Learning Basics
- NLP Concepts
- Streamlit Web Development
- Data Preprocessing
- Similarity Algorithms

---

# 👨‍💻 Author

Developed using Python, Machine Learning, and Streamlit for educational and portfolio purposes.

---

# ⭐ Project Outcome

This project demonstrates:

✅ Machine Learning Concepts  
✅ Recommendation Systems  
✅ NLP-Based Similarity  
✅ Data Processing  
✅ Streamlit Web Development  
✅ Real-World AI Application  

Suitable for:

- College Projects
- Minor/Major Projects
- Resume Projects
- Portfolio Projects
- Machine Learning Demonstrations

---

# 📜 License

This project is open-source and free to use for educational purposes.
