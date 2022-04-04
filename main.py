## to be exported by anaconda!
from importlib import reload
import time

import NumericDataMaker
import PlanMaker
import PatternCheck
import TextBasedGraphicExport



class HYPERPARAMETERS:
	def __init__(self, RoomNumber, MinSubspace, MaxSubspace, DateCode):
		self.RoomNumber=RoomNumber
		self.MinSubspace=MinSubspace
		self.MaxSubspace=MaxSubspace
		self.DateCode=DateCode

class FEATURES:
	def __init__(self,Width,Depth,ActiveRooms,TrueNorth,EntrancePosition):
		self.Width=Width ## cm, in X
		self.Depth=Depth ## cm, in Y
		self.TrueNorth=TrueNorth ## degree
		self.EntrancePosition=EntrancePosition
		self.ActiveRooms=ActiveRooms

"""
NumericalExpressionOfPlan
NumericData --> some numbers, only
Plan --> a class of Subspaces
Subspace
"""



def main():
	RunOnlyOne=True
	##
	t0=time.time()
	##
	# TextBasedGraphicExport.SetDateCode("22-03-06")

	HyperParameters=HYPERPARAMETERS(
		RoomNumber=2,
		MinSubspace=2,
		MaxSubspace=10,
		DateCode="22-03-07"
		)
	Features=FEATURES(
		Width=1000,
		Depth=1700,
		TrueNorth=60,
		EntrancePosition=0.80,
		ActiveRooms=[1,1,1,1,1,1]
		)

	Run=True
	while Run:
		NumericData=NumericDataMaker.RandomNumericData(NumberOfSubspaces=16)
		Plan=PlanMaker.GeneratePlanFromNumericData(
			HyperParameters=HyperParameters,
			Features=Features,
			NumericData=NumericData
			)
		if RunOnlyOne:
			Run=False
		else:
			time.sleep(1)

	# if Plan.Score.Dead:
	# 	## ...
	# 	pass
	# Score=PatternCheck.Scoring(Plan)
	##
	t1=time.time()
	print(t1-t0)
	##








if __name__ == '__main__':
	reload(NumericDataMaker)
	reload(PlanMaker)
	reload(PatternCheck)
	reload(TextBasedGraphicExport)
	main()
