import streamlit as st
import yfinance as yf
import datetime

st.header('Stock Market Analyser')

#textboxes

ticker_symbols = st.text_input("Enter Stock symbol","AAPL",key="placeholder")
ticker_data = yf.Ticker(ticker_symbols)

#Date input

col1 , col2 = st.columns(2)

with col1:
    st.header("starting date")
    start_date = st.date_input("input starting date",datetime.date(2019,1,1))

with col2:
    st.header("Ending date")
    end_date = st.date_input("input ending date",datetime.date(2025,1,1))

ticker_df = ticker_data.history(start=f'{start_date}',end=f'{end_date}')

dicter = {'AAPL':'APPLE','GOOG':'GOOGLE'}

st.write(f"""{dicter[ticker_symbols]}stock price analysis:""")
st.dataframe(ticker_df)

col1,col2 = st.columns(2)

with col1:
    st.header("volume analysis")
    st.line_chart(ticker_df['Volume'])

with col2:
    st.header("closing price analysis")
    st.line_chart(ticker_df['Close'])