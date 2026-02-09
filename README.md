## Air Quality Data Preparation

This script takes a txt file of air quality data generated from instrument X, extracts the date, rounds the variables, and writes it to a csv file.

### Requirements

#### Operating system

Windows 11

#### Software version

Python 3.11.4

#### Dependencies

- pandas 1.5.3
- numpy 1.24.3

### How to use this code

Install the requirements above, or import the computational environment with conda: `conda env export > environment.yml`

To run the analysis as-is, run `python process_data.py`. A new output file will appear in `results`

To re-run the analysis on new data:
1. Add a new data file to the `data` folder. The data file must be a text file with 4 unnamed columns that correspond to "seconds_since_midnight_utc", "atmospheric_pressure_hpa", "hcl_mixing_ratio_ppbv", and "o3_mixing_ratio_ppbv". The filename must have the format `experiment_YYYYMMDD.txt`
2. Update the path to the data as described in the code. 
3. Run `python process_data.py`. A new output file with the filename `experiment_YYYYMMDD.txt` will appear in `results`


