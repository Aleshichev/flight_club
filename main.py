from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


print("Welcome to Aleshichev Igor's Flight Club\nWe find the best flight price and email you")
first_name = input("What is your first name?:\n")
last_name = input("What is your last name?:\n")
email = input("What is your email?:\n")
mobile_phone = input("Type your mobile phone (e.x +380...):\n")
city_code = input("Enter the origin city IATA where you want to fly (e.x LON, PRG):\n").upper()
print("Ok. Wait a second")

data_manager.new_user(first_name, last_name, email, mobile_phone, city_code )


if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])



    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.chek_flights(
        city_code,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    try:
        if flight.price < destination["lowestPrice"]:

            notification_manager.send_sms(
                mobile_phone,
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                        f"to {flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."
            )

            notification_manager.send_emails(
                email,
                message=f"Low price alert! Only £{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} "
                        f"to {flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."
            )
    except AttributeError:
        pass
