# hello
# 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode, 6: Has Door?, 7: Has Fenestration?

from importlib import reload
import TextBasedGraphicExport
import Subspace
import Room
import DisjointSet
import PatternCheck


def ReloadAllImports():
    reload(TextBasedGraphicExport)
    reload(Subspace)
    reload(Room)
    reload(DisjointSet)
    reload(PatternCheck)


def Center(pos):
    return ((pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2)


class PLAN:
    def __init__(self, HyperParameters, Features, NumericData, TBGEElement, TBGEFrame):
        SubspaceTemp = [Subspace.SUBSPACE(HyperParameters, numericDiscrip) for numericDiscrip in NumericData]
        self.SubspaceSize = len(SubspaceTemp)
        # Add Subspace Codes:
        SubspaceTemp.sort(key=lambda x: (x.Room, x.SubspcaceCode))
        for i in range(self.SubspaceSize):
            SubspaceTemp[i].SubspcaceCode =\
                SubspaceTemp[i - 1].SubspcaceCode + 1 if SubspaceTemp[i].Room == SubspaceTemp[i - 1].Room else 0
        self.Subspace = SubspaceTemp
        self.Room = [
            Room.ROOM(
                NumberOfSubspaces=sum(1 if subspace.Room == i else 0 for subspace in self.Subspace),
                RoomCode=i
            ) if IsAcitveRoom == 1 else None
            for i, IsAcitveRoom in enumerate(Features.ActiveRooms)]  # Maybe Unnecesary
        self.Score = 0
        self.Features = Features
        self.HyperParameters = HyperParameters
        self.SubspaceConnections = DisjointSet.DISJOINSET(self.SubspaceSize)  # To Find Connections and Openings whitin a room
        self.RoomConnections = DisjointSet.DISJOINSET(HyperParameters.RoomNumber)  # To Find Connections and Openings Between Spaces
        self.Dead = False
        self.ActiveRoomCodes = [i for i in range(HyperParameters.RoomNumber) if Features.ActiveRooms[i] == 1]
        self.GraphicExport = None
        if TBGEElement is not None:
            self.GraphicExport = TBGEElement
            self.GraphicExport.SetFrame(TBGEFrame)

    def RecursiveSubspacePosition(Subspace, CutOrientation, Size, minX, minY, maxX, maxY):
        if Size == 1:
            Subspace[0].Position = [minX, minY, maxX, maxY]
            return Subspace
        SizeDivide2 = int(Size / 2)
        if CutOrientation == "H":
            Subspace.sort(key=lambda x: x.Yposition)
            ratioY = sum(ss.Yweight for ss in Subspace[:SizeDivide2]) / sum(ss.Yweight for ss in Subspace)
            middleY = round(ratioY * (maxY - minY) + minY)
            array1 = PLAN.RecursiveSubspacePosition(
                Subspace=Subspace[:SizeDivide2],
                CutOrientation="V",
                Size=Size / 2,
                minX=minX,
                minY=minY,
                maxX=maxX,
                maxY=middleY
            )
            array2 = PLAN.RecursiveSubspacePosition(
                Subspace=Subspace[SizeDivide2:],
                CutOrientation="V",
                Size=Size / 2,
                minX=minX,
                minY=middleY,
                maxX=maxX,
                maxY=maxY
            )
        if CutOrientation == "V":
            Subspace.sort(key=lambda x: x.Xposition)
            ratioX = sum(ss.Xweight for ss in Subspace[:SizeDivide2]) / sum(ss.Xweight for ss in Subspace)
            middleX = round(ratioX * (maxX - minX) + minX)
            array1 = PLAN.RecursiveSubspacePosition(
                Subspace=Subspace[:SizeDivide2],
                CutOrientation="H",
                Size=Size / 2,
                minX=minX,
                minY=minY,
                maxX=middleX,
                maxY=maxY
            )
            array2 = PLAN.RecursiveSubspacePosition(
                Subspace=Subspace[SizeDivide2:],
                CutOrientation="H",
                Size=Size / 2,
                minX=middleX,
                minY=minY,
                maxX=maxX,
                maxY=maxY
            )
        return array1 + array2

    def SetSubspacePositions(self):
        PLAN.RecursiveSubspacePosition(
            Subspace=self.Subspace,
            CutOrientation="H",
            Size=self.SubspaceSize,
            minX=0,
            minY=0,
            maxX=self.Features.Width,
            maxY=self.Features.Depth
        )

    def MakeConnection(self, Index1, Index2, Point1, Point2):
        if self.Subspace[Index1].Room == self.Subspace[Index2].Room:
            # They are in same room
            self.SubspaceConnections.Join(Index1, Index2)
        elif self.Subspace[Index1].HasOpening is True and self.Subspace[Index2].HasOpening is True:
            # We have a door here
            self.RoomConnections.Join(self.Subspace[Index1].Room, self.Subspace[Index2].Room)
            # print("Door Between:", self.Subspace[Index1].Room, "  ", self.Subspace[Index2].Room)
            if self.GraphicExport is not None:
                self.GraphicExport.AddLine(Point1, Point2, Thickness=20, Text="Door", StrokeColorCode=8, TextColorCode=8)
            pass
        else:
            # Just Simple Wall
            pass

    def MergeSubspacesAndFindDoors(self):
        # FIND CONNECTIONS:
        sweepX = set(ss.Position[0] for ss in self.Subspace) | set(ss.Position[2] for ss in self.Subspace)
        sweepY = set(ss.Position[1] for ss in self.Subspace) | set(ss.Position[3] for ss in self.Subspace)
        minXs = {xx: [] for xx in sweepX}
        minYs = {yy: [] for yy in sweepY}
        maxXs = {xx: [] for xx in sweepX}
        maxYs = {yy: [] for yy in sweepY}

        for i, ss in enumerate(self.Subspace):
            minXs[ss.Position[0]].append(i)
            minYs[ss.Position[1]].append(i)
            maxXs[ss.Position[2]].append(i)
            maxYs[ss.Position[3]].append(i)

        for swY in sweepY:
            for r1 in minYs[swY]:
                AminX, AminY, AmaxX, AmaxY = self.Subspace[r1].Position
                for r2 in maxYs[swY]:
                    BminX, BminY, BmaxX, BmaxY = self.Subspace[r2].Position
                    if AminX < BmaxX and BminX < AmaxX:
                        # y=swY
                        aa, x1, x2, bb = sorted([AminX, AmaxX, BminX, BmaxX])
                        self.MakeConnection(r1, r2, (x1, swY), (x2, swY))

        for swX in sweepX:
            for r1 in minXs[swX]:
                AminX, AminY, AmaxX, AmaxY = self.Subspace[r1].Position
                for r2 in maxXs[swX]:
                    BminX, BminY, BmaxX, BmaxY = self.Subspace[r2].Position
                    if AminY < BmaxY and BminY < AmaxY:
                        # x=swX
                        aa, y1, y2, bb = sorted([AminY, AmaxY, BminY, BmaxY])

    def ExportTBGE(self):
        # print("kkkk")
        if self.GraphicExport is not None:
            for o in self.Subspace:
                self.GraphicExport.AddRectangle(
                    position=o.Position,
                    Thickness=0,
                    FillColorCode=o.Room * 17 + 30,
                    StrokeColorCode=1,
                    text="-".join([str(o.Room), str(o.SubspcaceCode)])
                )
        # self.GraphicExport.End(Point0)

    def SetFenestrations(self):
        pass

    def SetEntranceDoor(self):
        pass

    def __del__(self):
        pass


def GeneratePlanFromNumericData(HyperParameters, Features, NumericData, TBGEElement=None, TBGEFrame=None):
    ReloadAllImports()
    Plan = PLAN(
        HyperParameters=HyperParameters,
        Features=Features,
        NumericData=NumericData,
        TBGEElement=TBGEElement,
        TBGEFrame=TBGEFrame
    )
    # ==== CHECK #1:
    PatternCheck.Evaluate(Plan, "PGssMm")
    if Plan.Score < 1:
        return Plan
    # === Continue to complete Plan
    Plan.SetSubspacePositions()
    Plan.MergeSubspacesAndFindDoors()
    # === Check #2
    PatternCheck.Evaluate(Plan, "PGssC")
    if Plan.Score < 2:
        Plan.ExportTBGE()
        return Plan
    # === Check #3
    PatternCheck.Evaluate(Plan, "PGAC")
    if Plan.Score < 3:
        Plan.ExportTBGE()
        return Plan

    # TestScore=PatternCheck.Evaluate("PGssC",Plan)
    # Plan.Score+=TestScore
    ##
    Plan.SetFenestrations()
    Plan.SetEntranceDoor()
    Plan.ExportTBGE()
    return Plan


def ScoreFunction(HyperParameters, Features, NumericData):
    # WE HAVE TO MAKE NUMERICDATA 2D!!!!!!
    NumericData2D = [[NumericData[i * 8 + j] for j in range(8)] for i in range(16)]
    return GeneratePlanFromNumericData(HyperParameters, Features, NumericData2D, TBGEElement=None, TBGEFrame=None).Score
