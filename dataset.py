## upload csv file

import pandas as pd
import numpy as np 

df_original = pd.read_csv('diabetes.csv') 

# Create ID column for JOIN later
df_original['Participants_ID'] = range(1, len(df_original) + 1)


## Create two new tables
# Table 1: participants info
df_participants = df_original[['Participants_ID', 'Age', 'Pregnancies']].copy()

# Table 2: Metabolic Measurements
df_measurements = df_original[['Participants_ID', 'Glucose', 'BloodPressure', 'BMI', 'Outcome']].copy()



## Simulate fasting data
n_rows = len(df_original)

# Simulate that 30% of the sample fasts for 16 hours
is_fasting = np.random.choice([True, False], size=n_rows, p=[0.3, 0.7]) 

df_fasting = pd.DataFrame({
    'Participants_ID': df_original['Participants_ID'],
    'Last_Meal_Time': np.where(is_fasting, '20:00:00', '22:00:00'),
    'First_Meal_Time': np.where(is_fasting, '12:00:00', '08:00:00')
})


## Import data from csv files
df_participants.to_csv('participants_info.csv', index=False)
df_measurements.to_csv('metabolic_measurements.csv', index=False)
df_fasting.to_csv('fasting_info.csv', index=False)


