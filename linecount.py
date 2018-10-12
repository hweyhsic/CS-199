f = open('ecoli.txt', 'r' )
lc = 0
for line in f:
	lc += 1
#linecount = sum( 1 for line in f )
#print(linecount)
print(lc)
