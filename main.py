import streamlit as st
import pandas as pd
from tradingview_ta import TA_Handler, Interval, Exchange 

st.title("Technical Analysis")
st.markdown(
	'''
	<style>
	[data-testid='sidebar'][aria-expanded='true'] > div:firstchild{width:400px}
	[data-testid='sidebar'][aria-expanded='false'] > div:firstchild{width:400px , margin-left: -400px}
	</style>
	''',
	unsafe_allow_html=True
)

st.markdown('---')
symbol = st.text_input('symobl', 'AAPL')
screener = st.text_input('screener', 'america')
exchange = st.text_input('exchange', 'NASDAQ')
interval = st.selectbox('interval', ['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w', '1M'])
if interval == '1m':
    interval = Interval.INTERVAL_1_MINUTE
elif interval == '5m':
    interval = Interval.INTERVAL_5_MINUTE
elif interval == '15m':
    interval = Interval.INTERVAL_15_MINUTE
elif interval == '30m':
    interval = Interval.INTERVAL_30_MINUTE
elif interval == '1h':
    interval = Interval.INTERVAL_1_HOUR
elif interval == '4h':
    interval = Interval.INTERVAL_4_HOUR
elif interval == '1d':
    interval = Interval.INTERVAL_1_DAY
elif interval == '1w':
    interval = Interval.INTERVAL_1_WEEK
elif interval == '1M':
    interval = Interval.INTERVAL_1_MONTH
SUDMIT = st.button('SUBMIT')
st.markdown('---')
if SUDMIT:
    tesla = TA_Handler(
        symbol=symbol,
        screener=screener,
        exchange=exchange,
        interval=interval,
        # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
    )
    print(tesla.get_analysis().summary)
    st.title('Prediction')
    st.write(tesla.get_analysis().summary)
    st.title('Info')
    basic = {'symbol':tesla.symbol,'Exchange':tesla.exchange,'interval':tesla.interval,'open':tesla.get_analysis().indicators['open'],'close':tesla.get_analysis().indicators['close'],'high':tesla.get_analysis().indicators['high'],'low':tesla.get_analysis().indicators['low'],'volume':tesla.get_analysis().indicators['volume']}
    basic = pd.DataFrame(basic, index=[0])
    st.dataframe(basic)
    inidicators = pd.DataFrame(tesla.get_analysis().oscillators['COMPUTE'], index=[0])
    st.title('Indicators')
    st.dataframe(inidicators)
    moving_avg = inidicators = pd.DataFrame(tesla.get_analysis().moving_averages['COMPUTE'], index=[0])
    st.title('Moving Averages')
    st.dataframe(moving_avg)
    oth = {'BUY PRICE':tesla.get_analysis().indicators['close'],'STOP LOSS':tesla.get_analysis().indicators['open']}
    oth = pd.DataFrame(oth, index=[0])
    st.title('RECOMANDATIONS')
    st.dataframe(oth)
    st.markdown('---')




