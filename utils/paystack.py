from datetime import datetime
import requests
from decouple import config

class Paystack:
    @staticmethod
    def initialise_payment(data):
        url = "https://api.paystack.co/transaction/initialize"
        ref = f"test-{str(datetime.now())}".replace(":", "").replace(" ", "")
        print(ref)
        payload = {
            "email": data["email"],
            "amount": data["amount"] * 100, 
            "ref": ref
        }
        header = {
            "Authorization": f"Bearer {config('PAYSTACK_SECRET_KEY')}"
        }
        response = requests.post(url, headers = header, data=payload)
        resp_data = response.json()
        payment_url = resp_data["data"]["authorization_url"]
        print(payment_url)