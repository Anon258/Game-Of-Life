def B3_S23(alive, neighbours):
	return neighbours==3 or (alive and neighbours==2)

def B34_S34(alive, neighbours):
	return neighbours==3 or neighbours==4

def B3_S012345678(alive, neighbours):
	return alive or neighbours==3

def B2_S(alive, neighbours):
	return not alive and neighbours==2

def B1357_S1357(alive, neighbours):
	return neighbours==1 or neighbours==3 or neighbours==5 or neighbours==7

def B36_S23(alive,neighbours):
	return neighbours==3 or (not alive and neighbours==6) or (alive and neighbours==2)