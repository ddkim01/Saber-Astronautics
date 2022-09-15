#
# Author: David Kim (z5255322@ad.unsw.edu.au).
#
# Date: September 2022.
#
# Task: Saber Astronautics Technical Test 2.
#
# Function: Creating Simple Moving Average (SMA) from data.
#
# Description: This script reads data from a .json file, sorts it into relevant columns.
#              and visualises it in a graphical plot.
#              Uses matplotlib and pandas package (.loc(), .dropna()).
#
# Parameters: .json file containing GOES 16 proton data (from a URL).
#
# Return: visual analysis and representation of a column in the .json file.
#
# Bugs: Note that WSL Linux cannot do graphical functions like plots. Should configure for VM linux next time.
#       Identifying and deleting NaN values.
#       Difficulty with "energy" data due to data type being 'object' (unresolved).
#       Using print() to see df1, df1.info() to help debug.
#       Difficult to judge the 20 min window due to x axis labeling.
#
# Sources: Importing data => https://www.w3schools.com/python/pandas/pandas_json.asp
#          Slicing data => https://www.activestate.com/resources/quick-reads/how-to-slice-a-dataframe-in-pandas/
#          SMA in pandas => https://www.geeksforgeeks.org/how-to-calculate-moving-average-in-a-pandas-dataframe/
#          Plotting => https://realpython.com/pandas-plot-python/
#
# Status: Finished.
#
# =======================================================================================
#

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Imported from the URL so anyone can run this script
df = pd.read_json(
    "https://services.swpc.noaa.gov/json/goes/primary/differential-protons-1-day.json"
)

# Only analysing "flux" only as "energy" is an object type.
df1 = df.loc[(df["channel"] == "P1"), ["time_tag", "flux", "energy"]]

# Set the time column as the index since the plot is comparing against time
# and not against the number of entries/rows
df1.set_index("time_tag", inplace=True)

# Translate index name into English
df1.index.name = "Time"

# Calculating a simple moving average using .rolling(window).mean()
# Every 5 entries is 20  minutes hence window size in .rolling().mean() is 5
# Note that 'df1["SMA20_flux"] =' creates a new column in df1 dataframe.
# Line below can be changed to accommodate any timeframe moving average
df1["SMA20_flux"] = df1["flux"].rolling(5).mean()

# Check and delete the NULL values using dropna() method.
df1.dropna(inplace=True)

# Creates the plot and assigns it to SMA20
# Note the code still works if "SMA20 =" is deleted.
SMA20 = df1[["flux", "SMA20_flux"]].plot(label="df1", figsize=(16, 8))

# Note that titles & labels to be defined AFTER the plot is created.
plt.title("The Simple Moving Average of 20 minutes for Channel P1")
plt.xlabel("Date and Time (UTC)", fontsize=16)
plt.ylabel("Flux", fontsize=16)
plt.grid()

plt.show()
