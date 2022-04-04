#ifndef PLANMAKER_H
#define PLANMAKER_H

#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>


#include "Subspace.h"
#include "Global.h"
#include "DisjointSet.h"
#include "Features.h"
#include "TextBasedGraphicExport.h"
// #include <>
// sdf
// #include "Patterns.h"

namespace PlanMaker{
	class PLAN;
}

namespace Patterns{
	class PATTERNS;
}

class PlanMaker::PLAN{
private:
	std::vector<Subspace::SUBSPACE> Subspace;
	int SubspaceSize,RoomNumber;
	float Score;
	Features::FEATURES *Features;
	DisjointSet::DISJOINTSET SubspaceConnections;
	DisjointSet::DISJOINTSET RoomConnections;
	bool Dead;
	std::vector<int> ActiveRoomCodes;
	TextBasedGraphicExport::TBGE *GraphicExport;
public:
    PLAN(Features::FEATURES *feat, const std::vector<std::vector<float>> &nData,
    	                        TextBasedGraphicExport::TBGE *TBGEElement = NULL, int TBGEFrame=-1){
		SubspaceSize = nData.size();
		// vector<pair<float,Subspace::SUBSPACE>> SubspaceTemp;
		for(int i = 0; i < SubspaceSize; i++)
			Subspace.push_back(Subspace::SUBSPACE(nData[i]));
		// Add Subspace Codes:
		Subspace::SetSubspaceCodes(Subspace,SubspaceSize);
		// end
		RoomNumber = Global::RoomNumber;
		Score = 0;
		Features = feat;
		SubspaceConnections = DisjointSet::DISJOINTSET(SubspaceSize);
		RoomConnections = DisjointSet::DISJOINTSET(RoomNumber);
		Dead = false;
		for(int i = 0; i < RoomNumber; i++)
			if(feat->ActiveRooms[i]==1)
				ActiveRoomCodes.push_back(i);
		if (TBGEFrame != -1){
			GraphicExport = TBGEElement;
			GraphicExport->SetFrame(TBGEFrame);
		}
		// cout << Subspace[0].Xweight<< endl;

	}

	float SumOfWeightRange(int Begin, int End, bool IsX){
		if(IsX){
			float sum = 0;
			for(int i = Begin; i < End; i++) sum +=Subspace[i].Xweight;
			return sum;
		}else{
			float sum = 0;
			for(int i = Begin; i < End; i++) sum +=Subspace[i].Yweight;
			return sum;			
		}
	}

	void RecursiveSubspacePosition(int Begin, int End, bool HorizontalCut, int MinX, int MinY, int MaxX, int MaxY){
		if(End - Begin == 1){
			Subspace[Begin].Position={MinX,MinY,MaxX,MaxY};
			return;
		}
		int Mid = (Begin + End) / 2;
		if (HorizontalCut){
			sort(Subspace.begin() + Begin, Subspace.begin() + End,Subspace::SortByY);
			float RatioY = SumOfWeightRange(Begin, Mid, false) / SumOfWeightRange(Begin, End, false);
			int MiddleY = round(RatioY * float(MaxY - MinY) + MinY);
			RecursiveSubspacePosition(Begin, Mid, false, MinX, MinY,    MaxX, MiddleY);
			RecursiveSubspacePosition(Mid,   End, false, MinX, MiddleY,	MaxX, MaxY   );
		}else{
			sort(Subspace.begin() + Begin, Subspace.begin() + End, Subspace::SortByX);
			float RatioX = SumOfWeightRange(Begin, Mid, true ) / SumOfWeightRange(Begin, End, true );
			int MiddleX = round(RatioX * float(MaxX - MinX) + MinX);
			RecursiveSubspacePosition(Begin, Mid, true, MinX,    MinY, MiddleX, MaxY);
			RecursiveSubspacePosition(Mid,   End, true, MiddleX, MinY, MaxX,    MaxY);
		}
	}

	void SetSubspacePositions(){
		RecursiveSubspacePosition(
			0,                // begin pointer
			SubspaceSize,     // end pointer
			true,             // cut orientation: cut is horizontal ?
			// SubspaceSize,     // Size
			0,                // MinX
			0,                // MinY
			Features->Width,  // MaxX
			Features->Depth   // MaxY
			);
	}

