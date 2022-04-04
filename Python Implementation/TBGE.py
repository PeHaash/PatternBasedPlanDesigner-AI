# print("DILDO!")

class DATE:
	def __init__(self):
		self.date=""

now=DATE()

class TBGE:
	def __init__(self,name):
		Address="E:/Desktop/ML class/Pattern-Based Plan Designer AI/"+now.date+"/"
		self.file=open(Address+name+".TBGE","w")
	def AddLine(self,p1,p2,text="-"):
		x0,y0,x1,y1=[str(p) for p in (p1[0],p1[1],p2[0],p2[1])]
		Command="LINE: "+"X0="+x0+" Y0="+y0 +" X1="+x1+" Y1="+y1+" Text="+text+"\n"
		self.file.write(Command)
	def AddRectangle(self,position,text=""):
		x0,y0,x1,y1=[str(p) for p in position]
		Command="REC: "+"X0="+x0+" Y0="+y0 +" X1="+x1+" Y1="+y1+" Text="+text+"\n"
		self.file.write(Command)
		# pass
	def End(self):
		self.file.close()

def SetDateCode(DATE):
	global now
	now.date=DATE

