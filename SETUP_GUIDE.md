# 🛠️ SETUP GUIDE — Follow these 5 steps

## ✅ STEP 1: Download the dataset
1. Go to: https://www.kaggle.com/datasets/stefanoleone992/ea-sports-fc-24-complete-player-dataset
2. Sign in (create a free account if needed)
3. Click the **Download** button
4. Extract the ZIP
5. Find the file `male_players.csv`, **rename it to `players.csv`**
6. Move it into the `data/` folder of this project

## ✅ STEP 2: Install Python packages
Open a terminal inside this project folder and run:
```bash
pip install -r requirements.txt
```

## ✅ STEP 3: Run the notebook
```bash
jupyter notebook notebooks/FIFA_Player_Value_Predictor.ipynb
```
Then click **Cell → Run All** in the menu.

All charts will auto-save inside the `visuals/` folder.

## ✅ STEP 4: Push to GitHub
Inside this project folder:
```bash
git init
git add .
git commit -m "Initial commit: FIFA Player Value Predictor"
```

Then on GitHub.com:
1. Click **+** → **New repository**
2. Name: `FIFA-Player-Value-Predictor`
3. Keep it **Public**, DO NOT add a README (you already have one)
4. Click **Create repository**

Copy the commands GitHub shows you — they look like:
```bash
git remote add origin https://github.com/neelacademy10-crypto/FIFA-Player-Value-Predictor.git
git branch -M main
git push -u origin main
```

## ✅ STEP 5: Post on LinkedIn
Use the post template below, attach 2-3 chart screenshots from the `visuals/` folder.

**Best charts for LinkedIn:**
1. `feature_importance.png` — most eye-catching
2. `top10_valuable.png` — recognizable player names grab attention
3. `predictions_vs_actual.png` — shows the ML worked

---

## 📱 LINKEDIN POST TEMPLATE

🚀 New project drop: FIFA Player Value Predictor

As a Data Analytics student, I wanted to answer a question I've always been curious about:

What actually drives a football player's market value?

So I built an end-to-end ML project using the EA Sports FC 24 dataset (17,000+ players, 100+ attributes).

What I did:
↳ Cleaned & explored the data in Python (pandas)
↳ Built 6 visualizations to uncover patterns
↳ Trained two ML models — Linear Regression & Random Forest
↳ Random Forest hit an R² of ~0.95 predicting player values

Biggest takeaway 👇
Overall rating and wage together explain most of a player's market value — but age and potential matter more than I expected for young players.

Stack used: Python, pandas, scikit-learn, seaborn, matplotlib

Full code + visuals on GitHub 🔗 [PASTE YOUR GITHUB REPO LINK HERE]

This is project 1 of a series I'm posting as I grow my data analytics portfolio.

What should I analyze next? Drop ideas in the comments 👇

#DataAnalytics #MachineLearning #Python #Portfolio #FanshaweCollege #FIFA

---

## ⚠️ If anything breaks
Copy the error message and send it back — I'll help debug.
