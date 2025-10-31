import requests
import random
import time
from fake_useragent import UserAgent

def spam_ngl(target_url, jumlah_spam, pesan_spam):
    """
    Tools Spam NGL Super Ampuh 🔥🔥🔥

    Args:
        target_url (str): URL NGL target.
        jumlah_spam (int): Jumlah spam yang mau dikirim.
        pesan_spam (str): Pesan spam yang mau dikirim.
    """
    # Inisialisasi UserAgent
    ua = UserAgent()
    
    try:
        for i in range(jumlah_spam):
            # Generate random string buat identifier (biar gak gampang ke-detect)
            identifier = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))

            # Data yang mau dikirim ke NGL (sesuaikan sama struktur request NGL)
            data = {
                'question': pesan_spam,
                'username': identifier  # Pake identifier random
            }

            # Generate random User-Agent untuk setiap request
            headers = {'User-Agent': ua.random}

            # Kirim request ke NGL dengan headers
            response = requests.post(target_url, data=data, headers=headers)

            # Cek status code (200 berarti sukses)
            if response.status_code == 200:
                print(f"[{i+1}/{jumlah_spam}] Spam berhasil dikirim! 🔥")
            else:
                print(f"[{i+1}/{jumlah_spam}] Gagal kirim spam. Status code: {response.status_code} 💩")

            # Kasih jeda biar gak terlalu ngebut (biar gak kena block)
            time.sleep(random.uniform(0.5, 1.5))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e} 💥")
    except Exception as e:
        print(f"Unexpected error: {e} 💥")

if __name__ == "__main__":
    # Input dari user
    target = input("Masukkan URL NGL target: ")
    jumlah = int(input("Masukkan jumlah spam yang mau dikirim: "))
    pesan = input("Masukkan pesan spam: ")

    # Eksekusi spam NGL
    spam_ngl(target, jumlah, pesan)

    print("Selesai! Semoga target lo menderita! 😈")
