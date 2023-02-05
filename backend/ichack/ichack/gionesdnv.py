import pandas as pd
import numpy as np
df = pd.read_csv('ichack/companies.csv')

df['email'] = [df['website'][i].split('.')[1]+'@gmail.com' for i in range(len(df))]

df.to_csv('ichack/companies.csv', index=False)