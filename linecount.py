f = open('ecoli.txt', 'r' )

linecount = 0

for line in f:
	linecount += 1

print(linecount)
