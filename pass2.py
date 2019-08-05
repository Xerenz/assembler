
from util import find

f1 = open('inter.txt')
f2 = open('machine.txt')

def PASS2():
	# read first input line
	x = f1.readline()
	pgm = x.split(" ")
	pgm[2] = pgm[2].rstrip('\n')
	label, opcode, operand = pgm

	if opcode == 'START':
		f2.write('H' + label) # write listing line

	# start reading code

	for instr in f1:


