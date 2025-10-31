# 💬 ChatSense — WhatsApp Chat Analyzer  

[![Project](https://img.shields.io/badge/Project-Internship-blue)](#)
[![Language](https://img.shields.io/badge/Language-Python-366a9c)](#)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-ff4b4b)](#)

**ChatSense** is an interactive analytics dashboard that parses exported WhatsApp chat files and produces meaningful insights — message activity, timelines, most active users, word frequency, and emoji statistics — all visualized through an intuitive Streamlit interface.  

> 🧑‍💻 Built as a **team project** during a **Data Science Internship at [CodeSpyder]**.

---

## 🔎 Project Summary

**Duration:** 4.5 months  
**Team Size:** 3 Interns  

- Parses WhatsApp exported chat files (`.txt`) using regex.  
- Converts messages into a structured DataFrame using **Pandas**.  
- Performs **statistical, time-based, and text-based analysis**.  
- Generates **interactive charts, word clouds, and emoji breakdowns**.  
- Built with **Python**, **Streamlit**, and popular data libraries.

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3.8+ |
| **Libraries** | pandas, regex, matplotlib, seaborn, wordcloud, urlextract, emoji, streamlit |
| **Tools** | VS Code, Git & GitHub |
| **Frontend/UI** | Streamlit Dashboard |

---

## ⚙️ Technical Workflow

### 🧹 1. Parsing & Preprocessing
- Used **regex** to extract date, time, user, and message from exported chats.  
- Converted timestamps using `pandas.to_datetime`.  
- Handled Unicode characters (like `U+202F` narrow spaces).  
- Generated derived columns:
  - `only_date`, `month`, `month_num`, `day_name`, `hour`, `minute`, `period`.

### 📊 2. Data Analysis
- Counted **messages, words, media files, and shared links**.  
- Generated **monthly/daily timelines**, **busiest days**, and **activity heatmaps** using `groupby` and `pivot_table`.  
- Identified **most active users** and **message patterns**.  

### 🔠 3. Text Processing
- Created a **custom Hinglish stopwords file** (`stop_hinglish.txt`).  
- Built **word clouds** and **most common word lists**.

### 😂 4. Emoji & Link Extraction
- Used the modern `emoji.is_emoji()` for counting emojis.  
- Extracted URLs via **URLExtract** for link-sharing analysis.

### 📈 5. Visualization
- Designed interactive charts with **Matplotlib** and **Seaborn**.  
- Integrated **Streamlit UI**:  
  - Sidebar file upload  
  - Per-user analysis  
  - Metrics and charts for better storytelling  

---
## 🗂️ Project Structure
- ChatSense/
- ├── app.py # Streamlit dashboard
- ├── preprocessor.py # Data parsing and cleaning
- ├── helper.py # Analytical and plotting functions
- ├── stop_hinglish.txt # Custom Hinglish stopwords
- ├── requirements.txt
- └── README.md

## 🎯 Key Features

- Upload WhatsApp chat (.txt) for instant analysis.
- Insights for individuals or overall group.
- Timeline and activity-based plots.
- Word cloud, most common words, and emoji frequency.
- Minimal, modern Streamlit dashboard UI.
