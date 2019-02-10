class time():
	def __init__(self,time):
		self.time=time
		self.minutes,self.seconds=divmod(time,60)
		self.hours,self.minutes=divmod(self.minutes,60)

	def __str__(self):
		return ('%.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds)

	def is_after(self,other):
		return other.time>self.time
time1=time(3659)
time2=time(325)

print(time2.is_after(time1))
