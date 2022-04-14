#ifndef PLANMAKER_H
#define PLANMAKER_H

#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <string>

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
    int SubspaceSize, RoomNumber;
    float Score;
    nFeatures::Features *Features;
    nDisjointSet::DisjointSet SubspaceConnections;
    nDisjointSet::DisjointSet RoomConnections;
    bool Dead;
    std::vector<int> ActiveRoomCodes;
    nTBGE::TBGE *GraphicExport;
public:
    Plan(nFeatures::Features *feat, const std::vector<std::vector<float>> &nData, nTBGE::TBGE *TBGEElement, int TBGEFrame);
    Plan(nFeatures::Features *feat, nTBGE::TBGE *TBGEElement, int TBGEFrame);
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

    static void PGOpenings(Plan &plan){
        // Check Openings By PatternCodeOfOpenings
    }

    static void PGDoorSize(Plan &plan){
        // "Doors shall be at least 80cm" later: we could 80<df<120
    }

    static void PGNoThinSpace(Plan &plan){
        // Rooms should not be narrower than a 100cm threshold because they will ending up unusable
    }

    static void PGAllConnected(Plan &plan){
        // All rooms Shall be Connected and have paths between them
    }

    static void PGEntranceLocation(Plan &plan){
        // Entrance Should Not be located in Bedroom, WC or Bathroom
    }

    static void PROneDoor(Plan &plan){
        // "WC/Bath only have one door" , if WC has two doors, one of them must be to bathroom.
    }

    static void EvaluatePlanByPattern(Plan &plan, std::string code){

    }

    // B-J-M Plan Migiran, &refrence, ye karish mikonan, baresh migardoonan. hamin!
};

#endif