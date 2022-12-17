from bs4 import BeautifulSoup
import requests

teams = ['1/Arsenal', '2/Aston-Villa', '127/Bournemouth', '130/Brentford', '131/Brighton-and-Hove-Albion', '4/Chelsea', '6/Crystal-Palace', '7/Everton', '34/Fulham', '9/Leeds-United', '26/Leicester-City', '10/Liverpool', '11/Manchester-City', '12/Manchester-United', '23/Newcastle-United', '15/Nottingham-Forest', '20/Southampton', '21/Tottenham-Hotspur', '25/West-Ham-United', '38/Wolverhampton-Wanderers']



url = "https://www.premierleague.com/clubs/127/Bournemouth/squad"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


def createTeamPageLinks(teams):
  links = []
  for team in teams: 
    link = f"https://www.premierleague.com/clubs/{team}/squad"
    links.append(link)
  return links

teamLinks = createTeamPageLinks(teams)


# --------------------------------------------


def getPlayers(doc): 
  project_h4 = doc.find_all('h4', attrs={'class': 'name'})
  playerNames = []
  for i in project_h4: playerNames.append(i.string)
  return playerNames
  
playerNames = getPlayers(doc)


def getPosition(doc): 
  project_position = doc.find_all('span', attrs={'class': 'position'})
  playerPosition = []
  for i in project_position: playerPosition.append(i.string)
  return playerPosition
  
playerPositions = getPosition(doc)


def getNationality(doc): 
  project_nationality = doc.find_all('span', attrs={'class': 'playerCountry'})
  playerNationality = []
  for i in project_nationality: playerNationality.append(i.string)
  return playerNationality
  
playerNationalities = getNationality(doc)


# --------------------------------------------


def getAllPlayerNames(links):
  playersList = []
  i = 0
  while i < 20:
    result = requests.get(links[i]).text
    doc = BeautifulSoup(result, "lxml")
    playersList.append(getPlayers(doc))
    i += 1
  return playersList

allPlayerNames = getAllPlayerNames(teamLinks)

# Names list flattened
def connectAllNames(splitPlayerNameList):
  connected_list = [item for sublist in splitPlayerNameList for item in sublist]
  return connected_list

connectedNames = connectAllNames(allPlayerNames)


def getAllPlayerNationalities(links):
  nationalitiesList = []
  i = 0
  while i < 20:
    result = requests.get(links[i]).text
    doc = BeautifulSoup(result, "lxml")
    nationalitiesList.append(getNationality(doc))
    i += 1
  return nationalitiesList

allPlayerNationalities = getAllPlayerNationalities(teamLinks)


# Nationality list flattened
def connectAllNationalities(splitPlayerNationalityList):
  connected_list = [item for sublist in splitPlayerNationalityList for item in sublist]
  return connected_list

connectedNationalities = connectAllNationalities(allPlayerNationalities)



def getAllPlayerPositions(links):
  positionsList = []
  i = 0
  while i < 20:
    result = requests.get(links[i]).text
    doc = BeautifulSoup(result, "lxml")
    positionsList.append(getPosition(doc))
    i += 1
  return positionsList

allPlayerPositions = getAllPlayerPositions(teamLinks)


# Position list flattened
def connectAllPositions(splitPlayerPositionList):
  connected_list = [item for sublist in splitPlayerPositionList for item in sublist]
  return connected_list

connectedPositions = connectAllPositions(allPlayerPositions)


def createDb(names, nationalities, positions):
  playerDb = []
  i = 0
  # print(len(names))
  # print(len(nationalities))
  # print(len(positions))
  while i < len(names):
    # print(names[i])
    playerDb.append({'playerName': names[i], 'playerNationality': nationalities[i], 'playerPosition': positions[i]})
    i += 1
  return playerDb

allPlayerDb = createDb(connectedNames, connectedNationalities, connectedPositions)
# ----------------------------------------------------


teamName = ['Arsenal', 'Aston-Villa', 'Bournemouth', 'Brentford', 'Brighton-and-Hove-Albion', 'Chelsea', 'Crystal-Palace', 'Everton', 'Fulham', 'Leeds-United', 'Leicester-City', 'Liverpool', 'Manchester-City', 'Manchester-United', 'Newcastle-United', 'Nottingham-Forest', 'Southampton', 'Tottenham-Hotspur', 'West-Ham-United', 'Wolverhampton-Wanderers']


# find the number of positions in each team list so that we can find out which players are missing positions
def findNoOfTeamPositions(links):
  noTeamPositions = []
  i = 0
  while i < 20:
    result = requests.get(links[i]).text
    doc = BeautifulSoup(result, "lxml")
    noTeamPositions.append(len(getPosition(doc)))
    i += 1
  return noTeamPositions

positionTotalByTeam = findNoOfTeamPositions(teamLinks)

def findNoOfTeamPlayerNames(links):
  noTeamPlayerNames = []
  i = 0
  while i < 20:
    result = requests.get(links[i]).text
    doc = BeautifulSoup(result, "lxml")
    noTeamPlayerNames.append(len(getPlayers(doc)))
    i += 1
  return noTeamPlayerNames

nameTotalByTeam = findNoOfTeamPlayerNames(teamLinks)


print(allPlayerDb)





# NEED TO ITERATE THROUGH EACH TEAM ARRAY AND INVOKE  createPlayerDict

