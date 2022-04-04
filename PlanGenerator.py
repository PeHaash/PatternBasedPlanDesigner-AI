## hello
## 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode
import math

def GenerateFrom(GlobalData,SubspaceDiscription):
	for ss in SubspaceDiscription:
		print(int(GlobalData.RoomNumber*ss[4]))
