from Teams import *

Team.instantiate_from_csv("/Users/carterkelly/Desktop/CS Python/LinkedListProject/NFL Teams.csv")

print("\n\n\n*** NFL Management System ***")
Team.all_teams.print_tree()
key = ""

# this program stores information about teams, allows the creation and storing of games (data) and the storing of completed games that can be seen from both relevent teams
# The loop contuines so long as q is not inputed
# The program either enters the games loop the teams loop or returns the list of teams if q was not entered
# INSIDE THE TEAMS LOOP: the teams loop can either show the upcoming games/compleated games/or into about the team
# inside the upcoming games sections the user is asked if they want to end the teams next game if they do not close the section (c) they enter the home and away score calling the end game method (Team.py)
# Games section - (g) The games section return the games in the played games stack
# info section - (i) The info section return the general info about the team (that was completely useless to me)
# INSIDE THE GAMES LOOP: the user is prompted to enter a home and away team to create a new games. this loops until c is entered as the home team
while(key != "q"):
    print("Would you like to mangage Teams (t) or Schedule Games (g)\n(Quit: q, List Teams: l)")
    key = str(input())
    
    if key == "l":
        Team.all_teams.print_tree()

    if key == "t":
        print("\n Enter a team's abbreviation to manage them")
        teamin = str(input())
        try:
            team = Team.find_team(teamin)
        except:
            print("A with that abbreviation could not be found\n")
        else:
            key = "g"
            while key == "g" or key == "u":
                print(f"{team} \n Would you like to see the teams Upcoming games (u) or Completed games (g) or Info (i)\nClose: c")
                key = str(input())
                if key == "u":
                    print(f"\nSchedule: {team.schedule}")
                    print("\nClose: c, End their next game: e")
                    key = str(input())
                    if key == "e":
                        print("\n Enter home team's score")
                        scoreH = str(input())
                        print("\n Enter aways team's score")
                        scoreA = str(input())
                        team.play_next_game(scoreH,scoreA)
                        print(f"Game Played: \n{team.playedGames.top_node}\n")
                if key == "g":
                    print(f"Played Games: {team.playedGames}")
                if key == "i":
                    print(f"The {team.team} from {team.city} play in {team.stadium} and {team.headCoach} is the Head Coach! \n")
            
    while key == "g":
        print("\n Enter the home team's abbreviation: (enter c to close)")
        home = str(input())
        if home == "c":
            break
        print("\n Enter the away team's abbreviation:")
        away = str(input())
        try:
            Games(home, away)
            print(f"\n Game Created: {Games.all_games.tail_node} \n")
        except:
            print("Teams with those abbreviations could not be found")

print("*** NFL Management System *** \n \t Closed \n")