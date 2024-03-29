# API that shows all timezones. This is located on htpp://127.0.0.1:5000/all.
# Every time the user refreshes the page, it takes the current time and converts it to the appropriate time zone.

import time
import math
from datetime import datetime

from flask import Flask, render_template, request, jsonify, url_for, redirect
import json
import requests

app = Flask(__name__)

timezone = {-11:{"name": "Midway Island Time", "abbreviation":"MIT", "UTC-time": -11},
            -10:{"name": "Hawaiian Standard Time", "abbreviation":"HST", "UTC-time": -10},
            -9: {"name": "Alaska Standard Time", "abbreviation": "AK", "UTC-time": -9},
            -8: {"name": "Pacific Standard Time", "abbreviation": "PT", "UTC-time": -8},
            -7: {"name": "Mountain Standard Time", "abbreviation": "MT", "UTC-time": -7},
            -6: {"name": "Central Standard Time", "abbreviation": "CT", "UTC-time": -6},
            -5: {"name": "Eastern Standard Time", "abbreviation": "ET", "UTC-time": -5},
            -4: {"name": "Atlantic Standard Time", "abbreviation": "AST", "UTC-time": -4},
             0: {"name": "Universal Coordinated Time", "abbreviation": "UTC", "UTC-time": 0},
            1: {"name": "European European Time", "abbreviation": "ECT", "UTC-time": 1},
            2: {"name": "Eastern European Time", "abbreviation": "EET", "UTC-time": 2},
            3: {"name": "Eastern African Time", "abbreviation": "EAT", "UTC-time": 3},
            4: {"name": "Near East Time", "abbreviation": "NET", "UTC-time": 4},
            5: {"name": "Pakistan Lahore Time", "abbreviation": "PLT", "UTC-time": 5},
            6: {"name": "Bangladesh Standard Time", "abbreviation": "BST", "UTC-time": 6},
            7: {"name": "Vietnam Standard Time", "abbreviation": "VST", "UTC-time": 7},
            8: {"name": "China Tiawan Time", "abbreviation": "CTT", "UTC-time": 8},
            9: {"name": "Japan Standard Time", "abbreviation": "JST", "UTC-time": 9},
            10: {"name": "Australia Eastern Time", "abbreviation": "AET", "UTC-time": 10},
            11: {"name": "Solomon Standard Time", "abbreviation": "SST", "UTC-time": 11},
}
def _find_next_id():
    return min(timezone["UTC-time"] for zone in timezone) + 1

@app.route('/')
def index():
    return "<h1>Welcome to My Website</h1>"

@app.route('/userprofile')
def usersLocalTime():

    currentTime = time.strftime("%H:%M")                    # Obtains the current time in the user's timezone
    usersTimeZone = -1 * (time.altzone / 3600) - 1          # Obtains the number of hours behind Greenwitch time (GMT) - obtains timezone. Technical explanation: obtains difference in time (in seconds) between user's local timezone and GMT. If 0, user is in GMT. If -3600, user is 1 hour behind GMT or 1 timezone away. And vice versa. In all, it calculates which timezone the user is in.
    calculatedTimeZone = timezone[usersTimeZone]["name"]    # Obtains the name of the user's timezone.


    userProfileList = currentTime + ", " + str(usersTimeZone) + ", " + calculatedTimeZone

    return jsonify(userProfileList)



@app.route("/all")
def yomask():

    currentHour = time.strftime("%H")          # Obtains the current time in the user's timezone
    currentMin = time.strftime("%M")           # Obtains the current minute
    currentMonth = time.strftime("%b")         # Obtains the month
    currentDay = time.strftime("%d")           # Obtains the day
    usersTimeZone = -1 * (time.altzone / 3600) - 1
    dz = []
    space = " "
    for el in timezone:
        calc = math.trunc(int(currentHour) + timezone[el]["UTC-time"] - usersTimeZone)
        currentDay = time.strftime("%e")
        if calc >= 24:                         # Accounts for timezones that are on a different day.
            calc -= 24
            ji = int(currentDay) + 1
            currentDay = str(math.trunc(ji))
        calc = str(math.trunc(calc))
        abbr = timezone[el]["abbreviation"]
        utc = timezone[el]["UTC-time"]


        nam = timezone[el]["name"]
        killerQueen = " {:<30} {:<3} (UTC-time:{:>3}): {:>2}:{:<2}, {:>3} {:<2}{:<150}".format(nam, abbr, utc, calc,currentMin,currentMonth, currentDay, space)
        dz.append(killerQueen)
    return jsonify(dz)

@app.route('/timezone')
def addUserLocalTime():
    return jsonify(timezone)

@app.route('/timezone', methods=['POST'])
def addTime():
    timezone.append(request.get_json)
    return '', 204


if __name__ == "main":
    app.run