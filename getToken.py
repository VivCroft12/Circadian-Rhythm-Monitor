import os
import time
import json 

import iot_api_client as iot

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import numpy as np
import pandas as pd


#CLIENT_ID = os.getenv("CLIENT_ID")  # get a valid one from your Arduino Create account
#CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # get a valid one from your Arduino Create account

def startApi():
    CLIENT_ID = "OJDD9Vl0SjBFF1GhkLZg2LlKfTm6nqwK"
    CLIENT_SECRET = "4yYtn7dZyPI8xsNbEdoNJaiXgspP3scPzf6rS7WY8AUxJ4qPfAzJoqEeZ2pdifvK"
    # Setup the OAuth2 session that'll be used to request the server an access token
    oauth_client = BackendApplicationClient(client_id=CLIENT_ID)
    token_url = "https://api2.arduino.cc/iot/v1/clients/token"
    oauth = OAuth2Session(client=oauth_client)

    # This will fire an actual HTTP call to the server to exchange client_id and
    # client_secret with a fresh access token
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        include_client_id=True,
        audience="https://api2.arduino.cc/iot",
    )

    # If we get here we got the token, print its expiration time
    print("Got a token, expires in {} seconds".format(token.get("expires_in")))

    # Now we setup the iot-api Python client, first of all create a
    # configuration object. The access token goes in the config object.
    client_config = iot.Configuration(host="https://api2.arduino.cc/iot")
    # client_config.debug = True
    client_config.access_token = token.get("access_token")    
    return client_config

def getBPMValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","a3cc6cfb-49c4-4d61-a44c-1909afe3488d")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value
    
def getTempValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","c6e6da6f-811e-40d5-97db-5d203987d503")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getLightValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","60658a36-9bd1-4cad-8647-622047236f26")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getDeepSleepValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","d5d33521-ea78-40f5-83af-f19b8c95d1e7")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getLightSleepValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","59c34d29-1056-41de-b9b9-08bf51d0ea21")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getTotalSleepValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","39acfd58-8614-42ff-a431-538f6c7905a9")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getBodyTempValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","074945c1-8df0-484a-aa70-87ff5a418adc")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getHumidityValue(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)
    properties = iot.PropertiesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        #print(resp)
        temp = properties.properties_v2_show("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","f28c4643-28e4-4c36-b899-a9df041bfdec")
        print(temp.last_value)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return temp.last_value

def getCfiValue(x,client_config):
    #put code here
    #return the final cfi value

    #IS code
    new_x = x.T
    new_x1 = new_x[[0,1,2]]
    #print(new_x1)
    final_x = new_x1.T
    p = len(final_x.columns)
    xh = final_x.mean()
    v = np.array(final_x.T)
    n = v.size
    numerator = np.sum(np.power((xh - np.mean(v)),2))/p
    denominator = np.sum(np.power((v - np.mean(v)),2))/n
    ISValue = (numerator/denominator)

    #IV code
    y = x.transpose()
    temp = np.array(y[0])
    index = [0, 1, 2]
    new_y = np.delete(temp, index)
    mean = np.mean(new_y)
    numerator = np.sum(np.power(np.diff(new_y),2))/(new_y.size - 1)
    denominator = np.sum(np.power((new_y - mean), 2))/new_y.size
    IVValue = numerator/denominator
    normalizedIV = 1 - (IVValue/2)
    print(normalizedIV)

    cfi = (normalizedIV + ISValue + 1 )/3

    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)
    properties = iot.PropertiesV2Api(client)

    try:
        properties.properties_v2_publish("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","89113216-ebb2-4094-bbe2-c095c0f85136",{'device_id':"746fb130-b167-472b-9ddf-f838be4723c8",'value':cfi})

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return cfi

def getCsv():
    x = pd.read_csv('example_activity_data.csv')
    return x 

def sendCFI(client_config):
    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)
    properties = iot.PropertiesV2Api(client)

    try:
        properties.properties_v2_publish("e7edd0ba-f0c9-4329-92ce-82dd7524c2a5","89113216-ebb2-4094-bbe2-c095c0f85136",20)

    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))

    return True


"""
added a variable to the main code
added a variable to the dashboard
added a button function
added a printCFI function
"""