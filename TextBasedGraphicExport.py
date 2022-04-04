# Class of TBGE

class TBGE:
    def __init__(self, FileName, DateCode):
        # We Open File At the end to prevent some problems
        self.Address = "E:/Desktop/ML class/Pattern-Based Plan Designer AI/" + DateCode + "/" + FileName + ".TBGE"
        self.Output = []

    def SetFrame(self, FrameNumber):
        Command = "FRAME: Code=" + str(FrameNumber) + '\n'
        self.Output.append(Command)

    def AddLine(self, p1, p2, **ArgumentsTemp):
        Arguments = {key: str(value) for key, value in zip(("X0", "Y0", "X1", "Y1"), (p1[0], p1[1], p2[0], p2[1]))}  # For required Args
        for key, value in ArgumentsTemp.items():  # For Optional Args
            value = "'" + value + "'" if isinstance(value, str) else str(value)
            Arguments[key] = value
        Command = "LINE: " + " ".join(["{}={}".format(key, value) for key, value in Arguments.items()]) + '\n'
        self.Output.append(Command)
        # print(  )

    def AddRectangle(self, position, **ArgumentsTemp):
        Arguments = {key: str(value) for key, value in zip(("X0", "Y0", "X1", "Y1"), position)}  # For required Args
        for key, value in ArgumentsTemp.items():  # For Optional Args
            value = "'" + value + "'" if isinstance(value, str) else str(value)
            Arguments[key] = value
        Command = "RECTANGLE: " + " ".join(["{}={}".format(key, value) for key, value in Arguments.items()]) + '\n'
        self.Output.append(Command)
        # pass

    def Clear(self):
        self.Output = []

    def End(self):
        with open(self.Address, "w") as file:
            file.writelines(self.Output)
