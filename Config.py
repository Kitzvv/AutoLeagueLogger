print("AutoLeagueLogger Config")
print('\n')
print("To properly work 'AutoLeagueLogger' u need to select your Riot/League Client path")

program_path = input("Enter path to LeagueClient: ")
path = [program_path]

for x in path:
    with open("Config.txt", "w") as file:
        file.write('\n'.join('"' + item + '"' for item in path))
        file.close()
