import pandas as pd
import numpy as np

# set filename where the data is located
# to run the analysis with new data, replace this filename with the filename of the new data
input_filename = "data/experiment_20250126.txt"

# read in txt file with experiment data to a pandas DataFrame
experiment_data = pd.read_table(input_filename, 
	header = None, 
	names = ["seconds_since_midnight_utc", "atmospheric_pressure_hpa", "hcl_mixing_ratio_ppbv", "o3_mixing_ratio_ppbv"])

# create a variable for the experiment date
experiment_data['date'] = input_filename[-12:-4]

# round atmospheric pressure to 2 decimal places 
experiment_data['atmospheric_pressure_hpa'] = np.round(experiment_data['atmospheric_pressure_hpa'])

output_filename = input_filename.replace(["txt", "data"], ["csv", "results"])
output_filename = output_filename.replace("data", "results")

# write dataframe to csv file
experiment_data.to_csv(output_filename)

