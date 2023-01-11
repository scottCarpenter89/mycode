#!/usr/bin/python3

import requests
import datetime
import reverse_geocoder as rg

def main():

    iss = requests.get('http://api.open-notify.org/iss-now.json')
    coordinates = iss.json()
    print(coordinates)

    longitude = coordinates['iss_position']['longitude']
    latitude = coordinates['iss_position']['latitude']
    current_time = coordinates['timestamp']
    time_stamp = datetime.datetime.fromtimestamp(current_time)
    
    loc = rg.search((latitude, longitude))

    city = loc[0]['name']
    country = loc[0]['cc']


    print(f'''CURRENT LOCATION OF THE ISS:
              Timestamp: {time_stamp}          
              Lon: {longitude}              
              Lat: {latitude}
              City/Country: {city}, {country}''')

if __name__ == "__main__":
    main()
