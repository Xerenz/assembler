
from util import find

f1 = open("src.txt","r")
f2 = open("optab.txt","r")
f3 = open("inter.txt","w+")
f4 = open("symtab.txt","w+")

def PASS1():
	x = f1.readline()
	pgm = x.split(" ")
	pgm[2] = pgm[2].rstrip('\n')
	label, opcode, operand = pgm

	if opcode == 'START':
		starting_addr = operand
		locctr = starting_addr
		
		f3.write(x)	#write line to intermediate file
				#read next input line
	else :
		locctr = 0

	for instr in f1:
		pgm = instr.split()
		pgm[2] = pgm[2].rstrip('\n')
		label, opcode, operand = pgm

		if opcode == 'END':
			f3.write(instr)
			break

		if label != "\t":
			if find(label,"symtab.txt") is False:   #complete
				#insert(label,locctr,symtab) #insert label and locctr to symtab
				f4.write(label+"\t"+locctr)
			else:
				print("Error!!! Duplicate symbol")

		if find(opcode,"optab.txt"):
			locctr += 3
		elif opcode == 'WORD':
			locctr += 3
		elif opcode == 'RESW':
			locctr += 3*int(operand)
		elif opcode == 'RESB':
			locctr += int(operand)
		elif opcode == 'BYTE':
			locctr += len(opcode)
		else:
			print("Error!!! Invalid	 operation code")
		
		#write line to intermediate file
		f3.write(instr)
		
		#read next input line
		
		
	#write last line to intermediate file
	
	program_length = locctr - starting_addr