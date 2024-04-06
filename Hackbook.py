class Hackbook():
	def __init__(self, date, time, home_team, visitor_team, m1, m2):
		self.date = date
		self.time = time
		self.home_team = home_team
		self.visitor_team = visitor_team
		self.m1 = m1
		self.m2 = m2
	def TimeFix(self, fixBY):
	    if len(self.time) == 6:
	        self.time = '0'+ self.time
	    parse_int = int(self.time[0:2])
	    parse_mm = self.time[5:7]
	    parse_min = self.time[3:5]
	    new_int = parse_int + fixBY
	    if new_int < 0:
	        new_int = new_int + 12
	        if parse_mm == 'AM':
	            parse_mm = 'PM'
	        else:
	            parse_mm = 'AM'
	    FixTime = str(new_int) + ":" + parse_min + parse_mm
	    self.time = FixTime
	    self.time = self.time.replace("P", " P").replace("A", " A")
	def display(self):
		print("Game Day: " + self.date)
		print("Game Time: " + self.time)
		print("Home Team: " + self.home_team + " at " + self.m1)
		print("Visitor Team: " + self.visitor_team + " at " + self.m2)