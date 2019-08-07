
from util import find, find_mc

#label,opcode,operand=read first line of input
#initialize symtab

program_length = 0
locctr = 0
starting_addr = 0

def PASS1():
	'''PASS1 algorithm to generate
intermediate file from the main input file

of the  The main function of PASS1
algorithm is to create a symbol table
and allocate memory to instructions
using the location counter
'''
	global locctr
	global program_length
	global starting_addr

	f1 = open("src.txt","r")
	f2 = open("optab.txt","r")
	f3 = open("inter.txt","w+")
	f4 = open("symtab.txt","w+")

	x=f1.readline()
	pgm = x.split(" ")
	pgm[2] = pgm[2].rstrip('\n')
	label,opcode,operand = pgm
	if opcode == 'START':
		starting_addr = int(operand)
		locctr = starting_addr
		
		f3.write(x)	#write line to intermediate file
				#read next input line
	else :
		locctr = 0

	for i in f1:
		pgm=i.split(" ")
		print(pgm)
		pgm[2] = pgm[2].rstrip('\n')
		label,opcode,operand = pgm
		if opcode == 'END':
			f3.write(i)
			break
		if label != "\t":
			if not find(label,"symtab.txt") :   #complete
				#insert(label,locctr,symtab) #insert label and locctr to symtab
				f4.write(label+"\t"+str(locctr))
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
		elif opcode == 'BYTE':
			locctr+=(len(operand)-3)
		else:
			print("Error!!! Invalid	 operation code")
		
		#write line to intermediate file
		f3.write(i[:-1] + " " + str(locctr) + '\n')
		
		#read next input line
		
		
	#write last line to intermediate file
	
	program_length = locctr - starting_addr

	f1.close()
	f2.close()
	f3.close()
	f4.close()	

	return starting_addr, program_length

if __name__ == '__main__':
	print('WORKING OUT PASS1 ALGORITHM..')
	PASS1()
