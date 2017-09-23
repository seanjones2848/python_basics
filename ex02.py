import sys

i = 0;
args = []

for arg in sys.argv:
	print ("Argv of " + str(i) + " is " + str(arg))
	i += 1

sortv = sorted(sys.argv, key=len, reverse=True)

for arg in sortv:
	print(arg)	
