import pandas as pd

df = pd.read_csv('ichack/companies.csv')

df = df.drop(columns='role_ids')
df.to_csv('ichack/companies.csv')