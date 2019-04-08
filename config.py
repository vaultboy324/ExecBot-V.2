import json

with open('config.json', 'r') as f:
    data = json.load(f)


class Config():
    TOKEN = data['token']
    PROXY_PROTOCOL = data['proxy']['protocol']
    PROXY_IP = data['proxy']['ip']


class DatabaseConfig:
    DATABASE = data['db_info']['database']
    USER = data['db_info']['user']
    PASSWORD = data['db_info']['password']
    HOST = data['db_info']['host']