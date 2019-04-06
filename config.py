import json

with open('config.json', 'r') as f:
    data = json.load(f)

class Config():
    TOKEN = data['token']
    PROXY_PROTOCOL = data['proxy']['protocol']
    PROXY_IP = data['proxy']['ip']