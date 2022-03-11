# Genetic Algorithm! v2.0
import random


class SPECIES:
    def __init__(self, Data):
        self.Data = Data
        self.Score = 0


class POPULATION:
    def __init__(self, SizeOfSet, DataSize, ScoreFunction, HyperParameters, Features, SurvivalRate, MutationRate, MutationMove):
        self.SizeOfSet = SizeOfSet
        self.ScoreFunction = ScoreFunction
        self.HyperParameters = HyperParameters
        self.Features = Features
        self.SurvivalRate = SurvivalRate
        self.SizeAfterKillExcess = int(SurvivalRate * SizeOfSet)
        self.MutationRate = MutationRate
        self.MutationMove = MutationMove
        self.SizeOfSet = SizeOfSet
        self.DataSize = DataSize
        self.Species = [SPECIES([random.random() for j in range(DataSize)]) for i in range(SizeOfSet)]
        if self.SizeAfterKillExcess < 2:
            print("IT WONT WORK")

    def Crossover(self):
        for i in range(self.SizeOfSet - self.SizeAfterKillExcess):
            A, B = random.sample(self.Species[:self.SizeAfterKillExcess], 2)
            # self.Species.append(SPECIES([(a * A.Score + b * B.Score) / (A.Score + B.Score) for (a, b) in zip(A.Data, B.Data)]))
            self.Species.append(SPECIES([a if random.uniform(0, A.Score + B.Score) > B.Score else b for (a, b) in zip(A.Data, B.Data)]))

    def Mutate(self):
        for i in range(1, self.SizeOfSet):  # self.KilllExcess...
            for j in range(self.DataSize):
                if random.random() < self.MutationRate:
                    self.Species[i].Data[j] =\
                        max(0.01, min(0.99, self.Species[i].Data[j] + random.uniform(-self.MutationMove / 2, self.MutationMove / 2)))

    def RunGeneration(self):
        # Score Them and sort
        for sp in self.Species:
            sp.Score = self.ScoreFunction(self.HyperParameters, self.Features, sp.Data)
        self.Species.sort(key=lambda x: x.Score, reverse=True)
        # Kill excess
        self.Species = self.Species[:self.SizeAfterKillExcess]
        # Crossover
        self.Crossover()
        # Mutate
        self.Mutate()

    def BestScore(self):
        return self.Species[0].Score

    def BestData(self):
        return self.Species[0].Data


def Scorr(HyperParameters, Features, NumericData):
    return 10 - sum(abs(nd - 0.375) for nd in NumericData)


def main():
    GenePool = POPULATION(
        SizeOfSet=10,
        DataSize=5,
        ScoreFunction=Scorr,
        HyperParameters=None,
        Features=None,
        SurvivalRate=0.5,
        MutationRate=0.5,
        MutationMove=0.1
    )
    for i in range(200):
        GenePool.RunGeneration()
        print("Generation: {} Score: {}".format(i, GenePool.BestScore()))
    print(GenePool.BestData())


if __name__ == "__main__":
    main()
