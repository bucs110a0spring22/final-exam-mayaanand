import requests
from datetime import date
from class2 import News

class SoccerLeagueAPI:
  api_url = "https://api-football-standings.azharimm.site/leagues"

  # Gets league data given a certain league
  def __init__(self, league):

    self.today = date.today()  # Current date
    self.news = News()  # News API (class2.py)

    # Fetch the list of possible leagues and search for the one the user inputted
    r = requests.request("GET", self.api_url).json()
    for l in r['data']:  # iterate over each league in api
      if l['id'] == league or l['name'] == league:  # find the league
        print("Loaded {}...".format(l['name']))
        self.league = l
        return None

  def __str__(self):
    return self.getLeagueTitle() + " Tracker"

  # Returns league data
  def get(self):
    # modify api url to get standings
    api_url = self.api_url+"/{}/standings?season=2021&sort=asc".format(self.league['id'])
    r = requests.request("GET", api_url).json()

    # simplifies the data for the standings maps team name to statistics
    result = {}
    for team in r['data']['standings']:
      teamName = team['team']['name']
      stats = team['stats']
      data = {}
      for stat in stats:
        if 'value' in stat.keys():
          data[stat['name']] = stat['value']
      result[teamName] = data
    return result

  # Return the league title
  def getLeagueTitle(self):
    return self.league['name']

  # Prints table of teams sorted by the given stat
  def compareBy(self, stat):
    standings = self.get()
    print("************************")
    print("Comparing Team By: {} (Descending)".format(stat))
    print("************************")

    # Get the values for the stat field
    field = {}
    for team,stats in standings.items():
      if stat in stats:
        field[team] = stats[stat]

    # Sort the dictionary by stat field (found online)
    data = dict(reversed(sorted(field.items(), key=lambda item: item[1])))
    for team, val in data.items():
      print("{} - {}".format(team,val))
      
    
  # Return a list of teams
  def getTeams(self):
    return list(self.get().keys())

  # Return a the standings of the league
  def getStandings(self):
    print("************************")
    print("Today's {} Standings ({})".format(self.getLeagueTitle(), self.today.strftime("%B %d, %Y")))
    print("************************")
    
    standings = self.get()
    for team,stats in standings.items():
      print("{} - {} ({} points)".format(stats['rank'], team, stats['points']))

  def getNews(self, team):
    if team in self.getTeams():
      self.news.getHeadlines(team, 5)
    else:
      print("Please input a valid Premier League team!")