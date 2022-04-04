import random

## 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode

def GenerateRandom(NumberOfSubspaces):
	return [[random.random() for j in range(6)] for i in range(NumberOfSubspaces)]
