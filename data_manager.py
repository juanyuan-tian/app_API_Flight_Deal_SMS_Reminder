import requests
from pprint import pprint

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "UR OWN ENDPOINT"
        # self.row_id = 2

    def get_sheet_data(self):
        response = requests.get(url=self.sheety_endpoint)
        return response.json()['prices']
        # return response.json()

    def put_iataCode(self, city_info):
        data = {
            'price':
            # 这里面的key用的是取出来的sheet_data数据结构里面的key的形式，不是原来sheety里面的
            {
            # 'City': city_info['city'],
             'iataCode': city_info['iataCode'],
             # 'Lowest Price': city_info['lowestPrice'],
             }
        }
        response = requests.put(url=f"{self.sheety_endpoint}/{city_info['id']}", json=data)
        # print(response.status_code)
        # print(response.text)

