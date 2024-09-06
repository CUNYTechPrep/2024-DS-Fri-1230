### File `mixed_types.csv` cleaning process. 

0. Read in with with na_values=['MISSING']
0. ' NULL' values not registering because of stupid whitespaces. 
0. Remove whitespace by loop through all string cols and stripping. 
0. repace 'NULL' with np.nan
