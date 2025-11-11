import pandas as pd
import matplotlib.pyplot as plt

def visualize_by_input(filepath):
    # prompt user to input a list of countries to compare
    countries = input("Enter countries separated by commas: ").strip()

    #split input based on comma and strip whitespace on each element
    countries = [c.strip() for c in countries.split(",")]

    df = pd.read_csv(filepath)

    #filter from all countries to those from user input
    df_countries = df[df["Country"].isin(countries)]

    #group by country, calculate avg AQI, sort high -> low
    avg_aqi_by_country = df_countries.groupby("Country")["Average AQI"].mean().sort_values(ascending=False)
    try:
        # fig size for readability
        plt.figure(figsize=(10,6))
        # make bar plot avg AQI / country
        avg_aqi_by_country.plot(kind="bar", color="orange")
        # label titles :3
        plt.title(f"Average AQI of User Selected Countries")
        plt.ylabel("Average AQI Value")
        plt.xlabel("Country")
        # names of countries rotated 45 degrees for better readability
        plt.xticks(rotation=45, ha="right")
        # prevents labels/titles clipping
        plt.tight_layout()
        # show me da monie
        plt.show()
    except IndexError:
        print("Country was not found")

visualize_by_input('Country_AQI_data.csv')