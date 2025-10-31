import requests
import random
import time
from fake_useragent import UserAgent

def spam_ngl(target_url, jumlah_spam, pesan_spam, proxy=None):
    """
    Tools Spam NGL Super Ampuh dengan Proxy 🔥🔥🔥

    Args:
        target_url (str): URL NGL target.
        jumlah_spam (int): Jumlah spam yang mau dikirim.
        pesan_spam (str): Pesan spam yang mau dikirim.
        proxy (str, optional): Alamat proxy (contoh: 'http://10.10.1.10:3128'). Defaults to None.
    """
    ua = UserAgent()
    proxies = {'http': proxy, 'https': proxy} if proxy else None

    try:
        for i in range(jumlah_spam):
            identifier = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
            data = {
                'question': pesan_spam,
                'username': identifier
            }
            headers = {'User-Agent': ua.random}

            try:
                response = requests.post(target_url, data=data, headers=headers, proxies=proxies, timeout=10)

                if response.status_code == 200:
                    print(f"[{i+1}/{jumlah_spam}] Spam berhasil dikirim! 🔥")
                else:
                    print(f"[{i+1}/{jumlah_spam}] Gagal kirim spam. Status code: {response.status_code} 💩")

            except requests.exceptions.RequestException as e:
                print(f"Error saat kirim request: {e} 💥")

            time.sleep(random.uniform(1, 3)) # Delay lebih lama

    except Exception as e:
        print(f"Unexpected error: {e} 💥")

if __name__ == "__main__":
    target = input("Masukkan URL NGL target: ")
    jumlah = int(input("Masukkan jumlah spam yang mau dikirim: "))
    pesan = input("Masukkan pesan spam: ")
    proxy = input("Masukkan alamat proxy (opsional, contoh: http://10.10.1.10:3128): ")

    spam_ngl(target, jumlah, pesan, proxy)

    print("Selesai! Semoga target lo makin emosi! 😈")
