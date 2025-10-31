# ChatSense-WhatsApp-Chat-Analyzer

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>ChatSense — WhatsApp Chat Analyzer</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; background: #0f1724; color: #e6eef8; line-height: 1.6; padding: 2rem; }
    .container { max-width: 900px; margin: 0 auto; background: #0b1220; border-radius: 12px; padding: 28px; box-shadow: 0 8px 30px rgba(2,6,23,0.7); }
    h1 { color: #00d084; margin-bottom: 6px; }
    h2 { color: #8bd5ff; margin-top: 28px; }
    p.lead { color: #cfeefe; margin-top: 0; }
    .badges img { height: 24px; margin-right: 8px; vertical-align: middle; }
    pre { background: #08121a; padding: 12px; border-radius: 8px; overflow:auto; color: #d8f3ff; }
    code { background: rgba(255,255,255,0.03); padding: 2px 6px; border-radius: 6px; color:#bfe9ff; }
    ul { margin-top: 0; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
    .card { background: #071022; padding: 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.03); }
    .muted { color: #95b0c7; font-size: 0.95rem; }
    a { color: #7be7b9; text-decoration: none; }
    .center { text-align:center; }
    .screenshot { width:100%; border-radius:8px; border:1px solid rgba(255,255,255,0.04); }
    .footer { margin-top: 24px; color: #7b8ea3; font-size:0.9rem; text-align:center; }
  </style>
</head>
<body>
  <div class="container">
    <h1>ChatSense — WhatsApp Chat Analyzer</h1>
    <div class="badges">
      <!-- Replace the URLs below with your repo badges or remove if unwanted -->
      <img src="https://img.shields.io/badge/Project-Internship-blue" alt="internship">
      <img src="https://img.shields.io/badge/Language-Python-366a9c" alt="python">
      <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b" alt="streamlit">
    </div>

    <p class="lead">
      ChatSense (developed during an internship at <strong>CodeSpyder</strong>) is an interactive analytics dashboard that
      parses exported WhatsApp chat files and produces conversation insights — user activity, timelines, word frequency, emoji analysis,
      and visual summaries — using Python and Streamlit.
    </p>

    <h2>🔎 Project Summary</h2>
    <p class="muted">Team project — Data Science Interns (3 members) • Duration: 4.5 months</p>
    <ul>
      <li>Ingests exported WhatsApp chat text (.txt) and parses date, time, user, and message using regular expressions.</li>
      <li>Structures messages into a Pandas DataFrame and derives time-based features (date, month, hour, day_name, period).</li>
      <li>Generates visual analytics: monthly/daily timelines, activity heatmaps, word clouds, most active users, and emoji distributions.</li>
      <li>Interactive UI built with Streamlit for easy exploration and per-user / overall analysis.</li>
    </ul>

    <h2>🧰 Tech Stack</h2>
    <div class="grid">
      <div class="card">
        <strong>Languages</strong>
        <p class="muted">Python 3.8+</p>
      </div>
      <div class="card">
        <strong>Libraries</strong>
        <p class="muted">pandas, regex, matplotlib, seaborn, wordcloud, urlextract, emoji, streamlit</p>
      </div>
      <div class="card">
        <strong>Tools</strong>
        <p class="muted">VS Code / Jupyter, Git & GitHub</p>
      </div>
      <div class="card">
        <strong>UI</strong>
        <p class="muted">Streamlit — interactive web dashboard</p>
      </div>
    </div>

    <h2>⚙️ What I (the team) implemented — Technical Details</h2>
    <ul>
      <li><strong>Parsing & Preprocessing</strong>: Used a robust regex to split messages and timestamps, replaced Unicode narrow spaces (U+202F) when needed, and converted timestamps with <code>pandas.to_datetime</code>. The output DataFrame includes <code>user, message, date, only_date, year, month, month_num, day, day_name, hour, minute, period</code>.</li>
      <li><strong>Analytics Functions</strong>: Implemented helper functions to compute message counts, word counts, media counts, link extraction (via <code>urlextract</code>), most active users, monthly/daily timelines (groupby) and activity heatmaps (pivot_table).</li>
      <li><strong>Text Processing</strong>: Built a custom Hinglish stop-words file (<code>stop_hinglish.txt</code>) for meaningful word-clouds and frequency analysis.</li>
      <li><strong>Emoji Handling</strong>: Used the modern <code>emoji.is_emoji()</code> extraction method (compatible with emoji v2+) and produced emoji frequency tables.</li>
      <li><strong>Visualization</strong>: Charts & heatmaps with Matplotlib/Seaborn; WordCloud generation with the <code>wordcloud</code> library; rendered through Streamlit with layout, columns, and metrics for a dashboard feel.</li>
      <li><strong>UI</strong>: Streamlit frontend with sidebar file upload, per-user selection, collapsible sections, and summary metrics (<code>st.metric</code>) for polished presentation.</li>
    </ul>

    <h2>📂 Repository Structure</h2>
    <pre><code>
ChatSense/
├── app.py                  # Streamlit app (UI)
├── preprocessor.py         # parsing and cleaning logic
├── helper.py               # analytics & visualization helper functions
├── stop_hinglish.txt       # custom stop words (Hinglish)
├── requirements.txt
└── README.html
    </code></pre>

    <h2>🚀 Quick Start — Run Locally</h2>
    <p class="muted">Assumes Python 3.8+ installed.</p>
    <pre><code># 1. Create & activate virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
    </code></pre>

    <h2>📂 File Format Notes</h2>
    <p class="muted">The app expects WhatsApp exported chat text in the standard format (example):</p>
    <pre><code>12/20/22, 10:57 AM - Rahul: Hello everyone!
12/20/22, 10:55 AM - System message or group notification...
    </code></pre>
    <p>— The preprocessor handles common mobile formats and deals with Unicode narrow spaces that sometimes appear before AM/PM.</p>

    <h2>🎯 Features</h2>
    <ul>
      <li>Upload a WhatsApp chat export (.txt) and preview parsed messages.</li>
      <li>Overall and per-user analysis: messages, words, media, links.</li>
      <li>Monthly & daily timelines (plots), weekly heatmap, busiest days/months.</li>
      <li>Word cloud and most common words (Hinglish stopwords supported).</li>
      <li>Emoji analysis with frequency table and pie chart.</li>
    </ul>

    <h2>🧪 Unit / Sanity Tests</h2>
    <p class="muted">(Optional) We recommend adding minimal checks:</p>
    <pre><code># sanity_check.py (example)
from preprocessor import preprocess
text = open("sample_chat.txt", "r", encoding="utf-8").read()
df = preprocess(text)
assert "user" in df.columns
assert "message" in df.columns
print("Sanity checks passed")
    </code></pre>

    <h2>🤝 Team & Contribution</h2>
    <p class="muted">Project completed during internship at <strong>CodeSpyder</strong> — team of 3 data science interns. Contributions split across modules:</p>
    <ul>
      <li><strong>Data preprocessing & parsing:</strong> Raj Sonawane (lead)</li>
      <li><strong>Analytics functions & visualization:</strong> Team member 2</li>
      <li><strong>UI & deploy (Streamlit):</strong> Team member 3</li>
    </ul>
    <p class="muted">(Edit names as required before publishing.)</p>

    <h2>📸 Screenshots</h2>
    <p class="muted">Add images/screenshots in the repo and replace the <code>src</code> values below.</p>
    <div class="center">
      <img class="screenshot" src="screenshot-dashboard.png" alt="Dashboard screenshot">
    </div>

    <h2>📄 License</h2>
    <p class="muted">MIT License — feel free to adapt for your portfolio. Add a <code>LICENSE</code> file to the repo when publishing.</p>

    <h2>✉️ Contact</h2>
    <p class="muted">For questions or collaboration — <strong>Raj Sonawane</strong> (<a href="mailto:youremail@example.com">youremail@example.com</a>)</p>

    <div class="footer">
      <p>Built during an internship at <strong>CodeSpyder</strong> • ChatSense — WhatsApp Chat Analyzer</p>
    </div>
  </div>
</body>
</html>
