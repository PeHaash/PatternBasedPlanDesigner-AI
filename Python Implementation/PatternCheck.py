###
# Pattern Check
###

# We Have A Main Func: Evaluate
# Evaluate(Plan,"Name Of Pattern")
# Evaluate(Room,"Name Of Pattern")
# etc...
# Each Evaluation, Return 2 things:(maybe a class)
# ( Pattern Code , Pattern Score )
# Pattern Score:
# 1: Pattern Is OK!!
# [0,1) : Pattern is not considered, But, We have an indicator to see how much pattern is considered or not
# This is crucial because we need to evaluate plans in Genetic Algorithm

def PGSubspaceMaxMin(Plan):
    """Patten General: Subspaces Min and Max be considered,
    Also Check Whether Some Subspaces are allocated to unused spaces!"""
    minSS, maxSS = Plan.HyperParameters.MinSubspace, Plan.HyperParameters.MaxSubspace
    numofss = [0 for i in range(Plan.HyperParameters.RoomNumber)]
    for ss in Plan.Subspace:
        numofss[ss.Room] += 1
    error = sum(
        [max(0, nss - maxSS) + max(0, minSS - nss) + (nss if isAc == 0 else 0) for nss, isAc in zip(numofss, Plan.Features.ActiveRooms)]
    )
    return 1 - (error / Plan.SubspaceSize)


def PGSubspaceConnectivity(Plan):
    """Pattern General: All Sucspcases Should be Connected with eachother"""
    ssbyroom = [[] for i in range(Plan.HyperParameters.RoomNumber)]
    for i, ss in enumerate(Plan.Subspace):
        ssbyroom[ss.Room].append(i)
    # print("ssbyroom",ssbyroom)
    error = sum(Plan.SubspaceConnections.DisjointnessOfElements(ssbr) for ssbr in ssbyroom)
    # all = Plan.SubspaceSize
    # Plan.SubspaceConnections
    return 1 - (error / Plan.SubspaceSize)


def PGAllConnected(Plan):
    """Pattern General: All Rooms Has to be connected"""
    error = Plan.RoomConnections.DisjointnessOfElements([i for i in range(Plan.HyperParameters.RoomNumber)])
    return 1 - (error / Plan.HyperParameters.RoomNumber)

    # dset=DISJOINSET(RoomNumber)
    # for i in range(RoomNumber):
    #     for j in range(i):
    #         if len(OpeningsBetweenRooms[i][j])>0:
    #             dset.Join(i,j)
    # Scores.append((PatternCode,1.0 if dset.NumOfSets()==1 else 0.0))
    # return 0


def Evaluate(Plan, PatternCode):
    # TEMP: we send Plan as EvaluationMaterial, just to can set Plan.Score Here in Evaluate (this may have some benefits)
    Patterns = {"PGssMm": PGSubspaceMaxMin, "PGssC": PGSubspaceConnectivity, "PGAC": PGAllConnected}
    if PatternCode in Patterns:
        TestScore = Patterns[PatternCode](Plan)
        Plan.Score += TestScore
        return
    else:
        print("Pattern Not Found")
        return -1
