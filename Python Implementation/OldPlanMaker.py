# OldPlanMaker


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


def oldshit():
	
	Export=TextBasedGraphicExport.TBGE("export")




	Subspace=[SUBSPACE(GlobalData, ssDiscrip) for ssDiscrip in NumericData]
	SetSubspaceCode(Subspace)


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

	Plan=PLAN(Subspace=Subspace)

	## find adjs: set Doors and Merge spaces
	
	for o in Subspace:
		Export.AddRectangle(position=o.Position,text="-".join([str(o.Room),str(o.SubspcaceCode)]))

	Export.End()

