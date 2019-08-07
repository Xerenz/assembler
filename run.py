''' Main python file running PASS1 and PASS2 programs.'''

from pass1 import PASS1
from pass2 import PASS2

def main():
	print('Running Pass1..')
	SA, PL = PASS1()
	print('Symbtab and intermediate file created..')
	print('Running Pass2..')
	PASS2(SA, PL)
	print('Machine Code Generated.')

if __name__ == '__main__':
	main()
