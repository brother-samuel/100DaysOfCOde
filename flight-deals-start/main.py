from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
destinations_data = data_manager.pull_destinations()
print(destinations_data)

flight_search = FlightSearch()
for destination_dict in destinations_data:
    if destination_dict['iataCode'] == '':
        city_name = destination_dict['city']
        code = flight_search.pull_iata_code(city_name)
        data_manager.update_iata_code(code, destination_dict['id'])

for destination_dict in destinations_data:
    flight_search.search_flights(destination_dict['iataCode'], destination_dict['lowestPrice'])
