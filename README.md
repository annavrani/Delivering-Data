# Delivering Data: A Real-World Dataset for Last-Mile Delivery Optimization 

## Overview  

This repository provides scripts to download, extract, and analyze a dataset that includes time and distance matrices used in a Vehicle Routing Problem (VRP) study. Hosted on [Zenodo](https://doi.org/10.5281/zenodo.15310106), the dataset is valuable not only for VRP research but also for statistical analysis, including travel time distribution modeling. In addition to scripts for downloading and extracting the data, this repository includes a script for statistical analysis and an example script demonstrating how to download the data and analyze the first day's records. The provided scripts can be adapted for any desired data processing after loading the required information into DataFrames.

The [dataset](https://doi.org/10.5281/zenodo.15310106) is submitted for publication in 
[Data in Brief Journal](https://www.sciencedirect.com/journal/data-in-brief).

## Dataset Access  

The dataset is not stored in this repository but can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.15310106). The 'download_and_extract_data.py' script automates the process of downloading and extracting the data. You can run this script directly or include the following code in your own script to perform the download and extraction:

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

## Cite as:

*Vrani, A., Apostolidis, S. D., Kapoutsis, A. Ch., & Kosmatopoulos, E. B. (2025). Delivering data: A real-world dataset for last-mile delivery optimization. Data in Brief, 61, 111762.* \[[Link](https://doi.org/10.1016/j.dib.2025.111762)\]
```bibtex
@article{VRANI2025111762,
title = {Delivering data: A real-world dataset for last-mile delivery optimization},
journal = {Data in Brief},
volume = {61},
pages = {111762},
year = {2025},
issn = {2352-3409},
doi = {https://doi.org/10.1016/j.dib.2025.111762},
url = {https://www.sciencedirect.com/science/article/pii/S2352340925004895},
author = {Anna Vrani and Savvas D. Apostolidis and Athanasios Ch. Kapoutsis and Elias B. Kosmatopoulos},
keywords = {VRP benchmark, Distance matrix, Logistics optimization, Pharmaceutical deliveries},
abstract = {This dataset was collected to support Vehicle Routing Problem (VRP) optimization by providing structured time and distance matrices. A Third-Party Logistics (3PL) company granted access to its order management software, from which data on daily delivery problems involving pharmaceutical distribution were obtained. The dataset consists of carefully processed distance and time matrices, over a period of nine days. Each day’s problem involved 60-85 delivery stops that needed to be serviced. While the actual delivery routes covered only specific paths taken on the road, the generated matrices provide a complete view of travel distances and times between all locations, information essential for optimizing the routing process. To ensure confidentiality, only the structured matrices are provided, without the original address data. These matrices were generated using an API that computes travel durations based on historical traffic patterns, real-time data, and predictive models. From the API, we derived four distinct matrices: one for distances and three for travel times under different traffic scenarios: optimistic, pessimistic, and most likely. These matrices enable the modelling of realistic travel conditions accounting for the road congestion variability. Data retrieval was performed through automated API queries, ensuring consistency in structure and format. The collected matrices were processed and structured for direct use in VRP algorithms. The dataset offers substantial reuse potential by serving as a benchmark for evaluating VRP algorithms, enabling the comparison of optimization methods based on real-world logistics problems. It also supports statistical analysis and simulation, allowing researchers to assess travel time variability and model uncertainty in routing decisions through Monte Carlo simulations. Overall, this dataset offers valuable insights for optimizing delivery operations and addressing real-world logistics challenges. Its structured format, comprehensive traffic-based travel times, and applicability to VRP make it a valuable resource at the intersection of academia and industry.}
}
