import datetime
import matplotlib.pyplot as plt
from noaa_sdk import NOAA

# Create a NOAA object
noaa = NOAA()

# Specify the station and date
station_id = '8594900'  # Washington DC station ID
start_date = datetime.datetime(2023, 8, 1)
end_date = datetime.datetime(2023, 8, 10)

# Get tides data
tides_data = noaa.get_data(station_id, start_date, end_date, product='tides')

# Get current water level data
currents_data = noaa.get_data(station_id, start_date, end_date, product='currents')

# Extract water level and time data
water_levels = [data['v'] for data in tides_data['data']]
timestamps = [data['t'] for data in tides_data['data']]

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, water_levels, marker='o', linestyle='-', color='b')
plt.xlabel('Time')
plt.ylabel('Water Level (feet)')
plt.title('NOAA Tides and Current Water Level in Washington DC')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
