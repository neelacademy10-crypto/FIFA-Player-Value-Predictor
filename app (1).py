import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

st.set_page_config(
    page_title="FIFA Player Value Predictor",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&display=swap');

.main { background-color: #0a3d1f; }
.block-container { padding-top: 2rem; max-width: 1100px; }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem; font-weight: 800;
    color: #f8fafc; line-height: 1.1; margin-bottom: 0.5rem;
}
.hero-title span { color: #4ade80; }
.hero-sub { color: #94a3b8; font-size: 1rem; margin-bottom: 1rem; }

.badge {
    display: inline-block;
    background: rgba(74,222,128,0.12);
    border: 1px solid rgba(74,222,128,0.3);
    border-radius: 999px; padding: 4px 14px;
    color: #4ade80; font-size: 0.75rem;
    letter-spacing: 0.05em; text-transform: uppercase;
    font-weight: 600; margin-bottom: 1rem;
}

.metric-container {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px; padding: 1.2rem;
    border-top: 2px solid #4ade80;
}
.metric-label { color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.07em; }
.metric-value { color: #4ade80; font-size: 1.8rem; font-weight: 700; font-family: 'Syne', sans-serif; }
.metric-sub { color: #94a3b8; font-size: 0.75rem; }

.section-title {
    color: #4ade80; font-size: 0.75rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.1em;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 0.5rem; margin-bottom: 1rem;
}

.chart-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px; padding: 1.2rem;
}
.chart-title { color: #f8fafc; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.5rem; }
.chart-caption { color: #64748b; font-size: 0.75rem; margin-top: 0.4rem; text-align: center; }

.insight-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px; padding: 1rem 1.2rem;
    margin-bottom: 0.75rem;
}
.insight-num { color: rgba(74,222,128,0.3); font-size: 1.4rem; font-weight: 800; }
.insight-text { color: #94a3b8; font-size: 0.88rem; line-height: 1.6; }
.insight-text strong { color: #f8fafc; }

.model-best { color: #4ade80 !important; font-weight: 600; }
.pred-note {
    background: rgba(74,222,128,0.08);
    border: 1px solid rgba(74,222,128,0.2);
    border-radius: 8px; padding: 0.5rem 1rem;
    color: rgba(74,222,128,0.7); font-size: 0.8rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown('<div class="badge">⚡ Live Portfolio Dashboard</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-title">FIFA Player<br><span>Value Predictor</span></div>
<div class="hero-sub">End-to-end ML project — Data Cleaning · EDA · Predictive Modeling · 177K+ players</div>
""", unsafe_allow_html=True)

col_meta1, col_meta2 = st.columns([3, 1])
with col_meta1:
    st.markdown("""
    **Dataset:** EA Sports FC 24 · Kaggle &nbsp;|&nbsp;
    **Best Model:** Random Forest · R² 0.94 &nbsp;|&nbsp;
    **Author:** Neel Mendapara · Fanshawe College
    """)
with col_meta2:
    st.link_button("⭐ View on GitHub", "https://github.com/neelacademy10-crypto/FIFA-Player-Value-Predictor")

st.divider()

# ── KPI CARDS ──
k1, k2, k3, k4, k5 = st.columns(5)

def kpi(col, label, value, sub):
    col.markdown(f"""
    <div class="metric-container">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-sub">{sub}</div>
    </div>""", unsafe_allow_html=True)

kpi(k1, "Dataset Size", "177K+", "FC 24 players")
kpi(k2, "Best R² Score", "0.94", "Random Forest")
kpi(k3, "Best MAE", "€452K", "Mean abs. error")
kpi(k4, "Features", "13", "Incl. wage, potential")
kpi(k5, "Models", "2", "LR · Random Forest")

st.markdown("<br>", unsafe_allow_html=True)

# ── MODEL COMPARISON ──
st.markdown('<div class="section-title">Model Performance</div>', unsafe_allow_html=True)

model_df = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest 🏆"],
    "R² Score": [0.626, 0.937],
    "MAE (€)": ["€1,620,855", "€452,243"],
    "Winner": ["", "✅ Best"]
})

col_table, col_chart = st.columns([1, 1])
with col_table:
    st.dataframe(
        model_df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "R² Score": st.column_config.ProgressColumn(
                "R² Score", min_value=0, max_value=1, format="%.3f"
            )
        }
    )
    st.caption("Random Forest outperforms Linear Regression by 31% on R² score")

with col_chart:
    if os.path.exists("visuals/top10_valuable.png"):
        st.image("visuals/top10_valuable.png", use_container_width=True)
    else:
        st.info("visuals/top10_valuable.png")

st.divider()

# ── EDA CHARTS ──
st.markdown('<div class="section-title">Exploratory Data Analysis — Actual Python Outputs</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="chart-title">Overall Rating vs Market Value</div>', unsafe_allow_html=True)
    if os.path.exists("visuals/rating_vs_value.png"):
        st.image("visuals/rating_vs_value.png", use_container_width=True)
    st.caption("Correlation: 0.74 — higher rating = exponentially higher value")

with c2:
    st.markdown('<div class="chart-title">Feature Correlation Heatmap</div>', unsafe_allow_html=True)
    if os.path.exists("visuals/correlation_heatmap.png"):
        st.image("visuals/correlation_heatmap.png", use_container_width=True)
    st.caption("Wage–Value: 0.90 · Overall–Value: 0.74 · Age–Value: −0.16")

st.markdown("<br>", unsafe_allow_html=True)
c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="chart-title">Actual vs Predicted — Random Forest</div>', unsafe_allow_html=True)
    if os.path.exists("visuals/predictions_vs_actual.png"):
        st.image("visuals/predictions_vs_actual.png", use_container_width=True)
    st.caption("Points close to the red line = accurate predictions")

with c4:
    st.markdown('<div class="chart-title">Feature Importance — Random Forest</div>', unsafe_allow_html=True)
    if os.path.exists("visuals/feature_importance.png"):
        st.image("visuals/feature_importance.png", use_container_width=True)
    st.caption("Potential (42%) and Overall (30%) dominate — ceiling beats current form")

st.divider()

# ── INTERACTIVE PREDICTOR ──
st.markdown('<div class="section-title">Interactive Value Estimator</div>', unsafe_allow_html=True)
st.markdown('<div class="pred-note">⚠ Simulated estimator based on model patterns — not the live trained model</div>', unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)
with p1:
    overall = st.slider("Overall Rating", 45, 95, 75)
with p2:
    potential = st.slider("Potential", 45, 99, 82)
with p3:
    age = st.slider("Age", 17, 40, 24)
with p4:
    reputation = st.slider("Int. Reputation (1–5)", 1, 5, 2)

age_factor = 1.4 if age < 23 else (1.15 if age < 27 else (0.9 if age < 31 else 0.6))
raw = ((overall - 45) / 50) ** 2.5 * 15 + ((potential - 45) / 54) ** 2.2 * 18 + reputation * 1.2
value_m = round(max(0.1, raw * age_factor), 1)
tier = "Elite" if value_m > 20 else ("High Value" if value_m > 10 else ("Medium Value" if value_m > 3 else "Low Value"))

r1, r2, r3 = st.columns(3)
r1.metric("Estimated Market Value", f"€{value_m}M")
r2.metric("Player Tier", tier)
r3.metric("Age Factor Applied", f"×{age_factor}")

st.divider()

# ── KEY INSIGHTS ──
st.markdown('<div class="section-title">Key Findings</div>', unsafe_allow_html=True)

insights = [
    ("01", "<strong>Potential (#1 feature at 42%) outweighs current form.</strong> Random Forest learned that clubs pay for ceiling, not just current ability. A 22-year-old with 90 potential commands far more than a 32-year-old rated 78."),
    ("02", "<strong>Wage is the strongest market signal (0.90 correlation with value).</strong> Wage_EUR and Value_EUR move almost in lockstep — clubs signal what they believe a player is worth through wages."),
    ("03", "<strong>Random Forest explains 94% of variance in player market value</strong> — 31% better than linear regression. Non-linear interactions between age, potential and overall simply cannot be captured by a straight line."),
]
for num, text in insights:
    st.markdown(f"""
    <div class="insight-card">
        <div style="display:flex;gap:14px;align-items:flex-start">
            <div class="insight-num">{num}</div>
            <div class="insight-text">{text}</div>
        </div>
    </div>""", unsafe_allow_html=True)

st.divider()

# ── FOOTER ──
fc1, fc2, fc3 = st.columns(3)
fc1.markdown("[🔗 GitHub Repository](https://github.com/neelacademy10-crypto/FIFA-Player-Value-Predictor)")
fc2.markdown("[💼 LinkedIn Profile](https://www.linkedin.com/in/neel-mendapara-77b15a218/)")
fc3.markdown("[📊 Canada Vapes Project](https://github.com/neelacademy10-crypto/Canada-Vapes)")
st.caption("Built by Neel Mendapara · Data Analytics · Fanshawe College · 2026")
