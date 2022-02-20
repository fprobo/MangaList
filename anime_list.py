import requests
from alive_progress import alive_bar
import time

URL = 'https://api.jikan.moe/v4/manga/'
headers = {
	'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2,pt;q=0.2',
	'Connection':'keep-alive',
	'Host':'api.jikan.moe',
	'Origin':'https://jikan.moe',
	'Referer':'https://jikan.moe/',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}

# print(requests.get(URL, headers=headers).json())


with open('ids.txt') as file:
    lines = file.readlines()

tick = 1 if len(lines) > 60 else 0.5

with open('data.txt', 'w') as f:
    with alive_bar(len(lines), force_tty=True) as bar:
	    for x in lines:
            f.write(requests.get(URL + x, headers=headers).json())
		    time.sleep(tick)
		    bar()
