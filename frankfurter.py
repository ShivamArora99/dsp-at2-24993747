from api import get_url
import json

BASE_URL = 'https://api.frankfurter.app'
LATEST = '/latest'

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    status_code , response = get_url(BASE_URL + '/currencies')
    if status_code == 200:
        currencies = response.json()
        return list(currencies.keys())
    else:
        return response.text

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    latest_rate_url = BASE_URL + LATEST +'?amount='+ str(amount) + '&from=' + str(from_currency) + '&to=' + str(to_currency)
    status_code , response = get_url(latest_rate_url)
    if status_code == 200:
        latest_curr_data =  response.json()
        return latest_curr_data['date'] , latest_curr_data['rates'][to_currency]
    else:
        response.text



def get_historical_rate(from_currency , to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    hist_date = '/' + str(from_date)
    historical_rate_url = BASE_URL + hist_date +'?amount='+ str(amount) + '&from=' + str(from_currency) + '&to=' + str(to_currency)
    status_code , response = get_url(historical_rate_url)
    if status_code == 200:
        historical_data = response.json()
        return historical_data['rates'][to_currency]
    else:
        return historical_data.text