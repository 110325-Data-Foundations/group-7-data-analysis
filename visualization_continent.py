import pandas as pd
import matplotlib.pyplot as plt


# prompt user to input a continent name
continent = input("Enter continent name (Africa, Asia, Europe, North America, South America, Oceania): ").strip()

# find and build expected file 
file_name = f"{continent.replace(' ', '_')}_AQI.csv"

try:
    # based on given input continent, read from that CSV file 
    df = pd.read_csv(file_name)
    #group by country, calculate avg AQI, sort high -> low
    avg_aqi_by_country = df.groupby("Country")["Average AQI"].mean().sort_values(ascending=False)

    # fig size for readability
    plt.figure(figsize=(10,6))
    # make bar plot avg AQI / country
    avg_aqi_by_country.plot(kind="bar", color="orange")
    # label titles :3
    plt.title(f"Average AQI by Country — {continent}")
    plt.ylabel("Average AQI Value")
    plt.xlabel("Country")
    # names of countries rotated 45 degrees for better readability
    plt.xticks(rotation=45, ha="right")
    # prevents labels/titles clipping
    plt.tight_layout()
    # show me da monie
    plt.show()

# if user input has continent that doesnt exist
except FileNotFoundError:
    print(f"No data found for {continent}")
