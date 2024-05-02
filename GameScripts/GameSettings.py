#GameSettingLister
# Description: This script is used to list all the game settings in the game.
# Author: Balint


# List of game settings for each game
settings_data = {
    '1': {'game': 'CS:GO', 'fov': 90, 'sensitivity': 2.0, 'resolution': '1920x1080'},
    '2': {'game': 'TF2', 'fov': 90, 'sensitivity': 1.0, 'resolution': '1920x1080'},
    '3': {'game': 'League of Legends', 'fov': 90, 'sensitivity': 1.5, 'resolution': '1920x1080'},
    '4': {'game': 'Overwatch', 'fov': 103, 'sensitivity': 1.75, 'resolution': '1920x1080'},
    '5': {'game': 'Valorant', 'fov': 103, 'sensitivity': 1.5, 'resolution': '1920x1080'}
}

# Print available games
print("Select the game for the settings you want to list:")
for key, data in settings_data.items():
    print(f"{key}. {data['game']}")

# Take user input for the game number
selected_game = input("Enter the number of the game you want to see settings for: ")

# Check if the selected game number exists
if selected_game in settings_data:
    # Print the settings for the selected game
    print(f"Settings for {settings_data[selected_game]['game']}:")
    for setting, value in settings_data[selected_game].items():
        if setting != 'game':
            print(f"{setting}: {value}")
else:
    print("Invalid game number. Please select a valid number from the list.")
