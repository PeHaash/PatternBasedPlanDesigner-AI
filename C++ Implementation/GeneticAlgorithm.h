#ifndef GENETIC_ALGORITHM_H
#define GENETIC_ALGORITHM_H

#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>

#include "Random.h"

namespace nGeneticAlgorithm{
	struct Species;
	class Population;
}

struct nGeneticAlgorithm::Species{
	std::vector<float> Data;
	float Score;
	Species(const std::vector<float>& data){
		Data=data;
		Score = 0;
	}
};

class nGeneticAlgorithm::Population{
	private:
		int PopulationSize, DataSize, EliteSize;
		std::function<float(std::vector<float>)> ScoreFunction;
		float MutationRate, MutationMove;
		std::vector<Species> mSpecies;
	public:
		Population(int, int, int, std::function<float(std::vector<float>)>, float, float);
		Species Mutate(Species s);
		void RunGeneration();
		float GetBestScore();
		void PrintBestData();
};

#endif
