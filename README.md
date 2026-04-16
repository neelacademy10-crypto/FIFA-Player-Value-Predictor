# FIFA Player Value Predictor

A data analytics and machine learning project that predicts football player market values using the EA Sports FC 24 (FIFA 24) dataset.

## Project Overview
This project explores what factors drive a football player's market value and builds a machine learning model to predict it. It covers the full data science workflow: data cleaning, exploratory data analysis, feature engineering, model training, and evaluation.

## Dataset
- **Source:** [EA Sports FC 24 Complete Player Dataset (Kaggle)](https://www.kaggle.com/datasets/stefanoleone992/ea-sports-fc-24-complete-player-dataset)
- **Size:** 17,000+ players, 110 attributes
- **Target variable:** `value_eur` (market value in Euros)

## Tools & Libraries
- **Python 3**
- **pandas, NumPy** — data manipulation
- **matplotlib, seaborn** — data visualization
- **scikit-learn** — machine learning (Linear Regression, Random Forest)
- **Jupyter Notebook**

## Key Findings
- Overall rating and wage are the strongest predictors of player value
- Random Forest significantly outperforms Linear Regression (R² ~0.95 vs ~0.65)
- Top 5 European leagues dominate average player valuations
- Age has a non-linear impact — young high-potential players are valued higher

## Project Structure
```
FIFA-Player-Value-Predictor/
├── data/                                        # Raw dataset (gitignored)
├── notebooks/
│   └── FIFA_Player_Value_Predictor.ipynb        # Main analysis notebook
├── visuals/                                     # Generated charts
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run
1. Download the dataset from Kaggle and place `players.csv` in the `data/` folder
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Launch Jupyter and run the notebook:
```bash
jupyter notebook notebooks/FIFA_Player_Value_Predictor.ipynb
```
4. Run all cells top to bottom

##  Sample Visualizations
Charts generated in this project include:
- Top 10 most valuable players
- Age distribution
- Overall rating vs market value
- Top 10 leagues by average player value
- Feature correlation heatmap
- Feature importance (Random Forest)
- Predicted vs actual values

## 👤 Author
**Neel Mendapara**  
Data Analytics Student, Fanshawe College  
[GitHub](https://github.com/neelacademy10-crypto) | [LinkedIn](https://linkedin.com/in/YOUR-USERNAME)

---
⭐ If you found this project helpful, consider giving it a star!
