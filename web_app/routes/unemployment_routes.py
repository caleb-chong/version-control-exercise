# This is "web_app/routes/unemployment_routes.py"

from flask import Blueprint, request, render_template, redirect, flash
from statistics import mean
from plotly.express import line
from app.unemployment import fetch_unemployment_json

unemployment_routes = Blueprint("unemployment_routes", __name__)

@unemployment_routes.route("/unemployment")

def unemployment():
    print("UNEMPLOYMENT PAGE!")

    request_data = dict(request.args)
    print("URL PARAMS:", request_data)
    
    data = fetch_unemployment_json()

    print("-------------------------")
    print("LATEST UNEMPLOYMENT RATE:")

    print(f"{data[0]['value']}%", "as of", data[0]["date"])

    this_year = [d for d in data if "2022-" in d["date"]]

    rates_this_year = [float(d["value"]) for d in this_year]

    print("-------------------------")
    print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
    print("NO MONTHS:", len(this_year))

    dates = [d["date"] for d in data]
    rates = [float(d["value"]) for d in data]

    latest_date = dates[-1]
    latest_rate = rates[-1]

    # fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
    # fig.show()

    return render_template("unemployment.html", 
        data=data,
        dates=dates,
        rates=rates,
        latest_date=latest_date,
        latest_rate=latest_rate
    )