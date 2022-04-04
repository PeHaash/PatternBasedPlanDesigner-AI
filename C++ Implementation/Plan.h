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
#include "TBGE.h"

namespace nPlan{
    class Plan;
}




class nPlan::Plan{
private:
    std::vector<Subspace> SubspaceVector;
    int SubspaceSize,RoomNumber;
    float Score;
    nFeatures::Features *Features;
    nDisjointSet::DisjointSet SubspaceConnections;
    nDisjointSet::DisjointSet RoomConnections;
    bool Dead;
    std::vector<int> ActiveRoomCodes;
    nTBGE::TBGE *GraphicExport;
    int gooz;
public:
    Plan(nFeatures::Features *feat, const std::vector<std::vector<float>> &nData, nTBGE::TBGE *TBGEElement, int TBGEFrame);
    float SumOfWeightRange(int Begin, int End, bool IsX);
    void RecursiveSubspacePosition(int Begin, int End, bool HorizontalCut, int MinX, int MinY, int MaxX, int MaxY);
    void SetSubspacePositions();
    void MakeConnection(int Index1, int Index2, std::pair<int,int> Point1, std::pair<int,int> Point2);
    void MergeSubspacesAndFindDoors();
    void ExportTBGE();

    void Judger();
    class Builder;
    class Judge;
    class Mason;

};


class nPlan::Plan::Builder{

};

class nPlan::Plan::Mason{};


class  nPlan::Plan::Judge{
    public:
    Judge(int x){std::cout <<"sdfsdfsd"<<x<<std::endl;}

    static void salam(){
        std::cout << -5;
    }

    static void jj(Plan* p){
        std::cout <<"------"<<p->SubspaceSize<<std::endl;
    }
    // B-J-M Plan Migiran, &refrence, ye karish mikonan, baresh migardoonan. hamin!
};


////////////////////////////////////////////////////////////////////////////////////////////////////


void nPlan::Plan::Judger(){
        // Judge sda(4);
        Judge::jj(this);
}

nPlan::Plan::Plan(nFeatures::Features *feat, const std::vector<std::vector<float>> &nData,
                            nTBGE::TBGE *TBGEElement = NULL, int TBGEFrame=-1){
    SubspaceSize = nData.size();
    gooz = 5;
    // vector<pair<float,Subspace::SUBSPACE>> SubspaceTemp;
    for(int i = 0; i < SubspaceSize; i++)
        SubspaceVector.push_back(Subspace(nData[i]));
    // Add Subspace Codes:
    Subspace::SetSubspaceCodes(SubspaceVector, SubspaceSize);
    RoomNumber = nGlobal::ROOM_NUMBER;
    Score = 0;
    Features = feat;
    SubspaceConnections = nDisjointSet::DisjointSet(SubspaceSize);
    RoomConnections = nDisjointSet::DisjointSet(RoomNumber);
    Dead = false;
    for(int i = 0; i < RoomNumber; i++)
        if(feat->ActiveRooms[i]==1)
            ActiveRoomCodes.push_back(i);
    if (TBGEFrame != -1){
        GraphicExport = TBGEElement;
        GraphicExport->SetFrame(TBGEFrame);
    }
}

float nPlan::Plan::SumOfWeightRange(int Begin, int End, bool IsX){
    if(IsX){
        float sum = 0;
        for(int i = Begin; i < End; i++) sum +=SubspaceVector[i].Xweight;
        return sum;
    }else{
        float sum = 0;
        for(int i = Begin; i < End; i++) sum +=SubspaceVector[i].Yweight;
        return sum;         
    }
}

void nPlan::Plan::RecursiveSubspacePosition(int Begin, int End, bool HorizontalCut, int MinX, int MinY, int MaxX, int MaxY){
    if(End - Begin == 1){
        SubspaceVector[Begin].Position={MinX,MinY,MaxX,MaxY};
        return;
    }
    int Mid = (Begin + End) / 2;
    if (HorizontalCut){
        sort(SubspaceVector.begin() + Begin, SubspaceVector.begin() + End,Subspace::SortByY);
        float RatioY = SumOfWeightRange(Begin, Mid, false) / SumOfWeightRange(Begin, End, false);
        int MiddleY = round(RatioY * float(MaxY - MinY) + MinY);
        RecursiveSubspacePosition(Begin, Mid, false, MinX, MinY,    MaxX, MiddleY);
        RecursiveSubspacePosition(Mid,   End, false, MinX, MiddleY, MaxX, MaxY   );
    }else{
        sort(SubspaceVector.begin() + Begin, SubspaceVector.begin() + End, Subspace::SortByX);
        float RatioX = SumOfWeightRange(Begin, Mid, true ) / SumOfWeightRange(Begin, End, true );
        int MiddleX = round(RatioX * float(MaxX - MinX) + MinX);
        RecursiveSubspacePosition(Begin, Mid, true, MinX,    MinY, MiddleX, MaxY);
        RecursiveSubspacePosition(Mid,   End, true, MiddleX, MinY, MaxX,    MaxY);
    }
}

