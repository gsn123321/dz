from tkinter import *
import requests


root = Tk()

def get_weather():
    city = cityField.get()
    key = "9b9b5f5439450b9ea0b2a8cb86e7e361"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": key, "q": city, "units": "imperial"}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f"{weather['name']}: {weather['main']['temp']}°F"


root["bg"] = "#fafafa" 
root.title('мое приложение')
root.geometry("300x250")

root.resizable(width=False, height=False)

frame_top = Frame(root, bg="red", bd=5)
frame_top.place(relx=0.15, rely=0.15, relheight=0.25, relwidth=0.7)

frame_bottom = Frame(root,bg="red", bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relheight=0.1, relwidth=0.7)

cityField = Entry(frame_top, bg="white", font=30)
cityField.pack()

btn = Button(frame_top, text="Погода", command=get_weather)
btn.pack()

info = Label(frame_bottom, text="Инфо", bg="yellow", font=40)
info.pack()

root.mainloop()

