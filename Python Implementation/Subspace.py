# Subspace Class

class SUBSPACE:
    def __init__(self, HyperParameters, numericDiscrip):
        self.Xposition = numericDiscrip[0]
        self.Yposition = numericDiscrip[1]
        self.Xweight = numericDiscrip[2]
        self.Yweight = numericDiscrip[3]
        self.Room = int(numericDiscrip[4] * HyperParameters.RoomNumber)
        self.SubspcaceCode = numericDiscrip[5]
        self.HasOpening = True if numericDiscrip[6] > 0.5 else False
        self.IsFenestrated = True if numericDiscrip[7] > 0.5 else False
        self.Position = []
        self.IsEntranceDoor = False

    def Print(self):
        print("Xpos", self.Xposition, end="-")
        print("Ypos", self.Yposition, end="-")
        print("Room", self.Room, end=": ")
        print(self.SubspcaceCode)
