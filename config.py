import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('-1002190822875', '').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')
PICS = (environ.get('PICS', 'https://telegra.ph/file/748417f096140e5e1a8cc.jpg https://telegra.ph/file/748417f096140e5e1a8cc.jpg')).split() # Bot Start Picture
