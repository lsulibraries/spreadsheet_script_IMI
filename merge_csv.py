import pandas as pd
import sys

headers = pd.read_csv('headers.csv')
input = pd.read_csv(sys.argv[1])

output = headers.append(input, sort=False)

output.to_csv('output.csv', index=False)
