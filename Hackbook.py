nba_teams = {
    "Atlanta Hawks": "ATL Hawks",
    "Boston Celtics": "BOS Celtics",
    "Brooklyn Nets": "BKN Nets",
    "Charlotte Hornets": "CHA Hornets",
    "Chicago Bulls": "CHI Bulls",
    "Cleveland Cavaliers": "CLE Cavaliers",
    "Dallas Mavericks": "DAL Mavericks",
    "Denver Nuggets": "DEN Nuggets",
    "Detroit Pistons": "DET Pistons",
    "Golden State Warriors": "GSW Warriors",
    "Houston Rockets": "HOU Rockets",
    "Indiana Pacers": "IND Pacers",
    "LA Clippers": "LAC Clippers",
    "Los Angeles Lakers": "LAL Lakers",
    "Memphis Grizzlies": "MEM Grizzlies",
    "Miami Heat": "MIA Heat",
    "Milwaukee Bucks": "MIL Bucks",
    "Minnesota Timberwolves": "MIN Timberwolves",
    "New Orleans Pelicans": "NOP Pelicans",
    "New York Knicks": "NYK Knicks",
    "Oklahoma City Thunder": "OKC Thunder",
    "Orlando Magic": "ORL Magic",
    "Philadelphia 76ers": "PHI 76ers",
    "Phoenix Suns": "PHX Suns",
    "Portland Trail Blazers": "POR Trail Blazers",
    "Sacramento Kings": "SAC Kings",
    "San Antonio Spurs": "SAS Spurs",
    "Toronto Raptors": "TOR Raptors",
    "Utah Jazz": "UTA Jazz",
    "Washington Wizards": "WAS Wizards"
}

class Hackbook():
	def __init__(self, date, time, home_team, visitor_team, m1, m2, website):
		self.date = date
		self.time = time
		self.home_team = self.team_name_fix(home_team)
		self.visitor_team = self.team_name_fix(visitor_team)
		self.m1 = m1
		self.m2 = m2
		self.website = website
	def TimeFix(self, fixBY):
		if self.time == "Now":
			return
		if len(self.time) == 6:
			self.time = '0'+ self.time
		parse_int = int(self.time[0:2])
		parse_mm = self.time[5:7]
		parse_min = self.time[3:5]
		new_int = parse_int + fixBY
		if (new_int < 0 or (parse_int == 12 and fixBY < 0)):
			if (new_int < 0):
				new_int = new_int + 12
			if parse_mm == 'AM':
				parse_mm = 'PM'
			elif parse_mm == 'PM':
				parse_mm = 'AM'
		FixTime = str(new_int) + ":" + parse_min + parse_mm
		self.time = FixTime
		self.time = self.time.replace("P", " P").replace("A", " A")
	def display(self):
		print("Game Day: " + self.date)
		print("Game Time: " + self.time)
		print("Home Team: " + self.home_team + " at " + self.m1)
		print("Visitor Team: " + self.visitor_team + " at " + self.m2)
	def team_name_fix(self, team_name):
		if team_name in nba_teams:
			return nba_teams[team_name]
		else:
			return team_name


