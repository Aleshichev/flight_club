import requests
import os
from flight_data import FlightData


TEQUILA_ENDPOINT = os.environ.get('Owm_TEQUILA_ENDPOINT')
APIKEY = os.environ.get('Owm_APIKEY')


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def get_destination_code(self, city_name):
        """Get the destination code and return it"""
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": APIKEY}
        params = {
                  "term": city_name,
                  "location_types": "city"
        }

        response = requests.get(url=location_endpoint,
                                params=params,
                                headers=headers)
        results = response.json()['locations']
        code = results[0]['code']
        return code


    def chek_flights(self, origin_city_code, destination_city_code,
                     from_time, to_time):
        """Function checks

         the existence of the flight and returns the city and the price

         """
        headers = {"apikey":APIKEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=headers,
                                params=query,)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"Noflifhts found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
