from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

# fetch the url of the API
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'
weather = get(url).json()
#print(weather['items'][0])

#use for loop to iterate over the temperatures and add to a list
temperatures = []
timestamps = []
for record in weather['items']:
    temperature = record['ambient_temp']
    temperatures.append(temperature)
    time = parser.parse(record['reading_timestamp']) # to get the date into datetime format
    timestamps.append(time)

# create a plot of timestamps against temperature and show it
plt.plot(timestamps, temperatures)
#Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()

