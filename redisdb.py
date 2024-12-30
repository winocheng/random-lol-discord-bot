import json
import os
import redis
from scraper import getChampList

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def get(key: str):
    value = r.get(key)
    if value is None:
        value = getChampList(key)
        dayInSec = 60*60*24
        r.set(key, json.dumps(value), ex=dayInSec)
        return value
    
    return json.loads(value)
    