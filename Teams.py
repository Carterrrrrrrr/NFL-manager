from CollectionsforTeams import *
import csv

# The teams class contains the all teams BTS which is a list of teams obejcts. Team objects contain fundemental info about the team as well as a stack of the games they have played and a queue of the games they are going to play
# The play next games and find tmea menthods call other methods but ajust the return of info passed in a helpful manner

class Team:
    all_teams = BinarySearchTree()
    used_abbr = []

    def __init__(self, team, city, stadium, headCoach, image):
        self.team = team
        self.city = city
        self.stadium = stadium
        self.headCoach = headCoach
        self.image = image
        self.abbr = ""
        x = team.split()
        for word in x:
            self.abbr+=word[0]
        Team.used_abbr.append(self.abbr)
        if self.abbr in Team.used_abbr and Team.used_abbr.count(self.abbr) > 1:
            self.abbr+= "-" + str(Team.used_abbr.count(self.abbr))
        Team.all_teams.insert(self)
        self.playedGames = Stack()
        self.schedule = Queue()

    def play_next_game(self, scoreH, scoreA):
        self.schedule.pop().complete_game(scoreH, scoreA)

    def __repr__(self):
        return f"{self.abbr} - {self.team}" 

    @classmethod
    def find_team(cls, abbr):
        return cls.all_teams.get(abbr).data
    
    # this method creates new Team objects given the data in the csv
    # the method reads the first line as the titles of the colums and the follow lines as 'teams' 
    # for each line in the csv (each team) it takes the team city stadium head coach and image and creates a new team object with that data (which is located by the colum header)
    @classmethod
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            teams = list(reader)
        for team in teams:
            team_name=team.get('Team')
            city = team.get('City')
            stadium = team.get('Stadium')
            headCoach = team.get('Head coach')
            image = team.get('Image')
            Team(team_name,city,stadium,headCoach,image)


class Games:
    all_games = LinkedList()

    def __init__(self, homeTabbr, awayTabbr):
        self.home = Team.find_team(homeTabbr)
        self.away = Team.find_team(awayTabbr)
        self.home.schedule.push(self)
        self.away.schedule.push(self)
        self.homeTeamScore = 0
        self.awayTeamScore = 0
        Games.all_games.append(self)
    
    def __repr__(self):
        return f"{self.away} @ {self.home}: {self.awayTeamScore}-{self.homeTeamScore}"
    

    def complete_game(self, scoreH, scoreA):
        self.homeTeamScore = scoreH
        self.awayTeamScore = scoreA
        out = f"{self.away} @ {self.home}: {self.awayTeamScore}-{self.homeTeamScore}"
        self.home.playedGames.push(self)
        self.away.playedGames.push(self)
        self.home.schedule.pop()
        self.away.schedule.pop()
        Games.all_games.remove(self)
        return out


if __name__ == "__main__":
    pass
    