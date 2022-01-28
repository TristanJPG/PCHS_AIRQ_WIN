
from datetime import datetime
import requests
class Sender:
    def __init__(self, names, values):
        self.name = names
        self.value = values
        self.sheetyAPI = "https://api.sheety.co/ec2268bc28d37608590b3b795cf24e1e/airQuality/sheet1"
        self.today_date = datetime.now().strftime("%d/%m/%Y")
        self.now_time = datetime.now().strftime("%X")
        self.basicHeader = {
            "Authorization": "Basic bHVmZnk6Y29jb2E="
        }
        self.sheet()
    def sheet(self):
            self.sheet = {
                "sheet1": {
                    "date": self.today_date,
                    "time": self.now_time,
                    self.name[2].lower(): f"{self.value[2]}" + " µg/m³",
                    self.name[1].lower(): f"{self.value[1]}" + " µg/m³",
                    self.name[0].lower(): f"{self.value[0]}" + " µg/m³",
                    self.name[3].lower(): f"{self.value[3]}" + " hPa",
                    self.name[4].lower(): f"{self.value[4]}" + "%",
                    self.name[5].lower(): f"{self.value[5]}" + " °C"

                }
            }
            self.g = requests.post(url=self.sheetyAPI, json=self.sheet, headers=self.basicHeader)
            print(self.g.text)

