import os
import ProxyCloud

#Bot Config
BOT_TOKEN = os.environ.get('bot_token')

#Storage Config
BASE_ROOT_PATH = 'root/'

#Account Config
OWN_USER = os.environ.get('account_user')
OWN_PASSWORD = os.environ.get('account_password')
OWN_HOST = os.environ.get('host','https://misarchivos.uci.cu/owncloud/')

# Proxy Config
PROXY_OBJ = ProxyCloud.parse(os.environ.get('proxy_enc'))
#PROXY_OBJ = ProxyCloud.parse('socks5://KHDEKJYEJJJKGIYDJHGFGEYHKKFJEGRIDHLIDILD')


if PROXY_OBJ:
    print(f"PROXY :{PROXY_OBJ.ip}:{PROXY_OBJ.port}")
