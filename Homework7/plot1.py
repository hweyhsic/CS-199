import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    WL1 = list();
    #F1 = open( "wordlist1.txt", 'r' );
    F1 = open( "WL1.txt", 'r' );
    for item in F1:
        WL1.append( int(item.rstrip()) );

    WL2 = list();
    #F2 = open( "wordlist2.txt", 'r' );
    F2 = open( "WL2.txt", 'r' );
    for item in F2:
        WL2.append( int(item.rstrip()) );

    orig_fasta = pd.DataFrame( {"Lengths" : WL1} );
    reference_fasta= pd.DataFrame( {"Lengths" : WL2} );

    plt1 = sns.lineplot( data=orig_fasta );
    plt.show();
    plt2 = sns.lineplot( data=reference_fasta );
    #plt2 = sns.distplot( data=reference_fasta );
    plt.show();
