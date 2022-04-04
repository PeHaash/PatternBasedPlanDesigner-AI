#include "GeneticAlgorithm.h"

nGeneticAlgorithm::Population::Population(int popsize, int datasize, int elitesize,
					std::function<float(std::vector<float>)> scorefunc, float mrate, float mmove){
	PopulationSize = popsize;
	DataSize = datasize;
	EliteSize = elitesize;
	ScoreFunction = scorefunc;
	MutationRate = mrate;
	MutationMove = mmove;
	// srand(time(NULL));
	nRandom::SetRandomSeed();
	for (int i = 0; i < PopulationSize; i++){
		std::vector<float> randomdata;
		for (int j=0; j < DataSize; j++){
			randomdata.push_back(nRandom::random());
			// cout << (float)rand()/RAND_MAX <<endl;
		}
		mSpecies.push_back(Species(randomdata));
	}
}

nGeneticAlgorithm::Species nGeneticAlgorithm::Population::Mutate(Species s){
	for(int i = 0; i < DataSize; i++)
		if (nRandom::random() < MutationRate)
			s.Data[i]=nRandom::random(); //*MutationMove
	return s;
}

void nGeneticAlgorithm::Population::RunGeneration(){
	// Scoring
	for (int i = 0; i < PopulationSize; i++)
		mSpecies[i].Score=ScoreFunction(mSpecies[i].Data);
	// Sort By Score
	std::sort(mSpecies.begin(),mSpecies.end(),[](Species a, Species b) { return a.Score > b.Score;});
	// Kill Excess & Mutate
	std::vector<Species> NewSpecies;
	NewSpecies.push_back(mSpecies[0]);
	for(int i = 1; i < PopulationSize; i++){
		int p = rand() % EliteSize;
		NewSpecies.push_back(Mutate(mSpecies[p]));
	}
	mSpecies = NewSpecies;
}

float nGeneticAlgorithm::Population::GetBestScore(){
	return mSpecies[0].Score;
}

void nGeneticAlgorithm::Population::PrintBestData(){
	for(int i = 0; i < DataSize; i++)
		std::cout << mSpecies[0].Data[i] << "-";
	std::cout << std::endl;
}

