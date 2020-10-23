import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns


drivers = pd.read_csv('./dataset/drivers.csv')
constructors = pd.read_csv("./dataset/constructors.csv")
race_results = pd.read_csv('./dataset/results.csv')
races = pd.read_csv('./dataset/races.csv')
circuits = pd.read_csv('./dataset/circuits.csv')
pit_stops = pd.read_csv('./dataset/pitStops.csv')

# stock data
driver_results = pd.merge(drivers, race_results, on='driverId')
driver_race_results = pd.merge(driver_results, races, on='raceId')
driver_race_circuit_results = pd.merge(driver_race_results, circuits, on= 'circuitId')
driver_constructor_race_circuit_results = pd.merge(driver_race_circuit_results, constructors, on="constructorId")

filtered_stock = driver_constructor_race_circuit_results[['raceId', 'driverId', 'driverRef', 'nationality_x', "name", 'positionOrder', 'points', 'grid', 'country', 'alt']].rename(columns={"nationality_x": "nationality", "name": "constructor"})

#calculated data
# pit num
pit_cols = pit_stops[["raceId", "driverId", "stop"]]
pit_num = pit_cols.groupby(["raceId", "driverId"]).count().reset_index()

# pit avg time
pit_time_cols = pit_stops[["raceId", "driverId", "milliseconds"]]
pit_time = pit_time_cols.groupby(["raceId", "driverId"]).mean().reset_index()

pits = pd.merge(pit_num, pit_time, on=["raceId", "driverId"], how="left")

# data to use
data = pd.merge(filtered_stock, pits,  on=["raceId", "driverId"], how="right").drop(columns=["driverId", "raceId"])
data.head()