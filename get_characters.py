import time
from hashlib import md5
import requests as rq

def get_characters():
  public_key = 'the public key you generated'
  private_key = 'the private key you generated'
  ts = str(time.time())  
  hash_str = md5(f"{ts}{private_key}{public_key}".encode("utf8")).hexdigest()
  
  params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash_str,
        "orderBy": "name",
        "limit":1
    } 
  try:
    r = rq.get('https://gateway.marvel.com:443/v1/public/characters', params=params) 
  except Exception as e:
    print(f'Error: {e}')
  else:
    print(r.json())

get_characters()
