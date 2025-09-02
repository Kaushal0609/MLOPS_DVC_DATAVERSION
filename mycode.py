import pandas as pd
import os


# Create a sample dataframe with column names

data = {'name': ['Raj', 'Alakh', 'Ram'],
        'Age':[25,35,28],
        'City':["New York", "Canada","Brazil"]}

df = pd.DataFrame(data)

# Add new data to dataframe

new_row = {'name':'GF1','Age':25, 'City': "Canada"}
df.loc[len(df.index) ] = new_row

# Ensure the data directory exists at the root level

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"csv file saved to the {file_path}")
