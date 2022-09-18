import os

from flask import render_template
from flask import Flask
from bs4 import BeautifulSoup
import requests
import datetime
import json


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Instance folder check
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass




    def c_to_f(t_c):
        # Convert given temperature in deg C to deg F
        # Source: https://www.weather.gov/media/epz/wxcalc/tempConvert.pdf
        return (9/5)*t_c + 32

    def f_to_c(t_f):
        # Convert given temperature in deg F to deg C
        # Source: https://www.weather.gov/media/epz/wxcalc/tempConvert.pdf
        return (5/9)*(t_f - 32)

    def ms_to_mph(w_ms):
        # Convert given wind speed in m/s to mph
        # Source: https://www.weather.gov/media/epz/wxcalc/windConversion.pdf
        return 2.23694 * w_ms

    def mph_to_ms(w_mph):
        # Convert given wind speed in mph to m/s
        # Source: https://www.weather.gov/media/epz/wxcalc/windConversion.pdf
        return 0.44704 * w_mph

    def calc_wind_chill(t_c, w_ms):
        # t_c - temp in C
        # w_ms - wind speed in m/s
        # Source: https://www.weather.gov/media/epz/wxcalc/windChill.pdf
        t_c = float(t_c)
        w_ms = float(w_ms)
        # Convert to F and MPH
        t_f = c_to_f(t_c)
        w_mph = ms_to_mph(w_ms)
        wchill_f = 35.74 + (0.6215 * t_f) - (35.75 * (w_mph**0.16)) + (0.4275 * t_f * (w_mph**0.16))
        return f_to_c(wchill_f)


    def calc_dew_point(temp, hum, rnd1=True):
        # Reference:
        # M. Wanielista, R. Kersten and R. Eaglin. 1997. Hydrology Water Quantity and Quality Control. John Wiley & Sons. 2nd ed.
        temp = float(temp)
        hum = float(hum)
        dp = (hum/100) ** (1/8) * (112+0.9*temp) + 0.1*temp - 112
        if rnd1:
            return round(dp, 1)

        return dp


    def parse_meteo():
        # res = requests.get('https://meteo.physic.ut.ee/et/freshwin.php', )
        # soup = BeautifulSoup(res.content, 'html.parser')

        # table = soup.find_all('table')[1]
        data = {}
        # data['temp'] = table.find('a', text='Temperatuur').next_element.next_element.text.split(' ')[0]
        # data['humidity'] = table.find('a', text='Niiskus').next_element.next_element.text.split(' ')[0]
        # data['pressure'] = table.find('a', text='Õhurõhk').next_element.next_element.text.split()[0][:-2]
        # data['wind'] = table.find('a', text='Tuul').next_element.next_element.text[:-4].strip()
        # data['precip'] = table.find('a', text='Sademed').next_element.next_element.text.split(' ')[0]
        # data['irrflux'] = soup.find('a', text='Kiirgusvoog').next_element.next_element.text.split(' ')[0]

        # td = soup.find('small', text='Mõõdetud:').next_element.next_element.text.split()
        # data['timestamp'] = f'{td[0]}. {td[1]} {td[3]}'

        data['temp'] = '--'
        data['humidity'] = '--'
        data['pressure'] = '--'
        data['wind'] = '--'
        data['precip'] = '--'
        data['irrflux'] = '--'
        data['timestamp'] = '--'


        return data

    def greeting(hour):
        h = int(hour)
        if 6 <= h < 9: return 'Good morning!'
        if 9 <= h < 17: return 'Good day!'
        if 17 <= h < 23: return 'Good evening!'
        return 'Good night!'


    @app.context_processor
    def inject_load():
        data = {}
        meteo = parse_meteo()
        now = datetime.datetime.now()

        data['greeting'] = greeting(now.hour)
        data['sunrise'] = '08:07'
        data['sunset'] = '15:49'
        data['next-moon'] = '19. Nov (Full)'

        data['date'] = f'{now.strftime("%A")}, {now.strftime("%d")}. {now.strftime("%B")}'
        data['time'] = f'{now.strftime("%H")}:{now.strftime("%M")}:{now.strftime("%S")}'
        data['timezone'] = f'EEST (GMT+2)'

        data['cc'] = {
            'timestamp': meteo['timestamp'],
            'temp': f'{meteo["temp"]}°C',
            'humidity': f'{meteo["humidity"]}%',
            'pressure': f'{meteo["pressure"]} hPa',
            'wind': f'{meteo["wind"]} m/s',
            'precip': f'{meteo["precip"]} mm',
            'irrflux': f'{meteo["irrflux"]} W/m2'
        }
        
        # data['calc-dewpoint'] = f'{calc_dew_point(meteo["temp"], meteo["humidity"])}°C'
        # wc = round(float(calc_wind_chill(meteo["temp"], meteo["wind"].split()[1])),1)
        # data['calc-windchill'] = f'{wc}°C'
        data['calc-dewpoint'] = '--'
        data['calc-windchill'] = '--°C'
        data['calc-heatindex'] = '--°C'
        
        data['cc2'] = {
            'timestamp': 'Tue 16. Nov 23:15',
            'phenomenon': '--',
            'temp': '--°C',
            'dewpoint': '--°C',
            'humidity': '--%',
            'pressure': '-- hPa',
            'gusts': '-- m/s',
            'precip': '-- mm',
            'visibility': '-- km'
        }

        return {'data': data}


    @app.route('/')
    def index():
        return render_template('base.html')

    return app
