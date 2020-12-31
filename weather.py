# This is a Weather GUI application using the Tkinter module.
# Designed by Robert Miller in Python 3.8

# API Key = 6d32498b2d5f4df21051dbb4daafb974
# api.openweathermap.org/data/2.5/forecast?q={city name}, {country code}

import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']

    return str(name) + ' ' + str(desc) + ' ' + str(temp)

def test_function(entry):
    print("This is the entry:", entry)

def get_weather(city):
    weather_key = '6d32498b2d5f4df21051dbb4daafb974'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    lable['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='clouds.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

lable = tk.Label(lower_frame)
lable.place(relwidth=1, relheight=1)


root.mainloop()