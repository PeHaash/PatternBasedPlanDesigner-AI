#ifndef FEATURES_H
#define FEATURES_H

#include<vector>
#include<iostream>

namespace Features {
class FEATURES {
public:
	int Width, Depth;
	float TrueNorth;
	float EntrancePosition;
	std::vector<int> ActiveRooms;
	FEATURES(int width, int depth, std::vector<int> activerooms, float truenorth, float entranceposition)
	{
		Width = width;
		Depth = depth;
		ActiveRooms = activerooms;
		TrueNorth = truenorth;
		EntrancePosition = entranceposition;
		// for(unsigned int i = 0; i < ActiveRooms.size(); i++)
		// 	std::cout <<" "<<ActiveRooms[i]<<" ";
	}
};
}


#endif