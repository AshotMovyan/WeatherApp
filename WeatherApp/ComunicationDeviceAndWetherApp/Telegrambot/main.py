# -*- coding: utf-8 -*-
import telebot
import requests

import sys
import os
import time
import Adafruit_DHT

bot = telebot.TeleBot('1220565627:AAHRCYOX6zOJADrooLjGDmRCDWplN0sga_s')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Բարեվ Գրիր Ցանկացաժ Քաղաքի Անվանում')


@bot.message_handler(content_types=['text'])
def send_text(message):
    message.text.lower()
    apiKey = 'd37274b7fdd683c3c268b47bf9c9f003'
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + message.text + "&type=like&" + "DE&appid=" + apiKey
    response = requests.get(url)
    pogoda_data = response.json()

    if message.text.lower() == "sensor":
        DHT_SENSOR = Adafruit_DHT.DHT22
        DHT_PIN = 4

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")

        bot.send_message(message.chat.id, ("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity)))


    
    else:
        pogoda_json_request = pogoda_data["weather"][0]
        if pogoda_json_request["main"] == "Rain":
            obsheye = "Անձրև\n"
            sti = open('Stickers/rain.png', 'rb')

        elif pogoda_json_request["main"] == "Clouds":
            obsheye = "Ամպամած\n"
            sti = open('Stickers/cloud.png', 'rb')

        elif pogoda_json_request["main"] == "Clear":
            obsheye = "Պարզ երկինք\n"
            sti = open('Stickers/warm.png', 'rb')

        elif pogoda_json_request["main"] == "thunderstorm":
            obsheye = "Ամպրոպ\n"
            sti = open('Stickers/thunderstorm.png', 'rb')

    


        main = pogoda_data["main"]
        temp1 = main["temp"]
        temp2 = 273.15
        temp = round(temp1 - temp2)
        temp_ans = "ջերմաստիճան - " + str(temp) + "°,\n"

        wind = pogoda_data["wind"]
        wind_speed = wind["speed"]
        wind_deg = wind["deg"]
        if wind_deg < 23:
            napr = "Հյուսիսային"
        elif wind_deg < 68:
            napr = "Հյուսիս-արևելյան"
        elif wind_deg < 113:
            napr = "Արևելյան"
        elif wind_deg < 158:
            napr = "Հարավ-Արևելյան"
        elif wind_deg < 203:
            napr = "Հարավային"
        elif wind_deg < 248:
            napr = "Հարավ-Արևմտյան"
        elif wind_deg < 293:
            napr = "Արևմտյան"
        elif wind_deg < 338:
            napr = "Հյուսիս-Արևմտյան"
        else:
            napr = "Հյուսիսային"

        wind_mess = "Քամու Արագություն - " + str(wind_speed) + "Մ/Վ" + ",\nՔամու ՈՒղղություն - " + napr + ",\n"
        humidity = main["humidity"]
        otvet_vlaznost = "Օդի Խոնավություն - " + str(humidity) + "%"
    
        answer = obsheye + temp_ans + wind_mess + otvet_vlaznost
        bot.send_message(message.chat.id, answer)
    
        bot.send_sticker(message.chat.id, sti)

        print(answer)

bot.polling(none_stop=True)
getting_message_time(message)
