import glob     # Used to find all file paths matching a pattern
import os       # For file path manipulation
import sys      # Optional: useful for debugging, not used here
import pandas as pd  # For data handling

# 📥 1. Load master data that contains information for merging (e.g., about sensors or locations)
df_master = pd.read_csv(
    r'C:\Users\NiklasMathauer\Downloads\master_data\master_data.csv', 
    sep=';'  # Using semicolon as separator
)

# 📁 2. Set the folder path where all CSV files (likely containing sensor measurements) are stored
folder_path = r'C:\Users\NiklasMathauer\Downloads\FrankfurtaM'

# 📄 3. Find all .csv files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 🧮 4. Load all found CSV files and combine them into one DataFrame
df = pd.concat(
    (pd.read_csv(f, sep=';') for f in csv_files), 
    ignore_index=True  # So index is reset after concat
)

# 🔗 5. Merge measurement data with master metadata using 'pax_counter_id' as key
main_df = pd.merge(df_master, df, how='left', on='pax_counter_id')

# 🗓️ 6. Create a new column with formatted date (DD.MM.YYYY) from the timestamp
main_df['time_iot_date'] = pd.to_datetime(main_df['time_iot']).dt.strftime('%d.%m.%Y')

# 📆 7. Extract the weekday name (e.g., Monday) from the date
main_df['weekday'] = pd.to_datetime(main_df['time_iot_date'], format='%d.%m.%Y').dt.day_name()

# 🖨️ 8. Show the first few rows for inspection
print(main_df.head().to_string())

# 🧾 9. Print all column names
print(main_df.columns.tolist())

# 📚 10. Define all days of the week to loop over
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 📊 11. Create a new empty DataFrame to store aggregated results
final_df = pd.DataFrame(columns=['Weekday', 'Average_pax_count', 'Upper_Bound', 'Lower_Bound'])

# 🔁 12. Loop over each day to calculate average passenger counts for the specific station
for day in days_of_the_week:
    # Filter data to only include rows for the current weekday and target station
    main_df_weekday = main_df[
        (main_df['weekday'] == day) &
        (main_df['station_name'] == 'Frankfurt (Main) Ost')
    ].reset_index(drop=True)

    # Calculate total passenger count for this weekday
    sum_of_pax_count = main_df_weekday['data_pax'].sum()

    # Count number of distinct dates for this weekday (to get number of actual days)
    number_of_days = main_df_weekday['time_iot_date'].nunique()

    # Calculate average passenger count per day
    average_pax_count = sum_of_pax_count / number_of_days

    # 🔎 Print results to console for validation
    print('Weekday: ' + day)
    print('Pax count in total at this station: ' + str(sum_of_pax_count))
    print('Number of days: ' + str(number_of_days))
    print("Average pax count per day: " + str(average_pax_count))

    # ➕ Append the results as a new row in final_df, with +/- 10% bounds
    final_df.loc[len(final_df)] = [
        day,
        int(average_pax_count),
        int(average_pax_count * 1.1),
        int(average_pax_count * 0.9)
    ]

# 📤 13. Print final summary table
print(final_df.head().to_string())
