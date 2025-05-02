# Delivering Data: A Real-World Dataset for Last-Mile Delivery Optimization 

## Overview  

This repository provides scripts to download, extract, and analyze a dataset that includes time and distance matrices used in a Vehicle Routing Problem (VRP) study. Hosted on [Zenodo](https://zenodo.org/uploads/15310106), the dataset is valuable not only for VRP research but also for statistical analysis, including travel time distribution modeling. In addition to scripts for downloading and extracting the data, this repository includes a script for statistical analysis and an example script demonstrating how to download the data and analyze the first day's records. The provided scripts can be adapted for any desired data processing after loading the required information into DataFrames.

The [dataset](https://zenodo.org/uploads/15310106) is submitted for publication in 
[Data in Brief Journal](https://www.sciencedirect.com/journal/data-in-brief).

## Dataset Access  

The dataset is not stored in this repository but can be downloaded from [Zenodo](https://zenodo.org/uploads/15310106). The 'download_and_extract_data.py' script automates the process of downloading and extracting the data. You can run this script directly or include the following code in your own script to perform the download and extraction:

````
import download_and_extract_data

if __name__ == "__main__":
    # Download and extract dataset
    download_and_extract_data.download_data()
    download_and_extract_data.extract_data()
````

## Dataset Processing

The `process_data.py` script demonstrates how to:  

- Load time and distance matrices from the Zenodo dataset  
- Parse the data into Pandas DataFrames  
- Analyze travel times using different traffic conditions  
- Compute mean and standard deviation for travel time distributions

You can either run this script directly or include the following code in your script to perform the analysis for the desired day(s):

````
import process_data

if __name__ == "__main__":
    # Example of processing data for day 1 - You can update this part accordingly to process data in your desires way
    file_optimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_optimistic_1.xlsx"
    file_most_likely = "extracted_data/time_and_distance_matrices/day_1/time_matrix_mostlikely_1.xlsx"
    file_pessimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_pessimistic_1.xlsx"

    output_file_name = "computed_results_day_1.xlsx"

    process_data.process(file_optimistic, file_most_likely, file_pessimistic, output_file_name)
````

## Example for downloading data and performing analysis for day 1

The `example_day_1.py` script combines the two code blocks presented above to provide a complete example of downloading the data and performing statistical analysis for a specific day.
