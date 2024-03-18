import requests
import random
import string
import concurrent.futures 
import json
from colorama import init, Fore, Style
from datetime import datetime

url = 'https://www.guilded.gg/api/users'

with open('config.json') as c:
    config = json.load(c)
    threads = config['threads']  

def generate_random_string(length, chars=string.ascii_letters + string.digits + '@$'):
    return ''.join(random.choice(chars) for _ in range(length))

def main(url):
    name = generate_random_string(8, string.ascii_letters)
    email = f'{generate_random_string(8, string.ascii_letters)}@gmail.com'
    password = generate_random_string(9, string.ascii_letters + string.digits + '@$')
    fullname = generate_random_string(8, string.ascii_letters)
    time = datetime.now().strftime("%H:%M:%S")

    headers = {
        'authority': 'www.guilded.gg',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'guilded-viewer-platform': 'desktop',
        'origin': 'https://www.guilded.gg',
        'referer': 'https://www.guilded.gg/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    parameters = {
        'type': 'email',}

    data = {
        'extraInfo': {
            'platform': 'desktop',
        },
        'name': name,
        'email': email,
        'password': password,
        'fullName': fullname,
    }

    response = requests.post(url, params=parameters, headers=headers, json=data)
    uid = response.json()['user']['id']
    print(f"{Fore.YELLOW}[ {time} ]{Style.RESET_ALL} {Fore.GREEN}Created Account{Style.RESET_ALL} | UserID: {Fore.BLUE}{uid}{Style.RESET_ALL}")

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    while True:
        arguments = [url] * threads
        executor.map(main, arguments)