from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

df = players.find_players_by_first_name("stephen")

print(df)

player_info = commonplayerinfo.CommonPlayerInfo(player_id=201939)
test = player_info.get_data_frames()
print(test)
