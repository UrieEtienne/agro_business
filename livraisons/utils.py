import requests
import qrcode

def send_whatsapp(message, phone):

    url = "https://api.callmebot.com/whatsapp.php"

    params = {

        "phone": phone,

        "text": message,

        "apikey": "YOUR_API_KEY"

    }

    requests.get(url, params=params)

def generate_qr(code):

    img = qrcode.make(code)

    img.save(f"qr_{code}.png")