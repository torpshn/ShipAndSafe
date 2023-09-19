from App.Ship import Ship
import requests
from datetime import datetime


class Weather(Ship):

    def get_json(self, lat, lon):
        header = {'Content-Type': 'application/json'}
        url = 'https://api.windy.com/api/point-forecast/v2'
        # api_key = '83bsuhSWrEHgTcnywYmnvcAyYum8SbJu'
        # api_key = 'mJQTARUXB3UIGSI62N6nFobxnho4BGNN'
        # api_key = 'RTlJInX6C26qkXHiPN07X5ax0ha7KPXe'
        api_key = 'NOpe1T5bbORVgVnxpuwdPBnGf9dt5mAj'
        # api_key = 'BAROVzCSvcXdtaPY7kPcpAg9YXQn6nR8'
        # api_key = 'xLRbEICgGqISfZ3xiBVDQobjwc2fr26H'
        data = {
            "lat": lat,
            "lon": lon,
            "model": "gfs",
            "parameters": ["wind", "windGust", "waves"],
            "levels": ["surface", "surface", "surface"],
            "key": api_key
        }

        json = requests.post(url=url, json=data, headers=header).json()
        for i in range(len(json['ts'])):
            # Надо доработать
            json['ts'][i] = datetime.utcfromtimestamp(int(str(json['ts'][i])[0:-3])).strftime('%Y-%m-%d %H:%M:%S')

            # json['ts'][i] = pd.to_datetime(ts, unit='ms').strftime("%m/%d/%Y")

        return json

    def data_picker(self):
        # UNBLOCK
        path = self.expected_path()
        data = []
        res = []
        for i in range(len(path)):
            data.append(self.get_json(path[i][0], path[i][1]))

        for j in range(len(data)):
            dictionary = {data[j]['ts'][j]: {'wind_u': round(data[j]['wind_u-surface'][j], 2),
                                             'wind_v': round(data[j]['wind_v-surface'][j], 2),
                                             'gust': round(data[j]['gust-surface'][j], 2),
                                             'waves_period': str(data[j]['waves_period-surface'][j]),
                                             'waves_height': str(data[j]['waves_height-surface'][j])}}
            res.append(dictionary)

        # res = [{'2023-02-22 15:00:00': {'wind_u': 4.42, 'wind_v': 7.68, 'gust': 7.3, 'waves_period': 'None', 'waves_height': 'None'}}, {'2023-02-22 18:00:00': {'wind_u': -1.66, 'wind_v': 2.41, 'gust': 8.64, 'waves_period': 'None', 'waves_height': 'None'}}, {'2023-02-22 21:00:00': {'wind_u': -2.67, 'wind_v': 8.24, 'gust': 4.25, 'waves_period': 'None', 'waves_height': 'None'}}, {'2023-02-23 00:00:00': {'wind_u': -7.21, 'wind_v': 1.98, 'gust': 7.71, 'waves_period': 'None', 'waves_height': 'None'}}, {'2023-02-23 03:00:00': {'wind_u': -5.66, 'wind_v': 3.19, 'gust': 6.41, 'waves_period': 'None', 'waves_height': 'None'}}, {'2023-02-23 06:00:00': {'wind_u': -4.44, 'wind_v': 0.86, 'gust': 7.7, 'waves_period': 'None', 
# 'waves_height': 'None'}}]
        return res
