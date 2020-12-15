from itertools import permutations
import os

for group in permutations(['healthcare','molina','passport','healthplan'],2):
	print (''.join(group))
print('molinahealthcare.com , health.com' , 'health' , 'association')
