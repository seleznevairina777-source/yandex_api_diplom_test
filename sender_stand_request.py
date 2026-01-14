import requests
import configuration
import data

def create_order():
    resp = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)
    return resp

def recieveOrderByTrack(track):
    return requests.get(url = configuration.URL_SERVICE + configuration.RECEIVE_ORDER_PATH,headers=data.headers, params={"t":track})
