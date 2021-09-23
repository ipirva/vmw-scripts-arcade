#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import os
from dotenv import load_dotenv

def f_check_env_variables(var: list = None) -> dict:
    '''
        If input var is defined, the function will return the value of each env var variable
        If input var is None, the function will return all the env variables
    '''

    output = {}

    # load extra env vars
    load_dotenv()

    if type(var) == list and len(var) == 0:
        var = None
    if type(var) != list:
        var = None

    if var is None:
        envKeys = dict(os.environ)
        for key in envKeys:
            output[key] = envKeys[key]
    
    if type(var) == list and len(var) > 0:
        for key in var:
            output[key] = os.getenv(key, None)
        
    # output[0] = os.getenv('SECURITYSESSIONID', None)

    return output