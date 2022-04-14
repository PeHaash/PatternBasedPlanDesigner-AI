#ifndef FEATURES_H
#define FEATURES_H

#include<vector>
#include<iostream>

#include "global.h"

namespace nFeatures {
	class Features;
}

class nFeatures::Features {
public:
	int Width, Depth;
	float TrueNorth;
	float EntrancePosition;
	std::vector<int> ActiveRooms;
	std::vector<enum RoomCode> RoomCodes;
	Features(int width, int depth, std::vector<int> activerooms,std::vector<enum RoomCode> roomcodes , 
																						float truenorth, float entranceposition) {
		Width = width;
		Depth = depth;
		ActiveRooms = activerooms;
		TrueNorth = truenorth;
		EntrancePosition = entranceposition;
		RoomCodes = roomcodes;
	}
};

#endif