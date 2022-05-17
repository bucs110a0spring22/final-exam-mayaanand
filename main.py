from class1 import SoccerLeagueAPI
from class2 import News

def main():
  '''
  **** Supported Leagues ****
  arg.1 Argentine Liga Profesional de Fútbol
  aus.1 Australian A-League
  bra.1 Brazilian Serie A
  chn.1 Chinese Super League
  ned.1 Dutch Eredivisie
  eng.1 English Premier League
  '''
  
  N = News()
  N.getHeadlines("Liverpool")
  
  ChineseSuperLeague = SoccerLeagueAPI("chn.1")
  
  ChineseSuperLeague.getStandings()
  ChineseSuperLeague.compareBy('pointsAgainst')

  PremierLeague = SoccerLeagueAPI("eng.1")
  
  PremierLeague.getStandings()
  PremierLeague.compareBy('pointsAgainst')

main()
	
  