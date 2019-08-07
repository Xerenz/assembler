# utility function file

def find(value, fileName):
	ft = open(fileName, "r")
	for i in ft:
		line = i.split()

		if line[0] == value:
			ft.close()
			return True
	ft.close()
	return False

def find_mc(value, fileName):
	ft = open(fileName,"r")
	for i in ft:
		line = i.split()
		#line[1] = line[1].rstrip('\n')
		if line[0] == value:
			ft.close()
			return line[1]
	ft.close()
	return False

