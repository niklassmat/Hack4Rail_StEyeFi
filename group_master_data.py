import pandas as pd

df = pd.read_csv(r'C:\Users\NiklasMathauer\Downloads\master_data\master_data.csv', sep=';')

df.drop(columns=['pax_counter_id', 'equipmentname', 'tplnr', 'tpname'],axis=1, inplace=True)
df_grouped = df.groupby('station_id').first().reset_index()

print(df.columns.tolist())
print(df_grouped.head().to_string())
df_grouped.to_csv('master_data_grouped.csv', index=False)