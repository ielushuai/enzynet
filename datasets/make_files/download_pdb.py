'Converts list of PDB enzymes in a text file'

# Authors: Afshine Amidi <lastname@mit.edu>
#          Shervine Amidi <firstname@stanford.edu>

# MIT License

import pandas as pa
import csv
from enzynet.tools import read_dict


# Read csv files
df = pa.read_csv('../dataset_all.csv', header=None)

# Only keep PDB IDs
df = df[0]+', '
df = df.tolist()

# Save to text file with one PDB ID per line
file = open('../download_pdb.txt','w')
for i in range(len(df)):
    file.write(df[i])
file.close()
