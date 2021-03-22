import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys
from time import sleep

import random

from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

from opcua import ua, uamethod, Server

if __name__ == "__main__":
  # optional: setup logging
  logging.basicConfig(level=logging.WARN)
  #logger = logging.getLogger("opcua.address_space")
  # logger.setLevel(logging.DEBUG)
  #logger = logging.getLogger("opcua.internal_server")
  # logger.setLevel(logging.DEBUG)
  #logger = logging.getLogger("opcua.binary_server_asyncio")
  # logger.setLevel(logging.DEBUG)
  #logger = logging.getLogger("opcua.uaprocessor")
  # logger.setLevel(logging.DEBUG)

  # now setup our server
  server = Server()
  #server.disable_clock()
  #server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
  server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
  server.set_server_name("FreeOpcUa Example Server")
  # set all possible endpoint policies for clients to connect through
  server.set_security_policy([ ua.SecurityPolicyType.NoSecurity, ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt, ua.SecurityPolicyType.Basic256Sha256_Sign])

  # setup our own namespace
  uri = "http://examples.freeopcua.github.io"
  idx = server.register_namespace(uri)

  objects = server.get_objects_node()

  tempsens = objects.add_object('ns=2;s="TS1"' , "Temperature Sensor 1")


  tempsens.add_variable('ns=2;s="TS1_VendorName"', "TS1 Vendor Name", "Sensor King")

  tempsens.add_variable('ns=2;s="TS1_SerialNumber"', "TS1 Serial Number", 123456789)

  temp = tempsens.add_variable('ns=2;s="TS1_Temperature"', "TS1 Temperature", 20)

  bulb = objects.add_object(2, "Light Bulb")
  bulb

  state = bulb.add_variable(2, "State of Light Bulb", False)
  state

  state.set_writable()

  temperature = 20.0
  try:
    print("Start Server")
    server.start()
    print("Server Oline")
    while True:
      temperature += random.uniform(-1, 1)
      temp.set_value(temperature)
      print("New Temperature: " + str(temp.get_value()))
      print("State of Light Bulb: " + str(state.get_value()))
      sleep(2)
  finally:
    server.stop()
    print("Server Offline")
