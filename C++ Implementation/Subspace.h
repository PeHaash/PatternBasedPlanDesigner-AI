#ifndef SUBSPACE_H
#define SUBSPACE_H

#include <vector>

#include "Global.h"
// #include "Features.h"

using namespace std;

namespace Subspace {
class SUBSPACE;
}

class Subspace::SUBSPACE {
private:
	float Xposition, Yposition, Xweight, Yweight;
	int Room, SubspaceCode; float SubspaceCodeTemp;
	bool HasOpening, IsFenestrated, IsEntranceDoor;
	std::vector<float> Position;
public:
	SUBSPACE(const vector<float> numericDiscrip)
	{
		Xposition = numericDiscrip[0];
		Yposition = numericDiscrip[1];
		Xweight = numericDiscrip[2];
		Yweight = numericDiscrip[3];
		Room = int(numericDiscrip[4] * Global::RoomNumber);
		SubspaceCodeTemp = numericDiscrip [5];
		HasOpening = numericDiscrip[6] > 0.5 ? true : false;
		IsFenestrated = numericDiscrip[7] > 0.5 ? true : false;
		IsEntranceDoor = false;
	}
};


#endif