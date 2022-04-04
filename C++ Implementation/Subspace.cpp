#include "Subspace.h"

nPlan::Subspace::Subspace(const std::vector<float> numericDiscrip){
	Xposition = numericDiscrip[0];
	Yposition = numericDiscrip[1];
	Xweight = numericDiscrip[2];
	Yweight = numericDiscrip[3];
	Room = int(numericDiscrip[4] * nGlobal::ROOM_NUMBER);
	SubspaceCodeTemp = numericDiscrip [5];
	HasOpening = numericDiscrip[6] > 0.5 ? true : false;
	IsFenestrated = numericDiscrip[7] > 0.5 ? true : false;
	IsEntranceDoor = false;
}

void nPlan::Subspace::Print(){
	std::cout << "Xpos: " << Xposition << '-';
	std::cout << "Ypos: " << Yposition << '-';
	std::cout << "Room: " << Room << ": " << SubspaceCodeTemp <<'\t' <<SubspaceCode <<std::endl; 
}

std::pair<int,float> nPlan::Subspace::SortElement(){
	return std::make_pair(Room,SubspaceCodeTemp);
}


bool nPlan::Subspace::SortByRoom(Subspace &i, Subspace &j){
	return i.SortElement() < j.SortElement();
}

bool nPlan::Subspace::SortByX(Subspace &i, Subspace &j){
	return i.Xposition < j.Xposition;
}

bool nPlan::Subspace::SortByY(Subspace &i, Subspace &j){
	return i.Xposition < j.Xposition;
}

void nPlan::Subspace::SetSubspaceCodes(std::vector<Subspace>& subspace, int size){
	sort(subspace.begin(),subspace.end(),SortByRoom);
	subspace[0].SubspaceCode = 0;
	for(int i = 1; i < size; i++){
		subspace[i].SubspaceCode = (subspace[i].Room != subspace[i-1].Room)? 0 : subspace[i-1].SubspaceCode + 1;
	}
}
