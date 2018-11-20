f1 = open( "reference.fasta", 'r' );

wordlen = list();

charcount = 0;
contigs = 0;

for line in f1:
    if len( line ) == 81:
        charcount += len(line);
    else:
        if charcount != 0:
            wordlen.append( charcount );
            charcount = 0;
            contigs+=1;

for entry in wordlen:
    print( entry );
