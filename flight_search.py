import requests
from flight_data import FlightDate

header = {"apikey": "FROM YOUR OWN ACCOUNT", "accept": "application/json"}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # self.iatacode = "TESTING"
        pass

    # ------------------------------------------------------
    def find_iata_code(self, city_info):
        loction_endpoint = "https://api.tequila.kiwi.com/locations/query"
        # 找到城市对应的IATA code，赋值到数据中，city_info["iataCode"]
        params = {
            "term": city_info["city"],
            "location_types": "city"
        }
        response = requests.get(url=loction_endpoint, headers=header, params=params)
        city_info["iataCode"] = response.json()["locations"][0]["code"]

    # ------------------------------------------------------
    def find_flight_info(self, orgin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        params = {
            "fly_from": orgin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "ret_from_diff_city": "false",
            "ret_to_diff_city": "false",
            "adults": "1",
            "children": "0",
            "selected_cabins": "M",
            "only_working_days": "false",
            "only_weekends": "false",
            "max_stopovers": "1",
            "max_sector_stopovers": "0",
            "vehicle_type": "aircraft",
            "limit": "1",
            "flight_type": "round",
            "curr": "EUR"
        }

        try:
            response = requests.get(url=search_endpoint, headers=header, params=params)
            response.raise_for_status()

            price = response.json()["data"][0]["fare"]["adults"]
            origin_city = response.json()["data"][0]["cityFrom"]
            origin_airport = response.json()["data"][0]["flyFrom"]

            destination_city = response.json()["data"][0]["cityTo"]
            destination_airport = response.json()["data"][0]["flyTo"]
            out_date = response.json()["data"][0]["route"][0]["local_departure"]
            return_date = response.json()["data"][0]["route"][1]["local_arrival"]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            #        👉 航班找到了,保存数据
            flight_data = FlightDate(
                price=price,
                origin_city=origin_city,
                origin_airport=origin_airport,
                destination_city=destination_city,
                destination_airport=destination_airport,
                out_date=out_date,
                return_date=return_date)
            print(f"{flight_data.destination_city}: €{flight_data.price}")
            return flight_data
