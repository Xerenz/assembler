



#label,opcode,operand=read first line of input
#initialize symtab

f1 = open("src.txt","r")
f2 = open("optab.txt","r")
f3 = open("inter.txt","a+")
f4 = open("symtab.txt","a+")

def pass1():
	x=f1.readline()
	pgm = x.split(" ")
	pgm[2] = pgm[2].rstrip('\n')
	label,opcode,operand = pgm
	if opcode == 'START':
		starting_addr = operand
		locctr = starting_addr
		
		f3.write(x)	#write line to intermediate file
				#read next input line
	else :
		locctr = 0
#	while opcode != 'END':
	for i in f1:
		pgm=i.split()
		pgm[2] = pgm[2].rstrip('\n')
		label,opcode,operand = pgm
		if opcode == 'END':
			f3.write(i)
			break
		if label != "\t":
			if !find(label,"symtab.txt") :   #complete
				#insert(label,locctr,symtab) #insert label and locctr to symtab
				f4.write(label+"\t"+locctr)
			else:
				print("Error!!! Duplicate symbol")
		if find(opcode,"optab.txt"):
			locctr+=3
		elif opcode == 'WORD':
			locctr+=3
		elif opcode == 'RESW':
			locctr+=(3*int(operand))
		elif opcode == 'RESB':
			locctr+=int(operand)
		#elif opcode == 'BYTE':
		#	locctr+=(#length of constant in bytes)
		else:
			print("Error!!! Invalid	 operation code")
		
		#write line to intermediate file
		f3.write(i)
		
		#read next input line
		
		
	#write last line to intermediate file
	
	program_length = locctr - starting_addr
def find(value,fileName):
	ft = open(fileName,"r")
	for i in ft:
		line = i.split()
		#line[1] = line[1].rstrip('\n')
		if line[0] == value:
			ft.close()
			return True
	ft.close()
	return False
