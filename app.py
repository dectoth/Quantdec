
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up page config
st.set_page_config(page_title="QuantDec", layout="wide")

# Sidebar
st.sidebar.image("https://quantdec.streamlit.app/favicon.png", use_column_width=True)
st.sidebar.title("QuantDec")
page = st.sidebar.radio("Navigate", ["Home", "Strategy Builder", "Trading Simulator", "Performance Dashboard"])

# Home Page
if page == "Home":
    st.title("Welcome to QuantDec")
    st.markdown("### Your quantitative trading simulator and strategy builder.")
    st.image("https://images.unsplash.com/photo-1624996752380-8ec242e0f85b", caption="Quantitative Finance in Action", use_column_width=True)
    st.write("Use the sidebar to navigate through strategy building, simulation, and performance dashboards.")

# Strategy Builder
elif page == "Strategy Builder":
    st.title("📈 Strategy Builder")

    st.markdown("Define your strategy parameters:")
    short_window = st.slider("Short Moving Average Window", 5, 50, 20)
    long_window = st.slider("Long Moving Average Window", 50, 200, 100)

    st.write("Generating simulated price data...")
    np.random.seed(42)
    price = np.cumsum(np.random.randn(500)) + 100
    df = pd.DataFrame({"Price": price})
    df["SMA_Short"] = df["Price"].rolling(window=short_window).mean()
    df["SMA_Long"] = df["Price"].rolling(window=long_window).mean()

    st.line_chart(df)

# Trading Simulator
elif page == "Trading Simulator":
    st.title("⚙️ Trading Simulator")

    initial_balance = st.number_input("Initial Balance", 1000, 1000000, 10000)
    trade_size = st.number_input("Trade Size", 100, 10000, 1000)

    st.write("Simulating 100 trades with random PnL outcomes...")
    trades = np.random.normal(0, 1, 100)
    cumulative_pnl = np.cumsum(trades * trade_size)
    balance = initial_balance + cumulative_pnl

    fig, ax = plt.subplots()
    ax.plot(balance, label="Account Balance")
    ax.set_xlabel("Trade #")
    ax.set_ylabel("Balance")
    ax.set_title("Simulated Trading Balance Over Time")
    ax.legend()
    st.pyplot(fig)

# Performance Dashboard
elif page == "Performance Dashboard":
    st.title("📊 Performance Dashboard")

    st.markdown("Here’s a summary of key metrics:")

    pnl = np.random.normal(0, 1, 1000)
    cumulative_returns = np.cumsum(pnl)
    sharpe_ratio = np.mean(pnl) / np.std(pnl) * np.sqrt(252)
    max_drawdown = np.min(cumulative_returns - np.maximum.accumulate(cumulative_returns))

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Return", f"{cumulative_returns[-1]:.2f}")
    col2.metric("Sharpe Ratio", f"{sharpe_ratio:.2f}")
    col3.metric("Max Drawdown", f"{max_drawdown:.2f}")

    st.line_chart(cumulative_returns)
