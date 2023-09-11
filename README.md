 # “Hot ticket” Flight club (API - Проект)
The Google table shows cities and average flight prices. The programme searches for hot prices for a period of 6 months from tomorrow (round trip).
The user forms a request - enters name, surname, phone number, mail, IATA of the city. Receives sms and email about the found flight, if there are prices lower than average (specified).

## Resources used
- Google sheet, 
- Sheety API, 
- Kiwi Partners Tequilla API,
- Sms API Twilio, 
- SMTP outlook
Modules and libraries: datetime , reqests, os, twilio.reat, smtplib. 

## Project structure
For the convenience of data management 4 classes are created:
1.	**DataManager** - responsible for communicating with Google Sheet data.
2.	**FlightSearch** - responsible for searching and processing flight information.
3.	**FlightData** - responsible for structuring flight data.
4.	**NotificationManager** - responsible for sending sms and emails.

## Programme Process
1. First the programme makes a query and gets data from Google sheet table "prices" **def get_destination_data()**. 
2. The user enters the required data which is sent to the Google sheet table "users" **def new_user()**.
3. Data validation takes place. If the prices table does not contain the IATA of the cities , then the function **def get_destination_code()** is executed, which makes a request to Kiwi Partners Tequilla API and returns the required airport code for each city. At the same time, the **def update_destination_codes()** function is executed and the necessary data in the "prices" table is updated.
4. Using the datetime module, we determine the date of tomorrow and the day in 6 months.
5. For all destinations from the list of given cities we search for possible flights using the function **def check_flight()**.
6. Делаем проверку горячего билета. Если цена найденного рейса ниже указанной средней цены,  то с помощью функций **def send_sms()** и **def send_email()** отправляем на указанный номер и почту пользователя сообщение с горячим предложением.
<img src="https://github.com/Aleshichev/flight_club/blob/main/Flight_2.png" width="600">
<img src="https://github.com/Aleshichev/flight_club/blob/main/Flight_1.png" width="800">
<img src="https://github.com/Aleshichev/flight_club/blob/main/photo_2022-09-03_10-52-56.jpg" width="400">

