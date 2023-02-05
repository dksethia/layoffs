import pandas as pd
import numpy as np
df = pd.read_csv('ichack/roles.csv')

df['role_id'] = [i for i in range(len(df))]

df.to_csv('ichack/roles.csv', index=False)