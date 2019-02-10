class Kangaroo:
	def __init__(self):
		self.pouch_contents=[]
	def put_in_pouch(self,obj):
		self.pouch_contents.append(obj)
	def __str__(self):
		return str(self.pouch_contents)

content1=Kangaroo()
content2=Kangaroo()
content2.pouch_contents.append('This is task of lab five')
content1.put_in_pouch(content2)

for item in content1.pouch_contents:
	print('content of pouch in list: ',item)
