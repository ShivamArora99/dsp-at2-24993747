def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    if rate is not None:
        return round(rate,4)
    else:
        return 0
    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate is not None:
        return round(1/rate , 4)
    else:
        return 0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    # if rate is not None:
    #     return round(1/rate , 4)
    # else:
    #     return 0
    if rate is not None and rate != 0:
        inverse_rate = reverse_rate(rate)
        amount_input = round_rate(amount/rate)
        return (f'The conversion rate on {date} from {from_currency} to {to_currency} is {rate}. So {amount_input} in {from_currency} corresponds to {amount} in {to_currency}. The inverse was {inverse_rate}. ')
    else:
        return ("None")

    

   