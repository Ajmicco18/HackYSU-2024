import requests 
import urllib.request
import json
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from Hackbook import Hackbook
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
def DayFinder(s):
    if (s != "Spread" and s != "Total" and s!= "Moneyline"):
        return s

htmldata = getdata("https://sportsbook.draftkings.com/leagues/basketball/nba") 
soup = BeautifulSoup(htmldata, 'html.parser')

Gambling_Days = []
MoneyLines = []
Times = []
Teams = []

for card in soup.find_all("div", class_="parlay-card-10-a"):
    for day in soup.find_all("div", class_="sportsbook-table-header__title"):
        x = day.decode_contents()
        x = x.replace("<span>", "")
        x = x.replace("</span>","")
        gd = DayFinder(x)
        if gd != None:
            Gambling_Days.append(gd)

for time in soup.find_all("span", class_="event-cell__time"):
    t = time.decode_contents()
    Times.append("Now")

for time in soup.find_all("span", class_="event-cell__start-time"):
    t = time.decode_contents()
    Times.append(t)

for team in soup.find_all("div", class_="event-cell__name-text"):
    team = team.decode_contents()
    Teams.append(team)


for ml in soup.find_all("span", class_="sportsbook-odds american no-margin default-color"):
    MoneyLines.append(ml.decode_contents())

#Duplicate Error with BS4
GameTime=[]
for z in range(0, len(Times)):
    if z%2 == 0:
        GameTime.append(Times[z])

#Place Teams together
Matches = []
for x in range(0, len(Teams)):
    if x%2 == 0:
        Matches.append(Teams[x] + " VS " + Teams[x+1])
#Place Moneylines together per match
MoneyPairs = []
for y in range(0, len(MoneyLines)):
    if y%2 == 0:
        MoneyPairs.append(MoneyLines[y] + " VS " + MoneyLines[y+1])

Hackbook_Catalogue = []
for x in range(0, len(GameTime)):
    new_Hackbook = Hackbook(datetime.now().strftime("%m-%d"), GameTime[x], Teams[x*2+1], Teams[x*2], MoneyLines[x*2+1], MoneyLines[x*2], "DraftKings")
    new_Hackbook.TimeFix(-4)
    Hackbook_Catalogue.append(new_Hackbook)

JSON_Catalogue = []
for hb in Hackbook_Catalogue:
    new_dictionary = {"GameDay": hb.date, "GameTime": hb.time, "HomeTeam": hb.home_team, "VisitorTeam": hb.visitor_team,
        "MoneyLine1": hb.m1, "MoneyLine2": hb.m2, "Website": hb.website}
    print(new_dictionary)
    #Serialize the JSON
    json_object = json.dumps(new_dictionary, indent = 4)
    JSON_Catalogue.append(json_object)

#Write to a Sample Json Output File
with open("DraftKings_sample.json", "w") as output_file:
    output_file.write("[\n")
    for j in range(0, len(JSON_Catalogue)):
        if (j == len(JSON_Catalogue)-1):
            output_file.write(JSON_Catalogue[j] +"\n")
        else:
            output_file.write(JSON_Catalogue[j] +",\n")
    output_file.write("]")
    output_file.close()