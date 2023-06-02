from flask import Flask,render_template

from getToken import startApi
from getToken import getTempValue
from getToken import getLightValue
from getToken import getBPMValue
from getToken import getCfiValue
from getToken import getCsv
from getToken import sendCFI
from getToken import getDeepSleepValue
from getToken import getLightSleepValue
from getToken import getTotalSleepValue
from getToken import getHumidityValue
from getToken import getBodyTempValue

import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('website2.html')

@app.route("/temp")
def temp():
    return str(getTempValue(client_config))

@app.route("/light")
def light():
    return str(getLightValue(client_config))

@app.route("/BPM")
def BPM():
    return str(getBPMValue(client_config))

@app.route("/lightSleep")
def lightSleep():
    return str(getLightSleepValue(client_config))

@app.route("/deepSleep")
def deepSleep():
    return str(getDeepSleepValue(client_config))

@app.route("/totalSleep")
def totalSleep():
    return str(getTotalSleepValue(client_config))

@app.route("/bodyTemp")
def bodyTemp():
    return str(getBodyTempValue(client_config))

@app.route("/humidity")
def humidity():
    return str(getHumidityValue(client_config))

@app.route("/cfi")
def cfi():
    return str(getCfiValue(csv,client_config))


    
if __name__ == "__main__":
    client_config = startApi()
    csv = getCsv()
    app.run(debug=True)