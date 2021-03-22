import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys
from time import sleep

from time import sleep
import random
from opcua import Server

from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

# try:
#   from IPython import embed
# except ImportError:
#   import code

#   def embed():
#     myvars = globals()
#     myvars.update(locals())
#     shell = code.InteractiveConsole(myvars)
#     shell.interact()

from opcua import ua, uamethod, Server


# class SubHandler(object):
#   """
#   Subscription Handler. To receive events from server for a subscription
#   """

#   def datachange_notification(self, node, val, data):
#     print("Python: New data change event", node, val)

#   def event_notification(self, event):
#     print("Python: New event", event)


# method to be exposed through server

# def func(parent, variant):
#   ret = False
#   if variant.Value % 2 == 0:
#     ret = True
#   return [ua.Variant(ret, ua.VariantType.Boolean)]


# method to be exposed through server
# uses a decorator to automatically convert to and from variants

# @uamethod
# def multiply(parent, x, y):
#   print("multiply method call with parameters: ", x, y)
#   return x * y


# class VarUpdater(Thread):
#   def __init__(self, var):
#     Thread.__init__(self)
#     self._stopev = False
#     self.var = var

#   def stop(self):
#     self._stopev = True

#   def run(self):
#     while not self._stopev:
#       v = sin(time.time() / 10)
#       self.var.set_value(v)
#       time.sleep(0.1)


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

  # # create a new node type we can instantiate in our address space
  # dev = server.nodes.base_object_type.add_object_type(idx, "MyDevice")
  # dev.add_variable(idx, "sensor1", 1.0).set_modelling_rule(True)
  # dev.add_property(idx, "device_id", "0340").set_modelling_rule(True)
  # ctrl = dev.add_object(idx, "controller")
  # ctrl.set_modelling_rule(True)
  # ctrl.add_property(idx, "state", "Idle").set_modelling_rule(True)

  # # populating our address space

  # # First a folder to organise our nodes
  # myfolder = server.nodes.objects.add_folder(idx, "myEmptyFolder")
  # # instanciate one instance of our device
  # mydevice = server.nodes.objects.add_object(idx, "Device0001", dev)
  # mydevice_var = mydevice.get_child(["{}:controller".format(idx), "{}:state".format(idx)])  # get proxy to our device state variable 
  # # create directly some objects and variables
  # myobj = server.nodes.objects.add_object(idx, "MyObject")
  # myvar = myobj.add_variable(idx, "MyVariable", 6.7)
  # mysin = myobj.add_variable(idx, "MySin", 0, ua.VariantType.Float)
  # myvar.set_writable()    # Set MyVariable to be writable by clients
  # mystringvar = myobj.add_variable(idx, "MyStringVariable", "Really nice string")
  # mystringvar.set_writable()  # Set MyVariable to be writable by clients
  # myguidvar = myobj.add_variable(NodeId(uuid.UUID('1be5ba38-d004-46bd-aa3a-b5b87940c698'), idx, NodeIdType.Guid), 'MyStringVariableWithGUID', 'NodeId type is guid')
  # mydtvar = myobj.add_variable(idx, "MyDateTimeVar", datetime.utcnow())
  # mydtvar.set_writable()    # Set MyVariable to be writable by clients
  # myarrayvar = myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
  # myarrayvar = myobj.add_variable(idx, "myStronglytTypedVariable", ua.Variant([], ua.VariantType.UInt32))
  # myprop = myobj.add_property(idx, "myproperty", "I am a property")
  # # mymethod = myobj.add_method(idx, "mymethod", func, [ua.VariantType.Int64], [ua.VariantType.Boolean])
  # # multiply_node = myobj.add_method(idx, "multiply", multiply, [ua.VariantType.Int64, ua.VariantType.Int64], [ua.VariantType.Int64])

  # # starting!
  # server.start()
  # print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
  # # vup = VarUpdater(mysin)  # just  a stupide class update a variable
  # # vup.start()
  # try:
  #   # enable following if you want to subscribe to nodes on server side
  #   #handler = SubHandler()
  #   #sub = server.create_subscription(500, handler)
  #   #handle = sub.subscribe_data_change(myvar)
  #   # trigger event, all subscribed clients wil receive it
  #   var = myarrayvar.get_value()  # return a ref to value in db server side! not a copy!
  #   var = copy.copy(var)  # WARNING: we need to copy before writting again otherwise no data change event will be generated
  #   var.append(9.3)
  #   myarrayvar.set_value(var)
  #   mydevice_var.set_value("Running")
  #   # myevgen.trigger(message="This is BaseEvent")
  #   server.set_attribute_value(myvar.nodeid, ua.DataValue(9.9))  # Server side write method which is a but faster than using set_value
  #   while True:
  #     print("Fala algo, cabeça!")
  #     sleep(2)
  #   # embed()
  # finally:
  #   # vup.stop()
  #   server.stop()

  objects = server.get_objects_node()
objects
tempsens = objects.add_object('ns=2;s="TS1"' , "Temperature Sensor 1")
tempsens

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
