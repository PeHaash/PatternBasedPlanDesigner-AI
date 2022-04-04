#ifndef FEATURES_H
#define FEATURES_H

#include<vector>

namespace Features {
class FEATURES {
public:
	int Width, Depth;
	float TrueNorth;
	float EntrancePosition;
	std::vector<bool> ActiveRooms;
	FEATURES(int width, int depth, std::vector<bool> activerooms, float truenorth, float entranceposition)
	{
		Width = width;
		Depth = depth;
		ActiveRooms = activerooms;
		TrueNorth = truenorth;
		EntrancePosition = entranceposition;
	}
};
}


#endif