import pandas as pd

data = pd.read_csv("data/sports_gear.csv")

print("Unique sports in the dataset:")
print(data['Sport'].unique())
