#include <iostream>
#include <vector>
#include <string>
// #include <cstdlib>
// #include <ctime>
#include <functional>
#include <algorithm>

#include "Random.h"

using namespace std;


namespace GeneticAlgorithm{
	class SPECIES;
	class POPULATION;
}

class GeneticAlgorithm::SPECIES{
	public:
		vector<float> Data;
		float Score;
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
		POPULATION(int popsize, int datasize, int elitesize, function<float(vector<float>)> scorefunc, float mrate, float mmove){
			PopulationSize = popsize;
			DataSize = datasize;
			EliteSize = elitesize;
			ScoreFunction = scorefunc;
			MutationRate = mrate;
			MutationMove = mmove;
			// srand(time(NULL));
			Random::SetRandomSeed();
			for (int i = 0; i < PopulationSize; i++){
				vector<float> randomdata;
				for (int j=0; j < DataSize; j++){
					randomdata.push_back(Random::random());
					// cout << (float)rand()/RAND_MAX <<endl;
				}
				Species.push_back(SPECIES(randomdata));
			}
		}

		SPECIES Mutate(SPECIES s){
			for(int i = 0; i < DataSize; i++)
				if (Random::random() < MutationRate)
					s.Data[i]=Random::random(); //*MutationMove
			return s;
		}

		void RunGeneration(){
			// Scoring
			for (int i = 0; i < PopulationSize; i++)
				Species[i].Score=ScoreFunction(Species[i].Data);
			// Sort By Score
			sort(Species.begin(),Species.end(),[](SPECIES a, SPECIES b) { return a.Score > b.Score;});
			// Kill Excess & Mutate
			vector<SPECIES> NewSpecies;
			NewSpecies.push_back(Species[0]);
			for(int i = 1; i < PopulationSize; i++){
				int p = rand() % EliteSize;
				NewSpecies.push_back(Mutate(Species[p]));
			}
			Species = NewSpecies;
		}

		float BestScore(){
			return Species[0].Score;
		}

		void PrintBestData(){
			for(int i = 0; i < DataSize; i++)
				cout << Species[0].Data[i] << "-";
			cout << endl;
		}
};

