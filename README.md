![CI](https://github.com/hann2004/kaim-week1-news-sentiment/actions/workflows/unittests.yml/badge.svg)

# 📈 KAIM Week 1 - Predicting Price Moves with News Sentiment

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python)](https://www.python.org/) 
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![TA-Lib](https://img.shields.io/badge/TA--Lib-0.4.0-lightgrey)](https://mrjbq7.github.io/ta-lib/)
[![TextBlob](https://img.shields.io/badge/TextBlob-0.17.1-yellow)](https://textblob.readthedocs.io/)
[![VADER](https://img.shields.io/badge/VADER-1.3.2-red)](https://github.com/cjhutto/vaderSentiment)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

This project applies **news sentiment analysis**, **technical indicators**, and **data visualization** to explore how financial news may influence daily stock price movements. It is part of **10 Academy — AI Mastery Program (Week 1 Challenge)**.

---

## **🔍 Project Overview**

The goal of this project is to:

* Collect and preprocess stock market data
* Perform sentiment analysis on financial news headlines
* Compute technical indicators (RSI, MACD, SMA, etc.)
* Visualize trends and relationships
* Compare sentiment-based signals with technical signals
* Evaluate whether sentiment provides predictive insight

---

## **📁 Repository Structure**

```
kaim-week1-news-sentiment/
├── .github/                     # GitHub Actions workflows (CI/CD)
├── data/                        # Financial datasets
│   ├── notebooks/               # Jupyter notebooks used for EDA & comparisons
│   │   ├── __init__.py
│   │   ├── task1_eda.ipynb
│   │   ├── task2_technical_analysis.ipynb
│   │   └── README.md
├── scripts/                     # Reusable analysis modules
│   ├── technical_analysis.py    # TA-Lib indicator calculations
│   ├── technical_visualization.py # Plotting utilities
│   └── __init__.py
├── src/                         # Data preprocessing
│   ├── data_prep.py             # Data loading & cleaning helpers
│   └── __init__.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## **⚙️ Installation**

### **1. Clone the repository**

```bash
git clone https://github.com/<your-username>/kaim-week1-news-sentiment
cd kaim-week1-news-sentiment
```

### **2. Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **🧠 Features Implemented**

### **✔ Data Loading & Cleaning**

* Import historical stock prices
* Parse & align headline sentiment with daily trading data

### **✔ Sentiment Analysis**

* Compute sentiment scores from financial news
* Normalization & aggregation by date

### **✔ Technical Indicators**

(Implemented in `technical_analysis.py`)

* RSI
* MACD
* SMA / EMA
* Volatility measures
* Price returns

### **✔ Visualizations**

(Provided in `technical_visualization.py`)

* Price charts with technical overlays
* Sentiment vs. returns plots
* Indicator comparison charts

### **✔ Exploratory Data Analysis**

(Inside notebooks)

* Trend inspection
* Correlation studies
* Feature behavior visualized

---

## **📘 How to Use**

### **Run notebooks**

Open JupyterLab:

```bash
jupyter lab
```

Then explore:

* `task1_eda.ipynb`
* `task2_technical_analysis.ipynb`

### **Use Python scripts**

Example:

```python
from scripts.technical_analysis import compute_rsi
from src.data_prep import load_stock_data

df = load_stock_data("data/your_file.csv")
df = compute_rsi(df)
```

---

## **🛠 Planned Improvements (for resubmission)**

These are the updates planned to fully align with the rubric:

* Add simple **unit tests** using pytest
* Introduce **OOP structure** for sentiment, technicals, and processing
* Expand inline documentation and docstrings
* Add more detailed examples
* Improve modularity of analysis pipeline

---

## **📄 Requirements**

All dependencies are listed in `requirements.txt`.

Typical stack:

* Python 3.10+
* pandas
* numpy
* matplotlib
* TA-Lib
* Jupyter

---

## **👤 Author**

**Hanan**
10 Academy — Artificial Intelligence Mastery
Week 1 Challenge Submission


