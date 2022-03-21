import json
import urllib3
import pandas

flight_id = '2b367bc1' # MU5735

http = urllib3.PoolManager()
data = json.loads(http.request('GET', f'https://api.flightradar24.com/common/v1/flight-playback.json?flightId={flight_id}').data)

extracted_data = []
for point in data['result']['response']['data']['flight']['track']:
    timestamp = point['timestamp']
    lat, lng = point['latitude'], point['longitude']
    altitude = point['altitude']['feet']

    speed = point['speed']['kts']
    vs = point['verticalSpeed']['fpm']
    heading = point['heading']
    squawk = point['squawk']
    extracted_data.append((timestamp, lat, lng, altitude, speed, vs, heading, squawk))

df = pandas.DataFrame(extracted_data, columns=['timestamp', 'lat', 'lng', 'altitude', 'speed', 'vs', 'heading', 'squawk'])
df.to_csv('coarse.csv', index=False)