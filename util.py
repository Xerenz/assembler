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
