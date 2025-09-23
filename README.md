# 🎬 Movie Recommendation System

This project is a **content-based movie recommendation system** built with **Flask**. It suggests movies based on their **descriptions, genres, and metadata** using **TF-IDF Vectorization** and **Cosine Similarity**. Additionally, it leverages elements of **collaborative filtering** to refine recommendations. The system is lightweight, extendable, and serves recommendations through a simple Flask backend.

---

# 📑 Table of Contents

1. [🎬 Overview](#-overview)  
2. [🚀 Features](#-features)  
3. [🗂 Dataset](#-dataset)  
4. [🛠️ Tech Stack](#-tech-stack)  
5. [⚙️ Installation](#️-installation)  
   - [Clone Repository](#clone-repository)  
   - [Virtual Environment](#virtual-environment)  
   - [Install Dependencies](#install-dependencies)  
   - [Prepare Dataset](#prepare-dataset)  
6. [▶️ Running the Project](#️-running-the-project)  
7. [📊 Recommendation Logic](#-recommendation-logic)  
8. [📂 Project Structure](#-project-structure)  
9. [📌 Example Output](#-example-output)  
10. [🤝 Contribution](#-contribution)  
11. [📜 License](#-license)

---

## 🎬 Overview
This system suggests movies based on **plot descriptions, genres, and ratings**, leveraging **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features
- Content-based filtering using movie descriptions.
- Cosine similarity to measure closeness between movies.
- Flask backend with endpoints for recommendations.
- Simple and extendable codebase.

---

## 🗂 Dataset
- `movies_data.csv` → Contains movie ratings and IDs.
- `moviesmeta_data.csv` → Contains movie metadata (title, genre, overview, etc.).

Both datasets should be placed in the `dataset/` folder.

---

## 🛠️ Tech Stack
- **Python** (Flask, Pandas, Scikit-learn, Numpy, Joblib)
- **HTML/CSS/Bootstrap** (Frontend templates)
- **IMDB dataset** (~45k entries)

---

## ⚙️ Installation

### Clone Repository
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Prepare Dataset
Ensure `movies_data.csv` and `moviesmeta_data.csv` are inside the `dataset/` folder.

---

## ▶️ Running the Project
```bash
python main.py
```
Access the app at: **http://127.0.0.1:5000/**

---

## 📊 Recommendation Logic
- **TF-IDF Vectorizer** → Transforms movie descriptions into vectors.
- **Cosine Similarity** → Finds the closest matching movies.
- **Collaborative Filtering** → Enhances recommendations using user ratings.

---

## 📂 Project Structure
```
movie-recommendation-system/
| - dataset/
|    | - movies_data.csv
|    | - moviesmeta_data.csv
| - static/
| - templates/
| - main.py
| - modal.py
| - rapid.py
| - requirements.txt
| - README.md
```

---

## 📌 Example Output
If user searches for **“Skyfall”**, system may recommend:
- Casino Royale
- Quantum of Solace
- Spectre
- GoldenEye

---

## 🤝 Contribution
1. Fork the repo
2. Create a feature branch (`feature-new-idea`)
3. Commit changes
4. Push to branch
5. Create a Pull Request

---

## 📜 License
This project is licensed under the MIT License.
