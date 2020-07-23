import yfinance as yf
import streamlit as st
import datetime

st.write("""
# Simple Stock Price App 
""")

#user input
user_input = st.sidebar.text_input("Enter the stock ticker symbol")

d1 = st.sidebar.date_input(" Start Date", datetime.date(2010, 1, 1))
d2 = st.sidebar.date_input(" End Date", datetime.date(2020, 7,24))
time = st.sidebar.selectbox(
    'Time interval',
    ('1mo','1wk', '5d','1d')
)

#get data on this ticker
tickerData = yf.Ticker(user_input)
#get the historical prices for this ticker
tickerDf = tickerData.history(interval=time,start=d1,end=d2)
st.write(user_input+f" Price Chart from {d1} to {d2}")
st.line_chart(tickerDf.Close)
st.write(user_input+f" Volume Chart from {d1} to {d2}")
st.line_chart(tickerDf.Volume)
