import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys
from time import sleep

import requests
import json

from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

from opcua import ua, uamethod, Server

# Colocar a Url que o esp esta rodando a api -------------------------------------------------------------------------------------------------------
url_API_esp = "http://127.0.0.1:5000/companies"
# Colocar o ID do JSON que representa o valor ------------------------------------------------------------------------------------------------------
id_json = "value"

def get_value_from_esp():
  valor_requisicao = json.loads(requests.get(url_API_esp).content)
  return valor_requisicao[id_json]

if __name__ == "__main__":
  logging.basicConfig(level=logging.WARN)

  # now setup our server
  server = Server()
  
  server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
  server.set_server_name("FreeOpcUa Example Server")
  
  server.set_security_policy([ ua.SecurityPolicyType.NoSecurity, ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt, ua.SecurityPolicyType.Basic256Sha256_Sign])

  # setup our own namespace
  uri = "http://examples.freeopcua.github.io"
  idx = server.register_namespace(uri)

  objects = server.get_objects_node()

  rfidsens = objects.add_object('ns=2;s="RFID1"' , "RFID Sensor 1")


  rfidsens.add_variable('ns=2;s="RFID1_VendorName"', "RFID1 Vendor Name", "Sensor King")

  rfidsens.add_variable('ns=2;s="RFID1_SerialNumber"', "RFID1 Serial Number", 986532)

  id_rfid = rfidsens.add_variable('ns=2;s="RFID1_RFID"', "RFID1 ID RFID", 0)

  bulb = objects.add_object(2, "Light Bulb")
  bulb

  state = bulb.add_variable(2, "State of Light Bulb", False)
  state

  state.set_writable()

  try:
    print("Start Server")
    server.start()
    print("Server Oline")
    while True:
      id_rfid.set_value(get_value_from_esp())
      print("New ID: " + str(id_rfid.get_value()))
      print("State of Light Bulb: " + str(state.get_value()))
      sleep(2)
  finally:
    server.stop()
    print("Server Offline")
