import pandas as pd
import matplotlib.pyplot as plt

# load datasets
df = pd.read_csv("cleaned_data.csv")

# distribution of overall AQI values
# fig size for readability
plt.figure(figsize=(8,5))
# visualize frequency distribution of AQI values
# bins divides the range of AQI values into 30 intervals
# edgecolor for visual appealing look :D
plt.hist(df["AQI Value"], bins=30, edgecolor="black")
# titles and labels
plt.title("Distribution of AQI Values")
plt.xlabel("AQI Value")
plt.ylabel("Frequency")
# show me da monie
plt.show()
