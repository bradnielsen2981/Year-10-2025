import databaseinterface
import logging

import logging

# Configure logging
logfile = "database.log"
logging.basicConfig(filename='log.py') # Log format
logger = logging.getLogger("DatabaseLogger")

Database = databaseinterface.Database("games.db")

def insert_new_player(firstname, lastname, teamid, phonenumber, password, email):
    query = "INSERT INTO players (firstname, lastname, teamid, phonenumber, password, email) VALUES (?, ?, ?, ?, ?, ?)"
    Database.ModifyQuery(query, (firstname, lastname, teamid, phonenumber, password, email))
    return 

def get_all_players():
    query = "SELECT * FROM players"
    results = Database.ViewQuery(query)
    return results

def get_all_players_by_team(teamid):
    query = "SELECT * FROM players WHERE teamid = ?"
    results = Database.ViewQuery(query, (teamid,))
    return results

print(get_all_players())

list_of_dictionaries = get_all_players_by_team(1)
print(list_of_dictionaries)

for dict in list_of_dictionaries:
    print(dict["firstname"])
    print(dict["lastname"])
    print(dict["teamid"])