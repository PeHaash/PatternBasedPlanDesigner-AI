## to be exported by anaconda!
from importlib import reload
import time

import ClassDefinitions
import RandomNumberMaker
import PlanGenerator
import PatternCheck
import TBGE

"""
0: Living Room
1: Kitchen
2: Bedroom
3: WC
4: Bathroom
5: Entrance Room
6: --- (pazirayi) """

class GLOBALDATA:
	def __init__(self):
		## hyper parameters
		self.RoomNumber=6
		self.MinSubspace=3
		self.MaxSubspace=10
		## input
		self.X=1200 ## cm
		self.Y=1500 ## cm
		self.TrueNorth=65 ## degree
		self.EntrancePosition=0.53
		self.ActiveRooms=[1,1,1,1,1,1] ## 0...5 



def main():
	t0=time.time()
	reload(RandomNumberMaker)
	reload(PlanGenerator)
	reload(PatternCheck)
	reload(TBGE)

	TBGE.SetDateCode("22-03-03")
	GlobalData=GLOBALDATA()

	PlanGenerator.GenerateFrom(GlobalData=GlobalData,SubspaceDiscription=RandomNumberMaker.GenerateRandom(NumberOfSubspaces=32))
	t1=time.time()
	print(t1-t0)
	# while 1:
	# 	PlanGenerator.GenerateFrom(GlobalData=GlobalData,SubspaceDiscription=RandomNumberMaker.GenerateRandom(NumberOfSubspaces=32))
	# 	time.sleep(1)


if __name__ == '__main__':
	main()