# Genetic Algorithm! v2.0

class SPECIES:
    def __init__(self, SizeOfSet, DataShape, FitnessFunction, HyperParameters, Features, SurvivalRate, MutationRate, MutationMove):
        self.SizeOfSet = SizeOfSet
        self.FitnessFunction = FitnessFunction
        self.HyperParameters = HyperParameters
        self.Features = Features
        self.SurvivalRate = SurvivalRate
        self.MutationRate = MutationRate
        self.MutationMove = MutationMove

        for i in range(SizeOfSet):
            pass

        self.SizeOfSet = SizeOfSet
        self.DataShape = DataShape
