import requests
import qrcode
from geopy.geocoders import Nominatim

# Livraison automatique
def get_lat_lng(quartier, ville):
    geolocator = Nominatim(user_agent="livraison_app")

    location = geolocator.geocode(f"{quartier}, {ville}, Guinea")

    if location:
        return location.latitude, location.longitude

    return None, None

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