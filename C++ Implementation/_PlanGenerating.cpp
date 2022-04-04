// #include <iostream>

#include "Debug.h"
// #include "Global.h"
#include "Features.h"
#include "Plan.h"
#include "Random.h"
#include "TBGE.h"
// #include "Patterns.h"

int main(){
	// cout <<"E!"<<endl;
	nFeatures::Features feature(1500, 1800, {1,1,1,1}, 23, 0.5);
	nTBGE::TBGE tbge("1 C++ Implementation", "gooz");
	// Patterns::PATTERNS PatternCheck;
	//------
	auto data = nRandom::Random2DVector(16,8);
	nPlan::Plan plan(&feature, data, &tbge, 0); //  nPlan::Plan plan(&features, &tbge, 0);
												//	nPlan::Plan::Builder SetSubspaceVectorOn(plan);
												//	nPlan::Plan::Judge CheckPatternOn(plan, "PGmM");
												//	if (plan.IsDead()) continue;
												//  nPlan::Plan::Builder SetSubspacePositionsOn();
												//	nPlan::Plan::Builder SolveAdjencaciesOn(plan);
												//	nPlan::Plan::Judge CheckConnectivityPatternsOn(Plan);
												//	nPlan::Plan::Builder SetFenestrationsOn(plan);
												// 	nPlan::Plan::Builder SetEntranceDoorOn(plan);
												//	plan.ExportTBGE();
	plan.SetSubspacePositions();
	// std::cout << PatternCheck.PGSubspaceMaxMin(Plan)<<std::endl;
	plan.MergeSubspacesAndFindDoors();
	// nPlan::Plan::Judge dfk(65);
	// plan.Judger();
	// nPlan::Plan::Judge::salam();
	// ----nPlan::Plan::Builder::SetSomethingOn(Plan);
	// Plan.SetFenestrations();
	// Plan.SetEntranceDoor();
	plan.ExportTBGE();
	tbge.End();
	return 0;
}
