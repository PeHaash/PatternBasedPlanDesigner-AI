// Just Faster ;)
#include<iostream>
#include <string>
// #include<cstdlib>

#include "GeneticAlgorithm.cpp"

using namespace std;


float TT (vector<float>){
	return 0.5;
}

int main(){
	GeneticAlgorithm::POPULATION hello(
		/*popsize*/12,
		/*datasize*/22,
		/*elitesize*/1,
		/*ScoreFunc*/TT,
		/*MutationRate*/0.5,
		/*MutationMove*/0.5);
	hello.RunGeneration();
	cout <<"FUCK THIS SHIT :("<<endl;

}

/*
Disjointset
GeneticAlgorithm
main
NumericDataMaker
PatternCheck
PlanMaker
Room
SpeedTracker
Subspace
TextBasedGraphicExport

*/