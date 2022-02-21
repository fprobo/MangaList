import requests
from alive_progress import alive_bar
import time

URL = 'https://api.jikan.moe/v4/manga/'
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}

with open('list.txt') as file:
    lines = file.read().splitlines()

tick = 1 if len(lines) > 60 else 0.5

with open('data.json', 'w') as f:
    with alive_bar(len(lines), force_tty=True) as bar:
        f.write('[')
        for x in lines:
            f.write(requests.get(URL + x, headers=headers).text)
            if x != lines[-1]:
                f.write(',')
            time.sleep(tick)
            bar()
        f.write(']')
        
