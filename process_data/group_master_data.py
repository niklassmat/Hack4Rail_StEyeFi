import pandas as pd  # 📦 Import the pandas library for data manipulation

# 📥 1. Load the master data CSV file using ';' as separator
df = pd.read_csv(r'C:\Users\NiklasMathauer\Downloads\master_data\master_data.csv', sep=';')

# ❌ 2. Drop columns you don’t need: these are likely metadata columns
df.drop(columns=['pax_counter_id', 'equipmentname', 'tplnr', 'tpname'], axis=1, inplace=True)

# 🧮 3. Group the DataFrame by 'station_id'
#      For each group, take the first row (you assume other values are the same or not needed)
df_grouped = df.groupby('station_id').first().reset_index()

# 🖨️ 4. Print the remaining column names
print(df.columns.tolist())

# 🧾 5. Show the grouped DataFrame
print(df_grouped.head().to_string())

# 💾 6. Save the grouped result to a new CSV file
df_grouped.to_csv('master_data_grouped.csv', index=False)
