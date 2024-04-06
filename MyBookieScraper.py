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
    FixTime = str(new_int) + parse_min + parse_mm
    return(FixTime)


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

#Trim Excess Site Material
Gambling_Days = Gambling_Days[0:-1]
Times = Times[0:-1]

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
    new_Hackbook = Hackbook(Gambling_Days[x], Times[x], HomeTeams[x], VisitorTeams[x], MoneyLines[x*2], MoneyLines[x*2+1])
    new_Hackbook.TimeFix(2)
    Hackbook_Catalogue.append(new_Hackbook)
for y in Hackbook_Catalogue:
    y.display()
    print("\n")