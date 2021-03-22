import requests
import json

url_API = "http://127.0.0.1:5000/companies"

def get_value_from_esp():
  valor_requisicao = json.loads(requests.get(url_API).content)
  return valor_requisicao["value"]