import pandas as pd

#Load Dataset
df = pd.read_csv("cleaned_data.csv")

#Basic analysis
#Summary Stats
print(df.describe().round(2))

#Correlation Between Two Columns
correlation = df["AQI Value"].corr(df["PM2.5 AQI Value"])
print(f"Correlation Between AQI Value and PM2.5 AQI Value: {correlation:.2f}")
correlation = df["AQI Value"].corr(df["CO AQI Value"])
print(f"Correlation Between AQI Value and CO AQI Value: {correlation:.2f}")
correlation = df["AQI Value"].corr(df["Ozone AQI Value"])
print(f"Correlation Between AQI Value and Ozone AQI Value: {correlation:.2f}")
correlation = df["AQI Value"].corr(df["NO2 AQI Value"])
print(f"Correlation Between AQI Value and NO2 AQI Value: {correlation:.2f}")

