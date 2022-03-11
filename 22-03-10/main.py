# to be exported by anaconda!
from importlib import reload


import NumericDataMaker
import PlanMaker
import PatternCheck
import TextBasedGraphicExport
import SpeedTracker
import GeneticAlgorithm


def ReloadAllImports():
    reload(NumericDataMaker)
    reload(PlanMaker)
    reload(PatternCheck)
    reload(TextBasedGraphicExport)
    reload(SpeedTracker)
    reload(GeneticAlgorithm)


class HYPERPARAMETERS:
    def __init__(self, RoomNumber, MinSubspace, MaxSubspace, DateCode):
        self.RoomNumber = RoomNumber
        self.MinSubspace = MinSubspace
        self.MaxSubspace = MaxSubspace
        self.DateCode = DateCode


class FEATURES:
    def __init__(self, Width, Depth, ActiveRooms, TrueNorth, EntrancePosition):
        self.Width = Width  # cm, in X
        self.Depth = Depth  # cm, in Y
        self.TrueNorth = TrueNorth  # degree
        self.EntrancePosition = EntrancePosition
        self.ActiveRooms = ActiveRooms


def mainOld():
    RunOnlyOne = True
    ##
    # t0 = time.time()
    ##
    # TextBasedGraphicExport.SetDateCode("22-03-06")

    HyperParameters = HYPERPARAMETERS(
        RoomNumber=4,
        MinSubspace=2,
        MaxSubspace=10,
        DateCode="0 MainBranch"
    )
    Features = FEATURES(
        Width=1000,
        Depth=1700,
        TrueNorth=60,
        EntrancePosition=0.80,
        ActiveRooms=[1, 1, 1, 1, 1, 1]
    )

    Run = True
    while Run:
        NumericData = NumericDataMaker.RandomNumericData(NumberOfSubspaces=16)
        Plan = PlanMaker.GeneratePlanFromNumericData(
            HyperParameters=HyperParameters,
            Features=Features,
            NumericData=NumericData
        )
        print("Plan Score is:", Plan.Score)
        if RunOnlyOne:
            Run = False
        # else:
        #     time.sleep(1)

    # if Plan.Score.Dead:
    #   ## ...
    #   pass
    # Score = PatternCheck.Scoring(Plan)
    ##
    # t1 = time.time()
    # print(t1-t0)
    ##


def mainOld2():
    # Speed Check
    st = SpeedTracker.SPEEDTRACKER()
    # Initials
    HyperParameters = HYPERPARAMETERS(
        RoomNumber=6,
        MinSubspace=1,
        MaxSubspace=20,
        DateCode="0 MainBranch"
    )
    Features = FEATURES(
        Width=1000,
        Depth=1700,
        TrueNorth=60,
        EntrancePosition=0.80,
        ActiveRooms=[1, 1, 1, 1, 1, 1]
    )
    ExportPlace = TextBasedGraphicExport.TBGE("NewTBGE", "0 MainBranch")
    Plans = [PlanMaker.GeneratePlanFromNumericData(
        HyperParameters=HyperParameters,
        Features=Features,
        NumericData=NumericDataMaker.RandomNumericData(NumberOfSubspaces=32),
        TBGEElement=ExportPlace,
        TBGEFrame=i
    ) for i in range(10)
    ]
    ExportPlace.End()
    Plans.sort(key=lambda x: -x.Score)
    for pl in Plans:
        print(pl.Score)

    st.Lap()


def main():
    # Speed Check
    st = SpeedTracker.SPEEDTRACKER()
    # Initials
    HyperParameters = HYPERPARAMETERS(
        RoomNumber=6,
        MinSubspace=2,
        MaxSubspace=10,
        DateCode="0 MainBranch"
    )
    Features = FEATURES(
        Width=1000,
        Depth=1700,
        TrueNorth=60,
        EntrancePosition=0.80,
        ActiveRooms=[1, 1, 1, 1, 1, 1]
    )

    Gene = GeneticAlgorithm.POPULATION(
        SizeOfSet=300,
        DataSize=16 * 8,
        ScoreFunction=PlanMaker.ScoreFunction,
        Features=Features,
        HyperParameters=HyperParameters,
        SurvivalRate=0.9,
        MutationRate=0.9,
        MutationMove=0.15
    )
    ExportPlace = TextBasedGraphicExport.TBGE("NewTBGE", "0 MainBranch")
    # RowSize = 10  # cm
    # Gap = 30  # cm
    # PlanMaker.ScoreFunction(HyperParameters, Features, [1 for i in range(16 * 8)])
    # return
    GoalScore = 3
    for i in range(150):
        Gene.RunGeneration()
        print("Generation #{} Best Score:{}".format(i + 1, Gene.BestScore()))
        # print(Gene.BestData())
        bData = Gene.BestData()
        bData2d = [[bData[i * 8 + j]for j in range(8)] for i in range(16)]
        PlanMaker.GeneratePlanFromNumericData(
            Features=Features,
            HyperParameters=HyperParameters,
            NumericData=bData2d,
            TBGEElement=ExportPlace,
            TBGEFrame=i)
        # BestPlanNow.ExportTBGE()
        if Gene.BestScore() >= GoalScore:
            print("yooohoooooo!!!!")
            break
    ExportPlace.End()
    print("END!")
    st.Lap()


if __name__ == '__main__':
    ReloadAllImports()
    main()
