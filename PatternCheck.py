## We Have A Main Func: Evaluate
## Evaluate(Plan,"Name Of Pattern")
## Evaluate(Room,"Name Of Pattern")
## etc...
## Each Evaluation, Return 2 things:(maybe a class)
## ( Pattern Code , Pattern Score )
## Pattern Score:
## 1: Pattern Is OK!!
## [0,1) : Pattern is not considered, But, We have an indicator to see how much pattern is considered or not
## This is crucial because we need to evaluate plans in Genetic Algorithm

def PGSubspaceMaxMin(Plan):
	Text="Patten General: Subspaces Min and Max be considered, \
	Also Check Whether Some Subspaces are allocated to unused spaces!"
	minSS,maxSS=Plan.HyperParameters.MinSubspace,Plan.HyperParameters.MaxSubspace
	numofss=[0 for i in range(Plan.HyperParameters.RoomNumber)]
	for ss in Plan.Subspace:
		numofss[ss.Room]+=1
	error=sum([max(0,nss-maxSS)+max(0,minSS-nss)+(nss if isAc==0 else 0) for nss,isAc in zip(numofss,Plan.Features.ActiveRooms)])
	return 1-(error/Plan.SubspaceSize)

def PGSubspaceConnectivity(Plan):
	ssbyroom=[[] for i in range (Plan.HyperParameters.RoomNumber)]
	for i,ss in enumerate(Plan.Subspace):
		ssbyroom[ss.Room].append(i)
	# print("ssbyroom",ssbyroom)
	error=sum(Plan.SubspaceConnections.DisjointnessOfElements(ssbr) for ssbr in ssbyroom)
	# all = Plan.SubspaceSize
	# Plan.SubspaceConnections
	return 1-(error/Plan.SubspaceSize)

def Evaluate(Plan,PatternCode):
	## TEMP: we send Plan as EvaluationMaterial, just to can set Plan.Score Here in Evaluate (this may have some benefits)
	Patterns={"PGssMm":PGSubspaceMaxMin,"PGssC":PGSubspaceConnectivity}
	if PatternCode in Patterns:
		TestScore=Patterns[PatternCode](Plan)
		Plan.Score+=TestScore
		return
	else:
		print("Pattern Not Found")
		return -1


def Scoring(Plan):
	pass