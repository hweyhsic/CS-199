#import statistics
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd

#d_file = open("../../ee282/mytestfile.fastq")
d_file = open("../../../ee282/mytestfile.fastq")

def processlist( d_file ):
    index = 1
    minmaxmedlist = list()
    minmaxmedlist.append(list())
    minmaxmedlist.append(list())
    minmaxmedlist.append(list())
    minmaxmedlist.append(list())

    for line in d_file:
        if( index % 4 == 0 ):
            line = line.strip()

            myproblist = convertqual( line )

            minmaxmedlist[0].append( max(myproblist) )
            minmaxmedlist[1].append( min(myproblist) )
            minmaxmedlist[2].append( np.mean(myproblist) )
            minmaxmedlist[3].append( np.median(myproblist) )
            
        index+=1
    return minmaxmedlist

def convertqual( mycharstr ):
    mycharlist = list()
    for mychar in mycharstr:
        mycharlist.append( 1 - float( 10.0 ** float( -(ord(mychar)-33) / 10.0 ) ) )
    return mycharlist

if __name__ == "__main__":
    minmaxmedlist = processlist( d_file )

    minmaxmedDF = pd.DataFrame( minmaxmedlist ) #load data into DataFrame
    minmaxmedDF = minmaxmedDF.transpose()       #transpose data so 4 columns, 100 rows
    
    print( minmaxmedDF )

    #scatterplot
    sns.set()
    g = sns.scatterplot( data=minmaxmedDF )

    #histogram
    g = sns.distplot( minmaxmedDF[0], kde=False, rug=True )

    #pairplot
    g = sns.pairplot( minmaxmedDF )
    plt.show()

