#ifndef RANDOM_H
#define RANDOM_H

#include <cstdlib>
#include <ctime>


namespace Random{
	float random(){
		return (float) rand() / RAND_MAX;
	}
	void SetRandomSeed(int seed=0){
		srand(time(NULL)+seed);
	}
	float uniform();
	int RandomBetween();
	// and some other shits!
}

#endif

