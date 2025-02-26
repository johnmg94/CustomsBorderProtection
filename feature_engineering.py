import psycopg2
from dotenv import load_dotenv
import dotenv
import os
import pandas as pd
from itertools import count

# file_path = os.environ.get('FILE_PATH')
# print(df.head)
# Function to check if a value is numeric (including strings of numbers)
def is_number(value):
    try:
        float(value)  # Try converting to a float
        return True
    except ValueError:
        return False

# Function to either keep numbers as they are or assign unique integer values to non-numeric entries
def to_int_or_map(val, mapping, counter):
    if is_number(val):  # If it's a number or a numeric string, keep as is (converted to int)
        return int(val)
    if val not in mapping:  # Otherwise, assign a unique integer
        mapping[val] = next(counter)
    return mapping[val]

def process_features(df):
    # Create a mapping and counter for unique non-numeric values
    unique_mapping = {}
    counter = count(1)  # Start from 1
    columns = df.columns
    new_df = pd.DataFrame()
    for col in range(len(columns)):
        new_name = str(columns[col]) + str(counter)
        # Apply transformation
        new_df[new_name] = df[columns[col]].apply(lambda x: to_int_or_map(x, unique_mapping, counter))
        counter = count(1)

    # Replace the 1's in col1_int with 2025
    new_df.loc[new_df['Fiscal Yearcount(1)'] == 1, 'Fiscal Yearcount(1)'] = 2025
    print(new_df.head)
    return new_df

def create_csv(unique_mapping):
    # Convert mapping dictionary to DataFrame
    mapping_df = pd.DataFrame(list(unique_mapping.items()), columns=['Original Value', 'Mapped Value'])

    # Save the mappings to a CSV file
    mapping_df.to_csv("data_dictionary.csv", index=False)

# x = create_plot(new_df)