import pandas as pd

data = pd.read_csv("data/sports_gear.csv")
basketball_gear = data[data['Sport'].str.lower() == "basketball"]
print("Basketball gear found:\n", basketball_gear)
