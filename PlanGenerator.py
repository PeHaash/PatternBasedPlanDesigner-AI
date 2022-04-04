## hello
## 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode, 6: Has Door?, 7: Has Fenestration?
import math
import TBGE

class SUBSPACE:
    def __init__(self, GlobalData, ssDiscrip):
        self.Xposition=    ssDiscrip[0]
        self.Yposition=    ssDiscrip[1]
        self.Xweight=      ssDiscrip[2]
        self.Yweight=      ssDiscrip[3]
        self.Room=     int(ssDiscrip[4]*GlobalData.RoomNumber)
        self.SubspcaceCode=ssDiscrip[5]
        self.HasOpening=   1 if ssDiscrip[6]>0.5 else 0
        self.IsFenestrated=1 if ssDiscrip[7]>0.5 else 0
        self.Position=[]
        self.IsEntranceDoor=False
    def print(self):
    	print("Xpos",self.Xposition,end="-")
    	print("Ypos",self.Yposition,end="-")
    	print("Room",self.Room,end=": ")
    	print(self.SubspcaceCode)


def GeneratePlane(GlobalData,Subspace,CutOrientation,Size,minX,minY,maxX,maxY):
	if Size==1:
		Subspace[0].Position=[minX,minY,maxX,maxY]
		return Subspace
	SizeDivide2=int(Size/2)
	if CutOrientation=="H":
		Subspace.sort(key=lambda x:x.Yposition)
		ratioY=sum(ss.Yweight for ss in Subspace[:SizeDivide2])/sum(ss.Yweight for ss in Subspace)
		middleY=round(ratioY*(maxY-minY)+minY)
		array1=GeneratePlane(
			GlobalData=GlobalData,
			Subspace=Subspace[:SizeDivide2],
			CutOrientation="V",
			Size=Size/2,
			minX=minX,
			minY=minY,
			maxX=maxX,
			maxY=middleY
			)
		array2=GeneratePlane(
			GlobalData=GlobalData,
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
		array1=GeneratePlane(
			GlobalData=GlobalData,
			Subspace=Subspace[:SizeDivide2],
			CutOrientation="H",
			Size=Size/2,
			minX=minX,
			minY=minY,
			maxX=middleX,
			maxY=maxY
			)
		array2=GeneratePlane(
			GlobalData=GlobalData,
			Subspace=Subspace[SizeDivide2:],
			CutOrientation="H",
			Size=Size/2,
			minX=middleX,
			minY=minY,
			maxX=maxX,
			maxY=maxY
			)
	return array1+array2

def Center(pos):
	return ((pos[0]+pos[2])/2,(pos[1]+pos[3])/2)


def GenerateFrom(GlobalData, SubspaceDiscription):
	
	Export=TBGE.TBGE("export")

	Subspace=[SUBSPACE(GlobalData, ssDiscrip) for ssDiscrip in SubspaceDiscription]

	## set subspacecode
	Subspace.sort(key=lambda x:(x.Room,x.SubspcaceCode))
	for i in range(len(Subspace)):
		Subspace[i].SubspcaceCode=Subspace[i-1].SubspcaceCode+1 if Subspace[i].Room==Subspace[i-1].Room else 0

	### check min/max number of SSs  /// unused rooms etc...
	pass
	### recursive shit!
	Subspace=GeneratePlane(
		GlobalData=GlobalData,
		Subspace=Subspace,
		CutOrientation="H",
		Size=len(Subspace),
		minX=0,
		minY=0,
		maxX=GlobalData.X,
		maxY=GlobalData.Y
		)

	## find adjs
	sweepX=set(ss.Position[0] for ss in Subspace)|set(ss.Position[2] for ss in Subspace)
	sweepY=set(ss.Position[1] for ss in Subspace)|set(ss.Position[3] for ss in Subspace)
	
	minXs={xx:[] for xx in sweepX}
	minYs={yy:[] for yy in sweepY}
	maxXs={xx:[] for xx in sweepX}
	maxYs={yy:[] for yy in sweepY}

	for i,ss in enumerate(Subspace):
		minXs[ss.Position[0]].append(i)
		minYs[ss.Position[1]].append(i)
		maxXs[ss.Position[2]].append(i)
		maxYs[ss.Position[3]].append(i)

	for swY in sweepY:
		for r1 in minYs[swY]:
			AminX,AminY,AmaxX,AmaxY=Subspace[r1].Position
			for r2 in maxYs[swY]:
				BminX,BminY,BmaxX,BmaxY=Subspace[r2].Position
				if AminX<BmaxX and BminX<AmaxX:
					
					Export.AddLine(Center(Subspace[r1].Position),Center(Subspace[r2].Position))
	
	for swX in sweepX:
		for r1 in minXs[swX]:
			AminX,AminY,AmaxX,AmaxY=Subspace[r1].Position
			for r2 in maxXs[swX]:
				BminX,BminY,BmaxX,BmaxY=Subspace[r2].Position
				if AminY<BmaxY and BminY<AmaxY:
					Export.AddLine(Center(Subspace[r1].Position),Center(Subspace[r2].Position))

	for o in Subspace:
		Export.AddRectangle(position=o.Position,text="-".join([str(o.Room),str(o.SubspcaceCode)]))

	Export.End()