	void MakeConnection(int Index1, int Index2, std::pair<int,int> Point1, std::pair<int,int> Point2){
		if(GraphicExport != NULL && false){
			float x0 = ((float) Subspace[Index1].Position[0] + Subspace[Index1].Position[2]) / 2;
			float y0 = ((float) Subspace[Index1].Position[1] + Subspace[Index1].Position[3]) / 2;
			float x1 = ((float) Subspace[Index2].Position[0] + Subspace[Index2].Position[2]) / 2;
			float y1 = ((float) Subspace[Index2].Position[1] + Subspace[Index2].Position[3]) / 2;
			GraphicExport->AddLine(x0, y0, x1, y1);
		}
		if (Subspace[Index1].Room == Subspace[Index2].Room){
			// They are in same room
			SubspaceConnections.Join(Index1, Index2);
		}else if (Subspace[Index1].HasOpening && Subspace[Index2].HasOpening){
			// We have a door here
			RoomConnections.Join(Subspace[Index1].Room, Subspace[Index2].Room);
			if (GraphicExport!=NULL){
				int com = GraphicExport->AddLine(Point1.first, Point1.second, Point2.first, Point2.second);
				GraphicExport->AddArgument(com, "Thickness", 20);
				GraphicExport->AddArgument(com, "Text", std::string("Door"));
				GraphicExport->AddArgument(com, "StrokeColorCode", 8);
				GraphicExport->AddArgument(com, "TextColorCode", 9);
			}
		}

	}

	// Plan.MergeSubspacesAndFindDoors();
	void MergeSubspacesAndFindDoors(){
		// using namespace std;
		std::set<int> sweepX,sweepY;
		std::map<int,std::vector<int>> minXs, minYs, maxXs, maxYs;  // map position to subspaceIndex
		for (Subspace::SUBSPACE ss:Subspace){
			sweepX.insert(ss.Position[0]);
			sweepX.insert(ss.Position[2]);
			sweepY.insert(ss.Position[1]);
			sweepY.insert(ss.Position[3]);
		}
		for (int i = 0; i < SubspaceSize; i++){
			minXs[Subspace[i].Position[0]].push_back(i);
			minYs[Subspace[i].Position[1]].push_back(i);
			maxXs[Subspace[i].Position[2]].push_back(i);
			maxYs[Subspace[i].Position[3]].push_back(i);
		}

		for(int swY: sweepY){
			for(int r1: minYs[swY]){
				int AminX = Subspace[r1].Position[0];
				int AmaxX = Subspace[r1].Position[2];
				for(int r2: maxYs[swY]){
					int BminX = Subspace[r2].Position[0];
					int BmaxX = Subspace[r2].Position[2];
					if (AminX < BmaxX && BminX < AmaxX){
						std::vector<int> xx{AminX, AmaxX, BminX, BmaxX};
						std::sort(xx.begin(),xx.end());
						// x1 = xx[1] , x2 = xx[2]
						MakeConnection(r1, r2, std::make_pair(xx[1], swY), std::make_pair(xx[2], swY));
						// cout << "Connect!" << r1 <<"  " <<r2 <<'\n';
					}
				}

			}
		}
		// std::cout <<endl;
		for(int swX: sweepX){
			for(int r1: minXs[swX]){
				int AminY = Subspace[r1].Position[1];
				int AmaxY = Subspace[r1].Position[3];
				for(int r2: maxXs[swX]){
					int BminY = Subspace[r2].Position[1];
					int BmaxY = Subspace[r2].Position[3];
					if (AminY < BmaxY && BminY < AmaxY){
						std::vector<int> yy{AminY, AmaxY, BminY, BmaxY};
						std::sort(yy.begin(),yy.end());
						MakeConnection(r1,r2, std::make_pair(swX, yy[1]), std::make_pair(swX, yy[1])); 
						// cout << "Connect!" << r1 <<"  " <<r2 <<'\n';
					}
				}
			}
		}



	}

	void ExportTBGE(){
		if (GraphicExport != NULL){
			int i = 0;
			for(Subspace::SUBSPACE o: Subspace){
				int com = GraphicExport->AddRectangle(o.Position);
				GraphicExport->AddArgument(com, "Thickness", 0);
				GraphicExport->AddArgument(com, "FillColorCode", o.Room * 17 + 30);
				GraphicExport->AddArgument(com, "StrokeColorCode", 1);
				GraphicExport->AddArgument(com, "Text", std::to_string(o.Room) + "--" + std::to_string(o.SubspaceCode));
				i++;
			}
		}
	}

	friend class Patterns::PATTERNS;


};





#endif