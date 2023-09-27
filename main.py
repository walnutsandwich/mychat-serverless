# -*- coding: utf-8 -*-

from os import getenv
from mypandora_cloud.server import ChatBot

# _port = getenv('PORT')
_port = "8019"
_proxy = getenv('PANDORA_PROXY')
_debug = getenv('PANDORA_DEBUG', 'false').lower() == 'true'
_sentry = getenv('PANDORA_SENTRY', 'false').lower() == 'true'
_listen = getenv('PANDORA_SERVER_LISTEN', 'true').lower() == 'true'
_server = getenv('PANDORA_SERVER', '0.0.0.0:{}'.format(_port) if _port else '0.0.0.0')
# _server = '127.0.0.1'
app = ChatBot(proxy=_proxy, debug=_debug, sentry=_sentry, login_local=True).run(_server, listen=_listen)
