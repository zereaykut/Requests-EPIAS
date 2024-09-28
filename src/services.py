import os
from dotenv import load_dotenv
import requests
from datetime import date, timedelta

class EpiasTransparencyerServices:
    def __init__(self):
        self.main_url = ""

    def tgt(self):
        """
        Get TGT for authentication
        """
        load_dotenv()

        resp = requests.post(
            "https://giris.epias.com.tr/cas/v1/tickets",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
                },
            data={
                "username": os.getenv("USERNAME_"),
                "password": os.getenv("PASSWORD_")
            }
            )
        return resp

    def grt(self):
        pass

    def info_powerplant():
        pass
