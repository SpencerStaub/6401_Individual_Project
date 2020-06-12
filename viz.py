import pandas as pd

df = seeds = pd.read_csv("Data_Extract_From_World_Development_Indicators (1).csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pd = pd.melt(df, id_vars=['Country Name','Country Code','Series Name'], var_name='Year').sort_values(['Country Name','Country Code','Series Name'])

pd = pd.groupby(['Country Name', 'Year', 'Series Name'])['value'].sum().unstack('Series Name')

pd.to_csv(r'test.csv', index = True)


