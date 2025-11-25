#  KAIM Week 1 — News Sentiment & Technical Indicators for Stock Price Movement Prediction

[![CI](https://github.com/hann2004/kaim-week1-news-sentiment/actions/workflows/unittests.yml/badge.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]()
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

This project explores **how financial news sentiment correlates with daily stock market price movements**.
It combines **sentiment analysis**, **technical indicators**, **data visualizations**, and **correlation studies** to assess the predictive value of news in financial markets.

This is my **final submission** for **10 Academy — AI Mastery Program (Week 1 Challenge)**.

---

#  Objectives

The project investigates:

*  Whether sentiment signals align with next-day price changes
*  Whether technical indicators (RSI, MACD, SMA) confirm or contradict sentiment
*  How analyst ratings relate to stock movement
*  Which signals (sentiment or technical) provide stronger predictive patterns
*  Whether combining both can provide robust signals

---

#  Repository Structure

```
kaim-week1-news-sentiment/
├── data/                         # Cleaned stock & news datasets
│   ├── AAPL.csv
│   ├── AMZN.csv
│   ├── GOOG.csv
│   ├── META.csv
│   ├── MSFT.csv
│   ├── NVDA.csv
│   └── raw_analyst_ratings.csv
│
├── notebooks/                    # EDA + analysis notebooks
│   ├── task1_eda.ipynb
│   ├── task2_technical_analysis.ipynb
│   └── task3_sentiment_correlation.ipynb
│
├── scripts/                      # Reusable analysis modules
│   ├── sentiment_analysis.py
│   ├── technical_analysis.py
│   ├── technical_visualization.py
│   ├── correlation_analysis.py
│   ├── pynance_analysis.py
│   └── README.md
│
├── src/                          # Data preprocessing helpers
│   └── data_prep.py
│
├── outputs/                      # Generated plots
│   ├── AAPL_*.png
│   ├── AMZN_*.png
│   ├── GOOG_*.png
│   ├── META_*.png
│   ├── MSFT_*.png
│   └── NVDA_*.png
│
├── tests/                        # Unit tests (pytest)
│   ├── test_sanity.py
│   └── test_technical_analysis.py
│
├── .gitignore
├── requirements.txt
├── .github/workflows/unittests.yml
└── README.md
```

---

#  Environment Setup (Conda Version)

```bash
conda create -n kaim python=3.10 -y
conda activate kaim
pip install -r requirements.txt
```

---

#  Features Implemented

###  **1. Data Loading & Preprocessing**

* Unified structure for stock datasets
* Cleaned missing values
* Added daily returns, volatility, and metadata

###  **2. Sentiment Analysis**

Using:

* **TextBlob**
* **VADER**
* Standardized compound polarity scoring
* Merged sentiment with stock data by date

###  **3. Technical Indicators**

Implemented manually using pandas:

* SMA (20 & 50)
* RSI (14)
* MACD (12/26 with 9-signal)
* MACD Histogram
* Volatility
* Daily returns

###  **4. Visualizations**

* Price + SMA overlays
* RSI oscillators
* MACD with signal/histogram
* Sentiment vs price movement
* Analyst ratings vs returns
* Comprehensive chart per stock

###  **5. Correlation Analysis**

* Pearson correlation between:

  * sentiment & returns
  * SMA crossover signals & returns
  * MACD signals & returns
  * combined features

###  **6. Automated Testing (CI/CD)**

Includes:

* sanity check
* indicator shape/validity tests
* workflow pipeline via GitHub Actions

---

#  How to Run Analysis

### **Open Jupyter Notebook**

```bash
jupyter lab
```

Inside notebooks:

* `task1_eda.ipynb` — Explore data
* `task2_technical_analysis.ipynb` — Indicators + visualizations
* `task3_sentiment_correlation.ipynb` — Sentiment + correlation

---

#  Running Unit Tests

```bash
pytest -q
```

GitHub Actions badge in repo confirms pipeline status.

---

#  Key Insights (Summary)

*(Add your own insights here based on results! For example:)*

* Sentiment spikes often precede volatility jumps
* MACD histogram aligns strongly with positive analyst upgrades
* SMA crossovers lag sentiment-based moves
* Sentiment signals alone are noisy but meaningful when combined with SMA & MACD

---

#  Future Improvements

* Automate full end-to-end pipeline
* Add LLM-based headline embeddings
* Try logistic regression or random forest for prediction
* Add dashboard (Streamlit)
* Improve visual style of indicators

---

#  Author

**Hanan**
AI Mastery Program — Week 1 Final Submission
10 Academy


