class TimeSpan:
	#Constructors
	def __init__(self, sec = 0, min = 0, hour = 0):
		self.__sec = sec
		self.__min = min
		self.__hour = hour
		self.convertAndDisperse()
		
	#Getters
	def getSeconds(self):
		return self.__sec
	def getMinutes(self):
		return self.__min
	def getHours(self):
		return self.__hour

	#Setters
	def setTime(self, seconds, minutes, hours):
		self.__sec = seconds
		self.__min = minutes
		self.__hour = hours

	#Helpers
	def convertAndDisperse(self):
		totalSeconds = self.getSeconds() + ( 60 * self.getMinutes() ) + ( 3600 * self.getHours() )
		counter = 0
		if totalSeconds > 0:
			#get hours
			while totalSeconds > 3600:
				totalSeconds -= 3600
				counter += 1
			actualHours = counter
			#get minutes
			counter = 0
			while totalSeconds > 60:
				totalSeconds -= 60
				counter += 1
			actualMinutes = counter
			#get seconds
			actualSeconds = totalSeconds
			self.setTime(int(actualSeconds), int(actualMinutes), int(actualHours))
		elif totalSeconds < 0:
			#get hours
			while totalSeconds < -3600:
				totalSeconds += 3600
				counter -= 1
			actualHours = counter
			#get minutes
			counter = 0
			while totalSeconds < -60:
				totalSeconds += 60
				counter -= 1
			actualMinutes = counter
			#get seconds
			actualSeconds = totalSeconds
			self.setTime(int(actualSeconds), int(actualMinutes), int(actualHours))
		else:
			self.setTime(0,0,0)
		
	#Operator Overloads
	#addition
	def __add__(self, rhs):
		tempTime = TimeSpan(self.getSeconds() + rhs.getSeconds(), 
							self.getMinutes() + rhs.getMinutes(),
							self.getHours() + rhs.getHours())
		return tempTime
	#subtraction
	def __sub__(self, rhs):
		tempTime = TimeSpan(self.getSeconds() - rhs.getSeconds(),
							self.getMinutes() - rhs.getMinutes(),
							self.getHours() - rhs.getHours())
		return tempTime
	#unary negation
	def __neg__(self):
		return TimeSpan(-self.getSeconds(), -self.getMinutes(), -self.getHours())
	# +=
	def __iadd__(self, rhs):
		self.setTime(self.getSeconds() + rhs.getSeconds(),
					 self.getMinutes() + rhs.getMinutes(),
					 self.getHours() + rhs.getHours())
		self.convertAndDisperse()
		return self
	# -=
	def __isub__(self, rhs):
		self.setTime(self.getSeconds() - rhs.getSeconds(),
					 self.getMinutes() - rhs.getMinutes(),
					 self.getHours() - rhs.getHours())
		self.convertAndDisperse()
		return self
	# ==
	def __eq__(self, rhs):
		if self.getHours() != rhs.getHours() or self.getMinutes() != rhs.getMinutes() or self.getSeconds() != rhs.getSeconds():
			return False
		return True
	# <
	def __lt__(self, rhs):
		selfSeconds = self.getSeconds() + ( 60 * self.getMinutes() ) + ( 3600 * self.getHours() )
		rhsSeconds = rhs.getSeconds() + (60 * rhs.getMinutes() ) + (3600 * rhs.getHours() )
		return selfSeconds < rhsSeconds
	# <=
	def __le__(self, rhs):
		selfSeconds = self.getSeconds() + ( 60 * self.getMinutes() ) + ( 3600 * self.getHours() )
		rhsSeconds = rhs.getSeconds() + (60 * rhs.getMinutes() ) + (3600 * rhs.getHours() )
		return selfSeconds <= rhsSeconds
	# >
	def __gt__(self, rhs):
		selfSeconds = self.getSeconds() + ( 60 * self.getMinutes() ) + ( 3600 * self.getHours() )
		rhsSeconds = rhs.getSeconds() + (60 * rhs.getMinutes() ) + (3600 * rhs.getHours() )
		return selfSeconds > rhsSeconds
	# >=
	def __ge__(self, rhs):
		selfSeconds = self.getSeconds() + ( 60 * self.getMinutes() ) + ( 3600 * self.getHours() )
		rhsSeconds = rhs.getSeconds() + (60 * rhs.getMinutes() ) + (3600 * rhs.getHours() )
		return selfSeconds >= rhsSeconds
	#print
	#Exact Output: "Hours: X, Minutes: X, Seconds: X"
	def __str__(self):
		return "Hours: " + str(self.getHours()) + ", Minutes: " + str(self.getMinutes()) + ", Seconds: " + str(self.getSeconds())