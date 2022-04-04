## hello
## 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode, 6: Has Door?, 7: Has Fenestration?

from importlib import reload
import math
import TextBasedGraphicExport
import Subspace
import Room
import DisjointSet

def ReloadAllImports():
	reload(TextBasedGraphicExport)
	reload(Subspace)
	reload(Room)
	reload(DisjointSet)






def Center(pos):
	return ((pos[0]+pos[2])/2,(pos[1]+pos[3])/2)


	

class PLAN:
	def __init__(self, HyperParameters, Features, NumericData):
		Subspace=[Subspace.SUBSPACE(HyperParameters, numericDiscrip) for numericDiscrip in NumericData]
		self.SubspaceSize=len(Subspace)
		## Add Subspace Codes:
		Subspace.sort(key=lambda x:(x.Room,x.SubspcaceCode))
		for i in range(self.SubspaceSize):
			Subspace[i].SubspcaceCode=Subspace[i-1].SubspcaceCode+1 if Subspace[i].Room==Subspace[i-1].Room else 0
		self.Subspace=Subspace
		self.Room=[Room.ROOM() if IsAcitveRoom==1 else None for IsAcitveRoom in Features.ActiveRooms]
		self.Scores=[]
		self.Features=Features
		self.GraphicExport=[]
		self.RoomConnections=DisjointSet.DISJOINSET(HyperParameters.RoomNumber)
		self.ActiveRoomCodes=[i for i in range(HyperParameters.RoomNumber) if Features.ActiveRooms[i]==1]

	def RecursiveSubspacePosition(Subspace,CutOrientation,Size,minX,minY,maxX,maxY):
		if Size==1:
			Subspace[0].Position=[minX,minY,maxX,maxY]
			return Subspace
		SizeDivide2=int(Size/2)
		if CutOrientation=="H":
			Subspace.sort(key=lambda x:x.Yposition)
			ratioY=sum(ss.Yweight for ss in Subspace[:SizeDivide2])/sum(ss.Yweight for ss in Subspace)
			middleY=round(ratioY*(maxY-minY)+minY)
			array1=PLAN.RecursiveSubspacePosition(
				Subspace=Subspace[:SizeDivide2],
				CutOrientation="V",
				Size=Size/2,
				minX=minX,
				minY=minY,
				maxX=maxX,
				maxY=middleY
				)
			array2=PLAN.RecursiveSubspacePosition(
				Subspace=Subspace[SizeDivide2:],
				CutOrientation="V",
				Size=Size/2,
				minX=minX,
				minY=middleY,
				maxX=maxX,
				maxY=maxY
				)
		if CutOrientation=="V":
			Subspace.sort(key=lambda x:x.Xposition)
			ratioX=sum(ss.Xweight for ss in Subspace[:SizeDivide2])/sum(ss.Xweight for ss in Subspace)
			middleX=round(ratioX*(maxX-minX)+minX)
			array1=PLAN.RecursiveSubspacePosition(
				Subspace=Subspace[:SizeDivide2],
				CutOrientation="H",
				Size=Size/2,
				minX=minX,
				minY=minY,
				maxX=middleX,
				maxY=maxY
				)
			array2=PLAN.RecursiveSubspacePosition(
				Subspace=Subspace[SizeDivide2:],
				CutOrientation="H",
				Size=Size/2,
				minX=middleX,
				minY=minY,
				maxX=maxX,
				maxY=maxY
				)
		return array1+array2


	def SetSubspacePositions(self):
		PLAN.RecursiveSubspacePosition(
			Subspace=self.Subspace,
			CutOrientation="H",
			Size=self.SubspaceSize,
			minX=0,
			minY=0,
			maxX=self.Features.Width,
			maxY=self.Features.Depth
			)

	def MakeConnection(self,Index1,Index2,Point1,Point2):
		if self.Subspace[Index1].Room==self.Subspace[Index2].Room:
			## They are in same room
			pass
		elif self.Subspace[Index1].HasOpening==True and self.Subspace[Index2].HasOpening==True:
			## We have a door here
			pass
		else:
			## Just Simple Wall
			pass


	def MergeSubspacesAndFindDoors(self):
		## FIND CONNECTIONS:

		sweepX=set(ss.Position[0] for ss in self.Subspace)|set(ss.Position[2] for ss in self.Subspace)
		sweepY=set(ss.Position[1] for ss in self.Subspace)|set(ss.Position[3] for ss in self.Subspace)
		minXs={xx:[] for xx in sweepX}
		minYs={yy:[] for yy in sweepY}
		maxXs={xx:[] for xx in sweepX}
		maxYs={yy:[] for yy in sweepY}

		for i,ss in enumerate(self.Subspace):
			minXs[ss.Position[0]].append(i)
			minYs[ss.Position[1]].append(i)
			maxXs[ss.Position[2]].append(i)
			maxYs[ss.Position[3]].append(i)

		for swY in sweepY:
			for r1 in minYs[swY]:
				AminX,AminY,AmaxX,AmaxY=self.Subspace[r1].Position
				for r2 in maxYs[swY]:
					BminX,BminY,BmaxX,BmaxY=self.Subspace[r2].Position
					if AminX<BmaxX and BminX<AmaxX:
						# y=swY
						aa,x1,x2,bb=sorted([AminX,AmaxX,BminX,BmaxX])
						self.MakeConnection(r1,r2,(x1,swY),(x2,swY))
						self.GraphicExport.append((Center(self.Subspace[r1].Position),Center(self.Subspace[r2].Position)))
		
		for swX in sweepX:
			for r1 in minXs[swX]:
				AminX,AminY,AmaxX,AmaxY=self.Subspace[r1].Position
				for r2 in maxXs[swX]:
					BminX,BminY,BmaxX,BmaxY=self.Subspace[r2].Position
					if AminY<BmaxY and BminY<AmaxY:
						# x=swX
						aa,y1,y2,bb=sorted([AminY,AmaxY,BminY,BmaxY])
						self.MakeConnection(r1,r2,(swX,y1),(swX,y2))
						self.GraphicExport.append((Center(self.Subspace[r1].Position),Center(self.Subspace[r2].Position)))

	def ExportTBGE(self):
		Export=TextBasedGraphicExport.TBGE("Export")
		for o in self.Subspace:
			Export.AddRectangle(position=o.Position,text="-".join([str(o.Room),str(o.SubspcaceCode)]))
		for row in self.GraphicExport:
			Export.AddLine(row[0],row[1])
		Export.End()

	def SetFenestrations(self):
		pass

	def SetEntranceDoor(self):
		pass





def GeneratePlanFromNumericData(HyperParameters, Features, NumericData):
	ReloadAllImports()
	Plan=PLAN(HyperParameters=HyperParameters, Features=Features, NumericData=NumericData)
	# if PatternCheck.CheckCountOfEachSubspaceInEachRoom(Plan)=="BAD":
	# 	return yeChizeBad
	Plan.SetSubspacePositions()
	Plan.MergeSubspacesAndFindDoors()
	Plan.SetFenestrations()
	Plan.SetEntranceDoor()
	Plan.ExportTBGE()
	return Plan

