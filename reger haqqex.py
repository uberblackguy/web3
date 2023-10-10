import time
import requests
from pypasser import reCaptchaV3
import random
import string
from faker import Faker
import re
import json
import os

def random_name():
    fake = Faker()
    name = fake.first_name()
    last_name = fake.last_name()
    return name, last_name

def generate_nickname(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
ref = input("ВВедите ваш реферальный код: ")

num_repeats = int(input("Введите количество аккаунтов: "))

mail_folder = 'saved_emails'
os.makedirs(mail_folder, exist_ok=True)

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
emails_file_path = os.path.join(desktop_path, 'emails.txt')

proxies_file_path = 'proxies.txt'
proxies_list = []

with open(proxies_file_path, 'r') as proxies_file:
    proxies_list = proxies_file.read().splitlines()



current_proxy_index = 0

for _ in range(num_repeats):
    Ip = proxies_list[current_proxy_index]



    proxies = {
        'http': f'socks5://{Ip}',
        'https': f'socks5://{Ip}'
    }

    nickname = generate_nickname()
    headers = {
        'authority': 'tempmail.plus',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://tempmail.plus/ru/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX 03)',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'email': f'{nickname}@mailto.plus',
        'limit': '20',
        'epin': '',
    }

    response = requests.get('https://tempmail.plus/api/mails', params=params, headers=headers, proxies=proxies)

    print(f"{nickname}@mailto.plus")

    captcha = reCaptchaV3(anchor_url='https://www.google.com/recaptcha/api2/anchor?ar=2&k=6LcNuCUjAAAAAF0xFJbMAHQae8BUFRLXB8kP1Wca&co=aHR0cHM6Ly9oYXFxZXguY29tOjQ0Mw..&hl=ru&v=lLirU0na9roYU3wDDisGJEVT&size=invisible&cb=txkcaiehzxg2')

    headers = {
        'authority': 'backend.prod.haqqex.tech',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://haqqex.com',
        'referer': 'https://haqqex.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX 03)',
        'x-captcha-token': captcha,
    }

    json_data = {
        'firstName': random_name()[0],
        'lastName': random_name()[1],
        'email': f'{nickname}@mailto.plus',
        'password': 'DenisPidaras1990!',
    }

    response = requests.post(
        f'https://backend.prod.haqqex.tech/account/api/v1/registration/{ref}',
        headers=headers,
        json=json_data,
    )

    time.sleep(15)

    headers = {
        'authority': 'tempmail.plus',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://tempmail.plus/ru/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX 03)',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get('https://tempmail.plus/api/mails', params=params, headers=headers, proxies=proxies)

    id_js = json.loads(response.text)
    id = id_js["last_id"]

    params = {
        'email': f'{nickname}@mailto.plus',
        'epin': '',
    }

    response = requests.get(f'https://tempmail.plus/api/mails/{id}', params=params, headers=headers, proxies=proxies)

    ff = response.json()["text"]
    s = re.search(r'https://haqqex.com/confirm-registration/(.+?) ', ff)
    s = s.group(1)

    headers = {
        'authority': 'backend.prod.haqqex.tech',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://haqqex.com',
        'referer': 'https://haqqex.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX 03)',
    }

    json_data = {
        'token': s,
    }

    response = requests.post('https://backend.prod.haqqex.tech/account/api/v1/registration/confirm', headers=headers, json=json_data, proxies=proxies)

    current_proxy_index += 1
    if current_proxy_index >= len(proxies_list):
        current_proxy_index = 0


    print(response.text)

    with open(emails_file_path, 'a') as email_file:
        email_file.write(f'{nickname}@mailto.plus\n')
