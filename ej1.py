import pandas as pd

df = pd.read_csv('air_traffic_data.csv', delimiter = ',')
print(df.info())
