import numpy

def Kadane(a):
	maxSoFar = 0
	maxHere = 0
	for i in range(0, len(a)):
		maxHere = max(maxHere + a[i], 0)
		maxSoFar = max(maxSoFar, maxHere)
	return maxSoFar
def Kadane2D(a):
	columns = len(a[0])
	rows = len(a)
	countAdditions = 0
	maxSoFar = 0
	maxHere =  0

	for k in range(0,columns):
		temp = []
		for d in range(len(a)):
			temp.append(0)
		for j in range(k,columns):
			for i in range(0, rows):
				temp[i]+=a[i][j]
			maxHere = Kadane(temp)
			if(maxHere > maxSoFar):
				maxSoFar = maxHere
	return maxSoFar
a = [[1,-6,3],[3,4,5],[-6,-7,-8]]
print "The sum of the maximum subrectangle is " + str(Kadane2D(a))