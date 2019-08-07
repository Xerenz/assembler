
from util import find, find_mc

def PASS2(starting_addr, program_length):
	'''PASS2  algorithm to generate
the machine code from the intermediate file.
'''
	global locctr

	f1 = open('inter.txt','r')
	f2 = open('machine.txt','a')
	# read first input line
	x = f1.readline()
	pgm = x.split(" ")
	pgm[2] = pgm[2].rstrip('\n')
	label, opcode, operand = pgm

	if opcode == 'START':
		f2.write('H' + label + '000' + str(starting_addr) + str(program_length)) # write listing line
		f2.close()


	# start reading code
	buff = ''

	counter = 0
	for i in f1:
		line = i.split(' ') # correct optab and inter
		opcode = line[1]
		operand = line[2]
		if counter==0:
			start = line[3]
		counter += 1

		if opcode == 'WORD':
			buff += ((6 - len(operand))*'0' + operand)
		elif opcode == 'RESW':
			buff, counter = store_t(buff, counter, start)
		elif opcode == 'RESB':
			buff, counter = store_t(buff, counter, start)
		elif opcode == 'BYTE':
			buff += '00FFAB'
		elif opcode == 'END':
			f2 = open('machine.txt','a')
			buff, counter = store_t(buff, counter, start)
			f2.write('\nE' + '000' + str(starting_addr))
			f2.close()
		else:
			mc = find_mc(line[1], 'optab.txt') 

			address =  find_mc(line[2], 'symtab.txt')
			if not address:
				address = line[2]
			buff = buff + (mc + address)

		if counter >= 10:
			buff, counter = store_t(buff, counter, start)

def store_t(buff, counter, start):
	fO = open('machine.txt', 'a')

	t = '\nT' + start.rstrip('\n')
	length = len(buff)/2
	hex_num = hex(int(length))[2:]
	t += hex_num

	fO.write(t + buff)
	fO.close()

	return '', 0

if __name__ == '__main__':
	print('RUNNING PASS2 ALGORITHM..')
	PASS2()

		
