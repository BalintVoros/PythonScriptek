# Conversion ratios or formulas for each game (sample data)
conversion_data = {
    '1': {'game': 'CS:GO', 'sensitivity_ratio': 1.0},
    '2': {'game': 'TF2', 'sensitivity_ratio': 0.5},
    '3': {'game': 'League of Legends', 'sensitivity_ratio': 0.75},
    '4': {'game': 'Overwatch', 'sensitivity_ratio': 0.85},
    '5': {'game': 'Valorant', 'sensitivity_ratio': 0.9}
}

# Function to convert sensitivity from Apex Legends to the target game
def convert_to_game(apex_sensitivity, target_game):
    if target_game in conversion_data:
        ratio = conversion_data[target_game]['sensitivity_ratio']
        converted_sensitivity = apex_sensitivity * ratio

        return converted_sensitivity
    else:
        return None  # Unsupported game

# Get Apex Legends sensitivity from user
apex_sensitivity = float(input("Enter your Apex Legends sensitivity: "))

# Display list of games for conversion
print("Select the game you want to convert to:")
for key, data in conversion_data.items():
    print(f"{key}. {data['game']}")

# Get user input for target game
target_game = input("Enter the number corresponding to the game: ")

# Perform conversion
converted_sensitivity = convert_to_game(apex_sensitivity, target_game)
if converted_sensitivity is not None:
    print(f"\nConverted sensitivity for {conversion_data[target_game]['game']}: {converted_sensitivity}")
else:
    print("Unsupported game")
