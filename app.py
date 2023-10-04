import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("FX Converter")

# Get the list of available currencies from Frankfurter
currency_list =  get_currencies_list()
# If the list of available currencies is None, display an error message in Streamlit App
if currency_list is None:
    st.error("Empty Currency List")

# Add input fields for capturing amount, from and to currencies

amount = st.number_input('Amount to be converted', min_value = 0.1)
from_curr = st.selectbox('From Currency', currency_list)
to_curr = st.selectbox('To Currency',currency_list)


# Add a button to get and display the latest rate for selected currencies and amount
if st.button('Get Latest Rate'):
    if from_curr == to_curr:
        st.text("Select a different currency to convert")
    else:    
        latest_date , latest_rate = get_latest_rates(from_currency= from_curr , to_currency= to_curr , amount= amount)
        latest_amount = round_rate(latest_rate)
        latest_rate = round_rate(latest_rate/amount)
        inverse_rate = reverse_rate(latest_rate)
        result = format_output(latest_date,from_curr,to_curr,latest_rate,latest_amount)
        st.header("Latest Conversion rate")
        st.markdown(result)

# Add a date selector (calendar)
historical_date = st.date_input('Select Date', datetime.date.today())

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button('Get Historical Rate'):
    if from_curr == to_curr:
        st.text("Select a different currency to convert")
    else:

        historical_rate = get_historical_rate(from_currency= from_curr , to_currency= to_curr ,from_date = historical_date, amount= amount)
        if historical_rate is not None:
            historical_amount = round_rate(historical_rate)
            historical_rate = round_rate(historical_rate/amount)
            inverse_historical_rate = reverse_rate(historical_rate)
            result = format_output(historical_date,from_curr,to_curr,historical_rate,historical_amount)
            st.header("Conversion rate")
            # st.text(result)
            st.markdown(result)
