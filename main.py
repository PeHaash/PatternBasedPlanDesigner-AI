## to be exported by anaconda!
from importlib import reload

import ClassDefinitions
import RandomNumberMaker
import PlanGenerator
import PatternCheck

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
		## input
		self.X=1200 ## cm
		self.Y=1500 ## cm
		self.TrueNorth=65 ## degree
		self.EntrancePosition=0.53
		self.ActiveRooms=[1,0,1,1,0,1]


# sarvenaz

def main():
	reload(RandomNumberMaker)
	reload(PlanGenerator)
	reload(PatternCheck)
	print("hello")
	GlobalData=GLOBALDATA()
	# Inputs=INPUTS()
	PlanGenerator.GenerateFrom(GlobalData=GlobalData,SubspaceDiscription=RandomNumberMaker.GenerateRandom(NumberOfSubspaces=8))


if __name__ == '__main__':
	main()