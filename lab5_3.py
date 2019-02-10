class time():
	def __init__(self,time):
		self.minutes,self.seconds=divmod(time,60)
		self.hours,self.minutes=divmod(self.minutes,60)
		print(('%.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds))

time(3689)
