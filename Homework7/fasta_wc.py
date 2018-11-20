f1 = open( "reference.fasta.gz", 'r')
wordlen = list();
index = 0;
charcount = 0;
contigs = 0;

for line in f1:
    for char in line:
        if( char == 'A' or char == 'C' or char == 'T' or char == 'G' or char == '\n'):
            charcount += 1;
        elif char == '>':
            line = line.rstrip();
        elif ( char == '\n' or char == '\r' ):
            wordlen.append( charcount );
            charcount = 0;
            contigs+=1;

print( "word lengths: ", wordlen );
print( "nu. contigs:  ", contigs );
