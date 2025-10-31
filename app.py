import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu

# ---------- FONT FIX ----------
try:
    fm.fontManager.addfont("C:/Windows/Fonts/seguiemj.ttf")
    plt.rcParams['font.family'] = 'Segoe UI Emoji'
except:
    plt.rcParams['font.family'] = 'DejaVu Sans'

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="💬 WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    /* App-wide font and layout */
    body {
        font-family: 'Poppins', sans-serif;
    }
    h1, h2, h3 {
        color: #00FFAA;
        font-weight: 600;
    }
    .metric-label {
        font-size: 16px !important;
        color: #E0E0E0 !important;
    }
    .stMetric {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 10px;
    }
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    hr {
        border: 1px solid #333;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("<h1 style='text-align:center; color:#00FA9A;'>💬 WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Analyze your chats in one click 📊</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("📁 Upload your chat text file (.txt)", type=["txt"])
    st.markdown("---")

# ---------- MAIN APP ----------
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # ---------- HEADER ----------
    st.markdown("<h2 style='color:#00BFFF;'>📋 Chat Data Preview</h2>", unsafe_allow_html=True)
    st.dataframe(df.head(10), use_container_width=True)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("🔍 Show analysis for:", user_list)
    analyze = st.sidebar.button("🚀 Run Analysis")

    if analyze:
        st.markdown("<h1 style='text-align:center; color:#32CD32;'>📈 Chat Insights Dashboard</h1>", unsafe_allow_html=True)
        st.markdown("---")

        # ---- Stats Cards ----
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(label="💬 Messages", value=num_messages)
        with col2:
            st.metric(label="📝 Words", value=words)
        with col3:
            st.metric(label="📷 Media Shared", value=num_media_messages)
        with col4:
            st.metric(label="🔗 Links Shared", value=num_links)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Timelines ----
        st.subheader("📆 Monthly Activity Trend")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='#1DB954', linewidth=2)
        plt.xticks(rotation='vertical')
        plt.grid(alpha=0.3)
        st.pyplot(fig, use_container_width=True)

        st.subheader("🗓️ Daily Activity Trend")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='#FFD700', linewidth=2)
        plt.xticks(rotation='vertical')
        plt.grid(alpha=0.3)
        st.pyplot(fig, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Activity Map ----
        st.subheader("📅 Weekly & Monthly Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.caption("🕒 Most Active Days")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            sns.barplot(x=busy_day.index, y=busy_day.values, ax=ax, palette="viridis")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.caption("📆 Most Active Months")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            sns.barplot(x=busy_month.index, y=busy_month.values, ax=ax, palette="plasma")
            plt.xticks(rotation=45)
            st.pyplot(fig)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Heatmap ----
        st.subheader("🔥 Weekly Heatmap")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(user_heatmap, cmap="coolwarm", ax=ax)
        st.pyplot(fig, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Busy Users ----
        if selected_user == 'Overall':
            st.subheader("🏆 Most Active Users")
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                sns.barplot(x=x.index, y=x.values, ax=ax, palette="mako")
                plt.xticks(rotation=45)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Word Cloud ----
        st.subheader("☁️ Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        plt.axis("off")
        st.pyplot(fig, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Common Words ----
        st.subheader("💬 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        sns.barplot(y=most_common_df[0], x=most_common_df[1], ax=ax, palette="crest")
        plt.xlabel("Count")
        plt.ylabel("Word")
        st.pyplot(fig, use_container_width=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # ---- Emoji Analysis ----
        st.subheader("😊 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f%%", textprops={'fontsize': 10})
            st.pyplot(fig)

        st.markdown("<br><p style='text-align:center; color:gray;'>✨ Built by <b>Raj</b> ✨</p>", unsafe_allow_html=True)
