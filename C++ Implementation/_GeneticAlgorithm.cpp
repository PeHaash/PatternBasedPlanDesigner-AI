// Just Faster ;)
#include<iostream>
#include <cmath>
#include <ctime>

#include "GeneticAlgorithm.h"

float colville (std::vector<float> x)
{
	float x1 = (x[0] - 0.5) * 10;
	float x2 = (x[1] - 0.5) * 10;
	float x3 = (x[2] - 0.5) * 10;
	float x4 = (x[3] - 0.5) * 10;

	float term1 = 100 * pow((pow(x1, 2) - x2), 2);
	float term2 = pow(x1 - 1, 2);
	float term3 = pow(x3 - 1, 2);
	float term4 = 90 * pow(pow(x3, 2) - x4, 2);
	float term5 = 10.1 * (pow(x2 - 1, 2) + pow(x4 - 1, 2));
	float term6 = 19.8 * (x2 - 1) * (x4 - 1);
	return -(term1 + term2 + term3 + term4 + term5 + term6);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	int st = clock();
	nGeneticAlgorithm::Population hello(/*popsize*/100, /*datasize*/4, /*elitesize*/10,
	        /*ScoreFunc*/colville, /*MutationRate*/0.7, /*MutationMove*/0.5);
	for (int i = 0; i < 2500; i++) {
		hello.RunGeneration();
		std::cout <<hello.GetBestScore()<<'\n';
	}
	hello.PrintBestData();
	int en = clock();
	std::cout << "end of code;) ticks:" << (en - st) << " time:" << ((float)en - st) / CLOCKS_PER_SEC << std::endl;
}
