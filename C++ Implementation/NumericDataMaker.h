#ifndef NUMERICDATAMAKER_H
#define NUMERICDATAMAKER_H

#include <vector>

#include "Random.h"


namespace NumericDataMaker{
	std::vector<std::vector<float> > RandomNumericData(int NumberOfSubspaces, int Seed=0){
		std::vector<std::vector<float> > ret;
		Random::SetRandomSeed(Seed);
		for(int i = 0; i < NumberOfSubspaces; i++){
			std::vector<float> cell;
			for(unsigned int j = 0; j < 8; j++)
				cell.push_back(Random::random());
			ret.push_back(cell);
		}
		return ret;
	}
}

#endif