"""SMTPハンドラーでログをEmail送信"""
import logging
import logging.handlers

import config


smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxx@hotmail.com'
to_email = 'xxx@hotmail.com'
username = 'xxx@hotmail.com'
password = 'gjaiogjha'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log', credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')