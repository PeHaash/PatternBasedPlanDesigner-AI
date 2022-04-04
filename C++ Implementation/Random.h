#ifndef RANDOM_H
#define RANDOM_H

#include <cstdlib>
#include <ctime>
#include <vector>

namespace nRandom{
    float random();
    void SetRandomSeed(int seed);
    std::vector<std::vector<float>> Random2DVector(int X, int Y, int Seed);
    float uniform();
    int RandomBetween();
    // and some other shits!
}

float nRandom::random(){
    return (float) rand() / RAND_MAX;
}

void nRandom::SetRandomSeed(int seed=0){
    srand(time(NULL)+seed);
}

std::vector<std::vector<float>> nRandom::Random2DVector(int X, int Y, int Seed=0){                  //Gives X vectors, each with Y num
    std::vector<std::vector<float> > ret;
    SetRandomSeed(Seed);
    for(int i = 0; i < X; i++){
        std::vector<float> cell;
        for(int j = 0; j < Y; j++)
            cell.push_back(random());
        ret.push_back(cell);
    }
    return ret;
}

#endif

