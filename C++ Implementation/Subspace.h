#ifndef SUBSPACE_H
#define SUBSPACE_H

#include <vector>
#include <iostream>
#include <vector>
#include <algorithm>

#include "Global.h"
// #include "Features.h"


namespace Subspace {
	struct SUBSPACE;
	bool SortByRoom(SUBSPACE&, SUBSPACE&);
	bool SortByX(SUBSPACE&, SUBSPACE&);
	bool SortByY(SUBSPACE&, SUBSPACE&);
	void SetSubspaceCodes(std::vector<SUBSPACE>&, int);
}

struct Subspace::SUBSPACE {
// public: // Room & Subspace is used in another func (SetSubspaceCodes)
	float Xposition, Yposition, Xweight, Yweight;
	int Room, SubspaceCode; float SubspaceCodeTemp;
	bool HasOpening, IsFenestrated, IsEntranceDoor;
	std::vector<int> Position;
// public:
	SUBSPACE(const std::vector<float> numericDiscrip){
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
	void Print(){
		std::cout << "Xpos: " << Xposition << '-';
		std::cout << "Ypos: " << Yposition << '-';
		std::cout << "Room: " << Room << ": " << SubspaceCodeTemp <<'\t' <<SubspaceCode <<std::endl; 
	}
	std::pair<int,float> SortElement(){
		return std::make_pair(Room,SubspaceCodeTemp);
	}
	// void SetPosition(vector<int> pos){
	// 	Position = pos;
	// }



	// friend void SetSubspaceCodes(vector<SUBSPACE>&, int);
	// friend class PlanMaker::PLAN;
};

bool Subspace::SortByRoom(SUBSPACE &i, SUBSPACE &j){
	return i.SortElement() < j.SortElement();
}

bool Subspace::SortByX(SUBSPACE &i, SUBSPACE &j){
	return i.Xposition < j.Xposition;
}

bool Subspace::SortByY(SUBSPACE &i, SUBSPACE &j){
	return i.Xposition < j.Xposition;
}


void Subspace::SetSubspaceCodes(std::vector<SUBSPACE>& subspace, int size){
	sort(subspace.begin(),subspace.end(),SortByRoom);
	subspace[0].SubspaceCode = 0;
	for(int i = 1; i < size; i++){
		subspace[i].SubspaceCode = (subspace[i].Room != subspace[i-1].Room)? 0 : subspace[i-1].SubspaceCode + 1;
	}

}

#endif