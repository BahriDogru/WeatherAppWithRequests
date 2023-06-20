from tkinter import *
import requests
import datetime

#we create the interface program here
window = Tk()
window.title("My City Weather")
window.geometry("500x700")
window.config(bg="orange", padx=20, pady=20)

# then we create variables to use
bg_color = "orange"
font_ = ('Source Serif Pro', 10, 'bold')
font_button = ('Source Serif Pro', 10, 'normal')
error_massage = "Lütfen geçerli bir şehir ismi giriniz."

# Logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="icon.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()

# tittle and entry
title_name_label = Label(text="Enter City Name", bg=bg_color, padx=10, pady=10, font=font_)
title_name_label.pack()
city_name_entry = Entry(width=40)
city_name_entry.pack()

# program
def show_wheater_info():
    city = str(city_name_entry.get())
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "YOUR API KEY !!!!!!"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&lang=tr"
    try:
        response = requests.get(URL).json()
        description = response["weather"][0]["description"]
        temp_celsius = round((response["main"]["temp"] - 273.15), 2)
        temp_feels_like_celsius = round((response["main"]["feels_like"] - 273.15), 2)
        humidity = response["main"]["humidity"]
        sunrise_time = datetime.datetime.fromtimestamp(response["sys"]["sunrise"]).time()
        sunset_time = datetime.datetime.fromtimestamp(response["sys"]["sunset"]).time()
        wind_speed = response["wind"]["speed"]

        city_name_label["text"] = city.upper() + " için hava durumu"
        description_label["text"] = "Hava Durumu:  " + description
        temp_label["text"] = "Sıcaklık:  " + str(temp_celsius) + " C"
        temp_feel_label["text"] = "Hissedilen sıcaklık:  " + str(temp_feels_like_celsius) + " C"
        humidity_label["text"] = "Nem:  " + "%" + str(humidity)
        wind_label["text"] = "Rüzgar:  " + str(wind_speed) + " m/s"
        sunrise_label["text"] = "Gün doğumu:  " + str(sunrise_time)
        sunset_label["text"] = "Gün batımı:  " + str(sunset_time)

    except Exception:
        city_name_label["text"] = error_massage.upper()
        city_name_label["font"] = font_
        city_name_label["bg"] = "red"

# labels
show_button = Button(window, text="Show Weather", font=('Source Serif Pro', 10, 'normal'), width=13, pady=5, command=show_wheater_info)
city_name_label = Label(text="Hava durumu", font=font_, bg=bg_color, padx=10, pady=10)
description_label = Label(bg=bg_color, text=" ", font=font_)
temp_label = Label(bg=bg_color, text=" ", font=font_)
temp_feel_label = Label(bg=bg_color, text=" ", font=font_)
humidity_label = Label(bg=bg_color, text=" ", font=font_)
wind_label = Label(bg=bg_color, text=" ", font=font_)
sunrise_label = Label(bg=bg_color, text=" ", font=font_)
sunset_label = Label(bg=bg_color, text=" ", font=font_)

show_button.pack(pady=10)
city_name_label.pack(pady=5)
description_label.pack(pady=5)
temp_label.pack(pady=5)
temp_feel_label.pack(pady=5)
humidity_label.pack(pady=5)
wind_label.pack(pady=5)
sunrise_label.pack(pady=5)
sunset_label.pack(pady=5)
mainloop()