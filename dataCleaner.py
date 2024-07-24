import numpy as np
import pandas as pd

# Read in the data
data = pd.read_csv("SPY/SPY_4-21-2024_to_7-21-2024.csv")

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data by date
data = data.sort_values('Date')

# Calculate daily returns
data['Daily_Return'] = data['Close'].pct_change()

# Drop any rows with missing values
data = data.dropna()

# Reset the index
data = data.reset_index(drop=True)

# Create a feature for the number of days since the start of the dataset
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

# Select features for the model
features = ['Days', 'Open', 'High', 'Low', 'Volume']
target = 'Close'

X = data[features]
y = data[target]