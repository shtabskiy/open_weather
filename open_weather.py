#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Пример доступа по АПИ
http://api.weatherstack.com/current?access_key=ab0ca3c7d6559ab23cd5b80c39be07f0&query=New%20York
'''

import requests
import sys

while True:
    try:
        city = input("Введите город или страну\n")
        url = ('your api link' + city)
        r = requests.get(url)
        data_parse = r.json()

        current_position = data_parse["request"] ["query"]
        print('Current position', current_position)

        temp1 = data_parse["current"] ["temperature"]
        print('Current temperature in' + ' ' + city + ' ' , temp1)

        temp = data_parse["current"] ["feelslike"]
        print('The temperature feels like', temp)

    except KeyboardInterrupt:
        print(" " + "exit script")
        sys.exit()

    except EOFError:
        print(" " + "exit script")
        sys.exit()

    except KeyError:
        print("Не правильно введен город")