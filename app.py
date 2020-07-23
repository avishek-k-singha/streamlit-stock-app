import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App 
""")

#user input
user_input = st.text_input("Find Out About Stock")

tickerSymbol = user_input

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write(user_input+" Price Chart")
st.line_chart(tickerDf.Close)
st.write(user_input+" Volume Chart")
st.line_chart(tickerDf.Volume)
