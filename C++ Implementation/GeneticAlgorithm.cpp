#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <functional>

using namespace std;

namespace GeneticAlgorithm{
	class SPECIES;
	class POPULATION;
}

class GeneticAlgorithm::SPECIES{
	public:
		vector<float> Data;
		float Score;
		// int DataSize;
		SPECIES(const vector<float>& data){
			Data=data;
			Score = 0;
		}
};


class GeneticAlgorithm::POPULATION{
	private:
		int PopulationSize, DataSize, EliteSize;
		function<float(vector<float>)> ScoreFunction;
		float MutationRate, MutationMove;
		vector<SPECIES> Species;
	public:
		// POPULATION(int, int, int, function<float(vector<float>)>, float, float);
		POPULATION(int popsize, int datasize, int elitesize, function<float(vector<float>)> scorefunc, float mrate, float mmove){
			PopulationSize = popsize;
			DataSize = datasize;
			EliteSize = elitesize;
			ScoreFunction = scorefunc;
			MutationRate = mrate;
			MutationMove = mmove;
			srand(time(NULL));
			for (int i = 0; i < PopulationSize; i++){
				vector<float> randomdata;
				for (int j=0; j < DataSize; j++){
					randomdata.push_back(float(rand()/RAND_MAX));
				}
				Species.push_back(SPECIES(randomdata));
			}
		}
		void RunGeneration(){
			cout <<PopulationSize<<endl;
			// Scoring
			for (int i=0; i<PopulationSize; i++){
				// cout <<"df"<<endl;
				Species[i].Score=ScoreFunction(Species[i].Data);
				// cout <<Species[i].Score<<endl;
			}

		}
};

/*
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
*/
// int main(){
// 	cout <<"meh";
// 	return 0;
// }

/*
#include <functional> // For std::function

bool IsGreaterThan(int a, int b){
    return a > b;
}

int main()
    {
    // 1. Create a lambda function that can be reused inside main()
    const auto sum = [](int a, int b) { return a + b;};

    int result = sum(4, 2); // result = 6

    // 2. Use std::function to use a function as a variable
    std::function<bool(int, int)> func = IsGreaterThan;

    bool test = func(2, 1); // test = true because 2 > 1
    }
*/