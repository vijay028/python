from flask import Flask, render_template, request
from datetime import datetime
import googlemaps
import json

time_calc = 0
GOOGLEMAPS_API_KEY = 'AIzaSyBHT1lW0btfOO8txVZ2SzCuDcC3hFZRE6s'

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/distcalc', methods=['POST'])
def distcalc():
    FROM_ADDRESS = request.form['from_place']
    TO_ADDRESS   = request.form['to_place']
    GOOGLE_MAPS_LINK = 'https://www.google.com/maps/dir/Millennium+Park,+Chicago,+IL/Willis+Tower+Skydeck,+South+Wacker+Drive,+Chicago,+IL/@41.8831931,-87.6326005,16z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x880e2ca70b00f081:0xcbf62372ee30a12b!2m2!1d-87.6193938!2d41.8827024!1m5!1m1!1s0x880e2cbf1d3c61a7:0xcee917a8ddbc62f1!2m2!1d-87.635915!2d41.8788761'

    gmaps = googlemaps.Client(key=GOOGLEMAPS_API_KEY)

    now_time = datetime.now()
    directions_result = gmaps.directions(FROM_ADDRESS,TO_ADDRESS,
                                        mode="driving",
                                        departure_time=now_time)

    time_calc = directions_result[0]['legs'][0]['duration_in_traffic']['text']
#    return time_calc
    return render_template("home.html", variable=time_calc)

@app.route('/about/')
def about():
    return "This is About page!!!"

@app.route('/contactus/')
def contactus():
    return " -- Contact Us page here -- Testing vijay"

if __name__ == "__main__":
    app.run(debug=True)
