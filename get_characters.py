import time
from hashlib import md5
import requests as rq

def get_characters():
  public_key = '9935fbeb4789c8a714bb88719d010dd8'
  private_key = '8afaf1ca9920b71dc97bf4cf3415e4c907ea20cd'
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
    return False, e
  else:
    return r.json()

get_characters()
