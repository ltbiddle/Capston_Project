import os
import pandas as pd

#Transposing csv files

#Defining input/output directories
input_directory = "/Users/lancebiddle/CodeYou/Capstone Project/Harvest Data/Raw Data"
output_directory = "/Users/lancebiddle/CodeYou/Capstone Project/Harvest Data/Data Cleaned/Transposed"

#Creating transposing Function
def transpose_csv_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a CSV file
        if filename.endswith(".csv"):
            input_path = os.path.join(input_dir, filename)
            
            # Read the CSV file
            df = pd.read_csv(input_path)
            
            # Transpose the DataFrame
            transposed_df = df.transpose()
            
            # Generate the output file path
            output_path = os.path.join(output_dir, filename)
            
            # Save the transposed DataFrame
            transposed_df.to_csv(output_path, header=False)
            print(f"Transposed and saved: {output_path}")

transpose_csv_files(input_directory, output_directory)



#Combining data frames
#Define path to CSV files
path = '/Users/lancebiddle/CodeYou/Capstone Project/Harvest Data/Data Cleaned/Transposed'
extension = '.csv'

#Identify all CSV files
files = [file for file in os.listdir(path) if file.endswith(extension)]

#Import CSV Files
dfs = []
for file in files:
	df = pd.read_csv(os.path.join(path, file))
	dfs.append(df)

#Merge all CSV files into on DataFrame
df = pd.concat(dfs,  ignore_index=True)

#New Header
df.columns = ["License Year", "2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015"]

#Saving result to new CSV file
df.to_csv('/Users/lancebiddle/CodeYou/Capstone Project/Harvest Data/Data Cleaned/Merged/Harvest_Data_Merged.csv', header=True)

