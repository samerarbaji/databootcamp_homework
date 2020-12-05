import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base= automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def main():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
)

@app.route("/api/v1.0/precipitation")
def precipitation():
    session= Session(engine)
    results = (session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date))


    prcpdate= []
    for eachrow in results:
        dt_dict = {}
        dt_dict["date"] = eachrow.date
        dt_dict["prcp"] = eachrow.prcp
        prcpdate.append(dt_dict)

    return jsonify(prcpdate)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.name).all()
    return jsonify(results)


@app.route("/api/v1.0/tobs")
def tobs():
    session= Session(engine)
    lastdate= session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    yearago=dt.date(2017, 8, 23) - dt.timedelta(days=366)
    activestations=  (session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all())
    activestation= activestations[0][0]
    results = (session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date >= yearago).filter(Measurement.station == activestation).all())

    tobs_list = []
    for result in results:
        line = {}
        line["Date"] = result[1]
        line["Station"] = result[0]
        line["Temperature"] = int(result[2])
        tobs_list.append(line)

    return jsonify(tobs_list)                


if __name__ == "__main__":
    app.run(debug = True)