import glob
import os
import sys
import pandas as pd

df_master = pd.read_csv(r'C:\Users\NiklasMathauer\Downloads\master_data\master_data.csv', sep=';')

folder_path = r'C:\Users\NiklasMathauer\Downloads\FrankfurtaM'

csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

df = pd.concat((pd.read_csv(f, sep=';') for f in csv_files), ignore_index=True)

main_df= pd.merge(df_master, df, how='left', on='pax_counter_id')

main_df['time_iot_date'] = pd.to_datetime(main_df['time_iot']).dt.strftime('%d.%m.%Y')

main_df['weekday'] = pd.to_datetime(main_df['time_iot_date'], format='%d.%m.%Y').dt.day_name()
print(main_df.head().to_string())

print(main_df.columns.tolist())
#test = main_df[['station_id', 'weekday', 'data_pax']].groupby(['station_id', 'weekday']).agg(
 #   data_pax=('data_pax', 'sum'))
#print(test.head().to_string())
#main_df.to_csv('master_data.csv', index=False)
#sys.exit()
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

final_df = pd.DataFrame(columns=['Weekday', 'Average_pax_count', 'Upper_Bound', 'Lower_Bound'] )

for day in days_of_the_week:
    main_df_weekday = main_df[
        (main_df['weekday'] == day) &
        (main_df['station_name'] == 'Frankfurt (Main) Ost')
    ].reset_index(drop=True)

    sum_of_pax_count = main_df_weekday['data_pax'].sum()
    number_of_days = main_df_weekday['time_iot_date'].nunique()
    average_pax_count = sum_of_pax_count/number_of_days

    print('Weekday: '+day)
    print('Pax count in total at this station: ' + str(sum_of_pax_count))
    print('Number of days: ' + str(number_of_days))
    print("Average pax count per day: " + str(average_pax_count))
    #print(main_df_weekday['data_pax'].max())

    final_df.loc[len(final_df)] = [day, int(average_pax_count), int(average_pax_count*1.1), int(average_pax_count*0.9)]


print(final_df.head().to_string())

#final_df.to_csv('frankfurt_data_weekday_averages.csv', index=False)