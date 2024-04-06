import requests 
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from Hackbook import Hackbook
import json
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
def DayFinder(s):
    if (s != "Spread" and s != "Total" and s!= "Moneyline"):
        return s

HomeTeams = []
VisitorTeams = []
Dates = []
MoneyLines = []

htmldata = getdata("https://www.mybookie.ag/sportsbook/nba/") 
soup = BeautifulSoup(htmldata, 'html.parser')

for date in soup.find_all("p", class_="game-line__time__date"):
    date = date.text.strip()
    date = date.replace(" ", "")
    date = date.replace("\n", "")
    Dates.append(date)

for team in soup.find_all("p", class_="game-line__home-team__name m-0"):
    team = team.find('a').decode_contents()
    HomeTeams.append(team)

for team in soup.find_all("p", class_="game-line__visitor-team__name m-0"):
    team = team.find('a').decode_contents()
    VisitorTeams.append(team)

for ml in soup.find_all("button", attrs={'data-markettype': "ml", 'data-wager-type':'ml'}):
    ml = ml.text.replace(" ", "").replace("\n", "")
    MoneyLines.append(ml)

Gambling_Days = []
Times = []

for d in Dates:
    Gambling_Days.append(d[0:5])
    Times.append(d[6:])


Matches = []
for x in range(0, len(HomeTeams)):
    Matches.append(HomeTeams[x] + " VS " + VisitorTeams[x])

#Place Moneylines together per match
MoneyPairs = []
for y in range(0, len(MoneyLines)-1):
    if y%2 == 0:
        MoneyPairs.append(MoneyLines[y] + " VS " + MoneyLines[y+1])

Hackbook_Catalogue = []
for x in range(0, len(Gambling_Days)):
    new_Hackbook = Hackbook(Gambling_Days[x], Times[x], HomeTeams[x], VisitorTeams[x], MoneyLines[x*2], MoneyLines[x*2+1], "MyBookie")
    new_Hackbook.TimeFix(2)
    Hackbook_Catalogue.append(new_Hackbook)


JSON_Catalogue = []
for hb in Hackbook_Catalogue:
    #Write Hackbook Information to Dictionary
    new_dictionary = {"GameDay": hb.date, "GameTime": hb.time, "HomeTeam": hb.home_team, "VisitorTeam": hb.visitor_team,
        "MoneyLine1": hb.m1, "MoneyLine2": hb.m2, "Website": hb.website}
    print(new_dictionary)
    #Serialize the JSON
    json_object = json.dumps(new_dictionary, indent = 4)
    JSON_Catalogue.append(json_object)

#Write to a Sample Json Output File
with open("MyBookie_sample.json", "w") as output_file:
    output_file.write("[\n")
    for j in range(0, len(JSON_Catalogue)):
        if (j == len(JSON_Catalogue)-1):
            output_file.write(JSON_Catalogue[j] +"\n")
        else:
            output_file.write(JSON_Catalogue[j] +",\n")
    output_file.write("]")
    output_file.close()