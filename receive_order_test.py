#Ирина Селезнева 39 когорта - финальный проект. Инжинер по тестированию
import pytest
import sender_stand_request
import data

      
def test_order():
    resp = sender_stand_request.create_order()
    orderTrack = resp.json()["track"]
    r = sender_stand_request.recieveOrderByTrack(orderTrack)
    r.status_code == 200