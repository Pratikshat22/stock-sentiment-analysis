import streamlit as st

st.set_page_config(page_title="Enhanced Stock Sentiment Analysis", layout="wide")

st.title("📈 Enhanced Stock Sentiment Analysis")
st.markdown("### Project for Google Apprenticeship by **Pratiksha Thakur**")

# --- Project Summary ---
st.subheader("🔍 Project Summary")
st.write("""
This project analyzes stock news headlines using **TextBlob + VADER Sentiment**,
engineers 15+ features, and applies ML models (Random Forest, XGBoost, SVM, Logistic Regression).
Best model achieved **~54% accuracy**, beating random guess baseline in a highly unpredictable domain.
""")

# --- Key Achievements ---
st.subheader("✅ Technical Achievements")
st.markdown("""
- End-to-end data pipeline with real Yahoo Finance stock data  
- Dual Sentiment Analysis: **TextBlob + Vader**  
- 15+ Feature Engineering (text, time, sentiment intensity)  
- Compared 4 ML Models + Hyperparameter Tuning  
- Visualized Results: ROC Curve, Confusion Matrix, Feature Importance  
- Business Insights for Stock Market Patterns
""")

# --- Business Insights ---
st.subheader("📊 Business Insights")
st.markdown("""
1. **Time factors** (Day of Week, Month) are strongest predictors  
2. **Sentiment Intensity > Polarity** → strong emotions move markets  
3. **Growth-related news** is more predictive than earnings/negative news  
4. Balanced performance across bull & bear conditions  
5. Random Forest proved most robust  
""")

# --- Link to Code/Resume ---
st.subheader("📂 Resources")
st.markdown("""
- [GitHub Repo](https://github.com/) (upload your code here)  
- [Resume](https://drive.google.com/) (link your Google Docs resume)  
- Contact: **nmee8753@gmail.com**
""")

st.success("🚀 Ready for recruiters! Deploy this to Streamlit Cloud in 2 minutes.")
