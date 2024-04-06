import requests 
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from Hackbook import Hackbook
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
def DayFinder(s):
    if (s != "Spread" and s != "Total" and s!= "Moneyline"):
        return s
#Beautiful Soup Timezone is Off by 4 Hours
def TimeFix(time):
    if len(time) == 6:
        time = '0'+time
    parse_int = int(time[0:2])
    parse_mm = time[5:7]
    parse_min = time[3:5]
    new_int = parse_int - 4
    if new_int < 0:
        new_int = new_int + 12
        if parse_mm == 'AM':
            parse_mm = 'PM'
        else:
            parse_mm = 'AM'
    FixTime = str(new_int) + ":" + parse_min + parse_mm
    return(FixTime)


htmldata = getdata("https://sportsbook.draftkings.com/leagues/basketball/nba") 
soup = BeautifulSoup(htmldata, 'html.parser')

Gambling_Days = []
MoneyLines = []
Times = []
Teams = []

for day in soup.find_all("div", class_="sportsbook-table-header__title"):
    x = day.decode_contents()
    x = x.replace("<span>", "")
    x = x.replace("</span>","")
    gd = DayFinder(x)
    if gd != None:
        Gambling_Days.append(gd)

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
for z in range(0, len(Times)-1):
    if z%2 == 0:
        GameTime.append(Times[z])
#Place Teams together
Matches = []
for x in range(0, len(Teams)-1):
    if x%2 == 0:
        Matches.append(Teams[x] + " VS " + Teams[x+1])
#Place Moneylines together per match
MoneyPairs = []
for y in range(0, len(MoneyLines)-1):
    if y%2 == 0:
        MoneyPairs.append(MoneyLines[y] + " VS " + MoneyLines[y+1])

Hackbook_Catalogue = []
for x in range(0, len(GameTime)):
    new_Hackbook = Hackbook("Today?", GameTime[x], Teams[x*2+1], Teams[x*2], MoneyLines[x*2+1], MoneyLines[x*2])
    new_Hackbook.TimeFix(-4)
    Hackbook_Catalogue.append(new_Hackbook)
for y in Hackbook_Catalogue:
    y.display()
    print("\n")

