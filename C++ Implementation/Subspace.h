#ifndef SUBSPACE_H
#define SUBSPACE_H

#include <vector>
#include <iostream>
#include <vector>
#include <algorithm>

#include "Global.h"

namespace nPlan {
	class Subspace;
}

class nPlan::Subspace {
private: // Room & Subspace is used in another func (SetSubspaceCodes)
	float Xposition, Yposition, Xweight, Yweight;
	int Room, SubspaceCode; float SubspaceCodeTemp;
	bool HasOpening, IsFenestrated, IsEntranceDoor;
	std::vector<int> Position;
public:
	Subspace(const std::vector<float> numericDiscrip);
	void Print();
	std::pair<int,float> SortElement();
	static bool SortByRoom(Subspace&, Subspace&);
	static bool SortByX(Subspace&, Subspace&);
	static bool SortByY(Subspace&, Subspace&);
	static void SetSubspaceCodes(std::vector<Subspace>&, int);

	friend class Plan;

};

#endif