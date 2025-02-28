import databaseinterface

Database = databaseinterface.Database("games.db")

def get_all_players():
    query = "SELECT * FROM players"
    results = Database.ViewQuery(query)
    return results

def get_all_players_by_team(teamid):
    query = "SELECT * FROM players WHERE teamid = ?"
    results = Database.ViewQuery(query, (teamid,))
    return results

list_of_dictionaries = get_all_players_by_team(1)
print(list_of_dictionaries)

for dict in list_of_dictionaries:
    print(dict["firstname"])
    print(dict["lastname"])
    print(dict["teamid"])