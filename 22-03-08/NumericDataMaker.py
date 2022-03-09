import random

## 0:Xpos, 1:Ypos, 2:Xweight, 3:Yweight, 4:ParentCode, 5:SubspaceCode, 6: Has Door?, 7: Has Fenestration?

def RandomNumericData(NumberOfSubspaces):
	return [[random.random() for j in range(8)] for i in range(NumberOfSubspaces)]
