#!env01/Scripts/python3
"""
這是一個report的module
"""

def get_description():
    """
    return random weather, jusk like the pros
    """
    from random import choice
    print("report.py的__name__=", __name__)
    possibilities = ['rain', 'snow', 'fog', 'sun', 'who knows']
    return choice(possibilities)