import requests
from collections import Counter

def retrieve_api_data():
    url = "https://publicapi.battlebit.cloud/Servers/GetServerList"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print("Error occurred while retrieving API data:", str(e))
        return None

# Call the function to retrieve the API data
api_data = retrieve_api_data()

if api_data:
    # Calculate total player count
    total_players = sum(server["MaxPlayers"] for server in api_data)
    print("Total player count:", total_players)
    print()

    # Calculate player count per unique region
    player_count_per_region = {}
    for server in api_data:
        region = server["Region"]
        max_players = server["MaxPlayers"]
        player_count_per_region[region] = player_count_per_region.get(region, 0) + max_players

    print("Player count per region:")
    for region, player_count in player_count_per_region.items():
        print(f"{region}: {player_count}")
    print()

    # Count occurrences of each map
    map_counts = Counter(server["Map"] for server in api_data)

    print("Map occurrences:")
    for map_name, count in map_counts.items():
        print(f"{map_name}: {count}")
    print()

    # Count occurrences of each unique max player count
    max_player_counts = Counter(server["MaxPlayers"] for server in api_data)

    print("Max player count occurrences:")
    for max_players, count in max_player_counts.items():
        print(f"{max_players}: {count}")
