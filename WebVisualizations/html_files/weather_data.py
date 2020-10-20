import pandas as pd
# Read the csv file in
df = pd.read_csv("Resources/cities.csv")
df.set_index("City_ID", inplace = True)
# Save to file
df.to_html("weather_data2.html")