p_string = 'CCCCCGFGCC;FE<FEGGGEFGGGGGG9FGDFFGCF<CE6;@FCCEGG7C+CFCGGGGDDEGGGFGGGGGGGGGGG'
r_list=[]

for char in p_string:
	r_list.append( ord(char) - 33 )
print('r_list', r_list)
p_value = sum( r_list )/len( r_list );
print( 'sum', sum(r_list), ' and len', len(r_list) )
print('p_value', float(p_value) )

result = 10 ** ( (-p_value) / 10 )
print(float(result))

(prob) = 1 - result
print( float(prob ) )
