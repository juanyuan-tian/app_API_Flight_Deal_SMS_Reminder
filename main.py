#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from flight_data import FlightDate

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


orgin_city_code = "LON"

# get sheet data # list
sheet_data = data_manager.get_sheet_data()
# print(sheet_data)
# ----------------loop: 取一个city的信息，flight_search里面找iata信息， data_manager存入sheety
for city_info in sheet_data:
    if city_info["iataCode"] == "":
        flight_search.find_iata_code(city_info)
        # print(city_info)
        data_manager.put_iataCode(city_info)

# ----------------loop:填好目标地的iata，然后找机票
tmr = (datetime.today() + timedelta(days=1))
six_month = tmr + timedelta(days=180)
tmr_date = tmr.date().strftime("%d/%m/%Y")
six_month_date = six_month.date().strftime("%d/%m/%Y")

for city_info in sheet_data:
    flight_data = flight_search.find_flight_info(orgin_city_code, city_info["iataCode"], tmr_date, six_month_date)
    if flight_data is None:
        continue
    #     -----------对比价格 city_info["lowestPrice"]和找到的price,🙋‍♂️️这个price从就在loop里一一对应
    if flight_data.price < city_info["lowestPrice"]:
        message = f"low price alart, only €{flight_data.price} from " \
                  f"{flight_data.origin_city}-{flight_data.origin_airport} to " \
                  f"{flight_data.destination_city}-{flight_data.destination_airport}," \
                  f"from: {flight_data.out_date} to: {flight_data.return_date}"
        notification_manager.sent_sms(message)

    #   return all flight_data



# print(sheet_data)


