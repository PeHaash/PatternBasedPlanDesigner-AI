#ifndef PATTERNS_H
#define PATTERNS_H

#include <vector>
#include <algorithm>
#include <iostream>

#include "Global.h"
#include "PlanMaker.h"

namespace Patterns{
	class PATTERNS;
}

class Patterns::PATTERNS{
public:
	PATTERNS() = default;
	float PGSubspaceMaxMin(const PlanMaker::PLAN& Plan){
		int minSS = Global::MinSubspace;
		int maxSS = Global::MaxSubspace;
		int error = 0;
		std::vector<int> numofss(Global::RoomNumber, 0);
		for(Subspace::SUBSPACE ss: Plan.Subspace) numofss[ss.Room]++;
		for(int i = 0; i < Global::RoomNumber; i++){
			error += std::max(0, numofss[i] - maxSS) + std::max(0, minSS - numofss[i]);
			    // + (Plan.Features->ActiveRooms[i] == 0)?numofss[i]:0;
		}
		for(int ss: numofss) std::cout<<ss<<" ";
		return 1.0 - ((float)error / Plan.SubspaceSize);
	}
	

};

// i love sarvenaz <3








#endif