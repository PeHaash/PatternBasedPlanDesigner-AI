## speed tracker for code
import time

class SPEEDTRACKER:
	def __init__(self):
		self.time0=time.time()
	def Lap(self):
		timeNow=time.time()
		print("LAP!",timeNow-self.time0)
		self.time0=timeNow
