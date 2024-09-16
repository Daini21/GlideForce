import requests

TOKEN = "6751171075:AAFAtsMDqbiGuqd2RGFBBkrG9VPMoYY70c8"  # Замените на токен вашего бота
WEBHOOK_URL = "https://aef6308e4c69b26f159994e204e7db6d.serveo.net"  # Замените на URL от Serveo

response = requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", data={"url": WEBHOOK_URL})
print(response.json())

