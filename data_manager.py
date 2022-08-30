import requests
import os

USERNAME = os.environ.get('myusername')
USER_PASSWORD = os.environ.get('mypassword')
SHEET_ENDPOINT = os.environ.get('sheet_endpoint')
SHEET_USERS_ENDPOINT = os.environ.get('OWM_SHEET_USERS_ENDPOINT')


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """Get and return destination data"""
        response = requests.get(url=SHEET_ENDPOINT, auth=(
        USERNAME,
        USER_PASSWORD,
    ))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """update destination codes"""
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    auth=(
        USERNAME,
        USER_PASSWORD,
    ))

            print(f"Successful operation code is {response.text}")


    def new_user(self,first_name, last_name, email, mobile_phone, city_code):
        """This function creates new user and write a name, email """
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phone": mobile_phone,
                "cityIata": city_code,
            }
        }

        requests.post(
            url=SHEET_USERS_ENDPOINT,
            json=new_data,
            auth=(
                USERNAME,
                USER_PASSWORD,
            ))