void nPlan::Plan::SetSubspacePositions(){
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

void nPlan::Plan::MakeConnection(int Index1, int Index2, std::pair<int,int> Point1, std::pair<int,int> Point2){
    if(GraphicExport != NULL && false){
        float x0 = ((float) SubspaceVector[Index1].Position[0] + SubspaceVector[Index1].Position[2]) / 2;
        float y0 = ((float) SubspaceVector[Index1].Position[1] + SubspaceVector[Index1].Position[3]) / 2;
        float x1 = ((float) SubspaceVector[Index2].Position[0] + SubspaceVector[Index2].Position[2]) / 2;
        float y1 = ((float) SubspaceVector[Index2].Position[1] + SubspaceVector[Index2].Position[3]) / 2;
        GraphicExport->AddLine(x0, y0, x1, y1);
    }
    if (SubspaceVector[Index1].Room == SubspaceVector[Index2].Room){
        // They are in same room
        SubspaceConnections.Join(Index1, Index2);
    }else if (SubspaceVector[Index1].HasOpening && SubspaceVector[Index2].HasOpening){
        // We have a door here
        RoomConnections.Join(SubspaceVector[Index1].Room, SubspaceVector[Index2].Room);
        if (GraphicExport!=NULL){
            int com = GraphicExport->AddLine(Point1.first, Point1.second, Point2.first, Point2.second);
            GraphicExport->AddArgument(com, "Thickness", 20);
            GraphicExport->AddArgument(com, "Text", std::string("Door"));
            GraphicExport->AddArgument(com, "StrokeColorCode", 8);
            GraphicExport->AddArgument(com, "TextColorCode", 9);
        }
    }

}

void nPlan::Plan::MergeSubspacesAndFindDoors(){
    // using namespace std;
    std::set<int> sweepX,sweepY;
    std::map<int,std::vector<int>> minXs, minYs, maxXs, maxYs;  // map position to subspaceIndex
    for (Subspace ss: SubspaceVector){
        sweepX.insert(ss.Position[0]);
        sweepX.insert(ss.Position[2]);
        sweepY.insert(ss.Position[1]);
        sweepY.insert(ss.Position[3]);
    }
    for (int i = 0; i < SubspaceSize; i++){
        minXs[SubspaceVector[i].Position[0]].push_back(i);
        minYs[SubspaceVector[i].Position[1]].push_back(i);
        maxXs[SubspaceVector[i].Position[2]].push_back(i);
        maxYs[SubspaceVector[i].Position[3]].push_back(i);
    }

    for(int swY: sweepY){
        for(int r1: minYs[swY]){
            int AminX = SubspaceVector[r1].Position[0];
            int AmaxX = SubspaceVector[r1].Position[2];
            for(int r2: maxYs[swY]){
                int BminX = SubspaceVector[r2].Position[0];
                int BmaxX = SubspaceVector[r2].Position[2];
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
            int AminY = SubspaceVector[r1].Position[1];
            int AmaxY = SubspaceVector[r1].Position[3];
            for(int r2: maxXs[swX]){
                int BminY = SubspaceVector[r2].Position[1];
                int BmaxY = SubspaceVector[r2].Position[3];
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

void nPlan::Plan::ExportTBGE(){
    if (GraphicExport != NULL){
        // int i = 0;
        for(Subspace o: SubspaceVector){
            int com = GraphicExport->AddRectangle(o.Position);
            GraphicExport->AddArgument(com, "Thickness", 0);
            GraphicExport->AddArgument(com, "FillColorCode", o.Room * 17 + 30);
            GraphicExport->AddArgument(com, "StrokeColorCode", 1);
            GraphicExport->AddArgument(com, "Text", std::to_string(o.Room) + "--" + std::to_string(o.SubspaceCode));
            // i++;
        }
    }
}

#endif