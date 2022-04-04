#ifndef FEATURES_H
#define FEATURES_H

#include<vector>
#include<iostream>

namespace nFeatures {
	class Features;
}

class nFeatures::Features {
public:
	int Width, Depth;
	float TrueNorth;
	float EntrancePosition;
	std::vector<int> ActiveRooms;
	Features(int width, int depth, std::vector<int> activerooms, float truenorth, float entranceposition) {
		Width = width;
		Depth = depth;
		ActiveRooms = activerooms;
		TrueNorth = truenorth;
		EntrancePosition = entranceposition;
	}
};

#endif