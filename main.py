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


"""
NumericalExpressionOfPlan
NumericData --> some numbers, only
Plan --> a class of Subspaces
Subspace
"""


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


def main():
    # Speed Check
    st = SpeedTracker.SPEEDTRACKER()
    # Initials
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
    Plans = [PlanMaker.GeneratePlanFromNumericData(
        HyperParameters=HyperParameters,
        Features=Features,
        NumericData=NumericDataMaker.RandomNumericData(NumberOfSubspaces=16)
    ) for i in range(100)
    ]
    Plans.sort(key=lambda x: -x.Score)
    for pl in Plans:
        print(pl.Score)

    st.Lap()


if __name__ == '__main__':
    ReloadAllImports()
    main()


def mainGA():
    # Initials
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

    Gene = GeneticAlgorithm.POPULATION(
        SizeOfSet=100,
        DataShape=16 * 8,
        ScoreFunction=PlanMaker.ScoreFunction,
        Features=Features,
        HyperParameters=HyperParameters,
        SurvivalRate=0.5,
        MutationRate=0.1,
        MutationMove=0.1
    )

    RowSize = 10  # cm
    Gap = 30  # cm
    for i in range(100):
        Gene.RunGeneration()
        print(Gene.BestScore())
        BestPlanNow = PlanMaker.GeneratePlanFromNumericData(
            Features=Features,
            HyperParameters=HyperParameters,
            NumericData=Gene.BestSpecies)
        BestPlanNow.ExportTBGE(Point0=((i % RowSize) * (Features.Width + Gap), (i // RowSize) * (Features.Depth + Gap)), Append=True)

    Plans = [PlanMaker.GeneratePlanFromNumericData(
        HyperParameters=HyperParameters,
        Features=Features,
        NumericData=NumericDataMaker.RandomNumericData(NumberOfSubspaces=16)
    ) for i in range(100)
    ]
    Plans.sort(key=lambda x: -x.Score)
    for pl in Plans:
        print(pl.Score)
    # st.Lap()
