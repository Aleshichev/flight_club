import requests


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
APIKEY = "RWU1xvcNJn7VkGgQxIju7FHjwjwXF7eX"
class FlightSearch:

    def get_destination_code(self, city_name):
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


