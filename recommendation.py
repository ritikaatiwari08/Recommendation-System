import pandas as pd

# Load the dataset
data = pd.read_csv("data/sports_gear.csv")

def recommend_gear(sport_name):
    # Convert input to lowercase for case-insensitive match
    sport_name = sport_name.strip().lower()

    # Filter dataset
    matching_gears = data[data['Sport'].str.lower() == sport_name]

    if matching_gears.empty:
        return [f"Sorry, no gear currently available for '{sport_name.title()}'. Please try a different sport."]
    
    return matching_gears['Name'].tolist()
