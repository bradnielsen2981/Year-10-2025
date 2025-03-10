import databaseinterface
import logging

print("\033c")

# Configure logging
logfile = "database.log"
logging.basicConfig(filename='log.txt') # Log format
logger = logging.getLogger("DatabaseLogger")

# Create the Database
Database = databaseinterface.Database("games.db")

def insert_new_player():
    firstname = input("Enter the player's first name: ")
    lastname = input("Enter the player's last name: ")

    #Red Warriors
    teamname = input("Enter the player's team name: ")
    query = "SELECT teamid FROM teams WHERE teamname = ?"
    results = Database.ViewQuery(query, (teamname,))
    team = results[0] #get the first item from the teams list
    teamid = team['teamid'] #get the team column from the team dictionary

    email = input("Enter the player's email: ")
    query = "INSERT INTO players (firstname, lastname, teamid, email, password) VALUES (?, ?, ?, ?, ?)"
    Database.ModifyQuery(query, (firstname, lastname, teamid, email, "password"))
    return

def get_players():
    query = "SELECT * FROM players"
    results = Database.ViewQuery(query) #LIST of DICTIONARIES
    for person in results:
        print(person['firstname'], person['lastname'], person['teamid'])
    return

# make this query useful
def get_games():
    gamequery = "SELECT team1, team2, gamelocation FROM games"
    gameresults = Database.ViewQuery(gamequery)

    for game in gameresults:

        #get team 1 
        teamquery = "SELECT teamname FROM teams WHERE teamid = ?"
        teamresults = Database.ViewQuery(teamquery, (game['team1'],))
        print(teamresults[0])

        #get team 2 
        teamquery = "SELECT teamname FROM teams WHERE teamid = ?"
        teamresults = Database.ViewQuery(teamquery, (game['team2'],))
        print(teamresults[0])        

        print(game['gamelocation'])
    return

insert_new_player()
get_players()


