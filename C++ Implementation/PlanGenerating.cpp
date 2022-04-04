// #include <iostream>

#include "Debug.h"
#include "Global.h"
#include "Features.h"
#include "PlanMaker.h"
#include "NumericDataMaker.h"
#include "TextBasedGraphicExport.h"
#include "Patterns.h"

int main(){
	// cout <<"E!"<<endl;
	Features::FEATURES feature(1500, 1800, {1,1,1,1}, 23, 0.5);
	TextBasedGraphicExport::TBGE tbge("1 C++ Implementation", "gooz");
	Patterns::PATTERNS PatternCheck;
	//------
	auto data = NumericDataMaker::RandomNumericData(16);
	PlanMaker::PLAN Plan(&feature, data, &tbge, 0);
	Plan.SetSubspacePositions();
	std::cout << PatternCheck.PGSubspaceMaxMin(Plan)<<std::endl;
	Plan.MergeSubspacesAndFindDoors();

	// Plan.SetFenestrations();
	// Plan.SetEntranceDoor();
	Plan.ExportTBGE();
	tbge.End();
	return 0;
}
