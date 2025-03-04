# README: Time and Distance Matrices for VRP and Statistical Analysis  

## Overview  

This repository provides an example script for analyzing time and distance matrices used in a Vehicle Routing Problem (VRP) study. Hosted on Zenodo (https://zenodo.org/uploads/14936915), the dataset is valuable not only for VRP research but also for statistical analysis, including travel time distribution modeling. The example code in this repository focuses on statistical analysis, demonstrating how to read the Excel files containing travel time data, store the information in DataFrames, and compute key statistical metrics. It was used in an article submitted to Data in Brief.

## Dataset Access  

The dataset is not stored in this repository but can be downloaded from Zenodo (https://zenodo.org/uploads/14936915). To streamline access, an SSH script (`setup_data_access.sh`) is included. This script automates the process of retrieving the dataset and ensuring compatibility with the provided example code.  

## Example Code  

The repository includes a Python script (`usage_example.py`) demonstrating how to:  

- Load time and distance matrices from the Zenodo dataset  
- Parse the data into Pandas DataFrames  
- Analyze travel times using different traffic conditions  
- Compute mean and standard deviation for travel time distributions  

## Running the Example  

1. Run the SSH script to download and set up the dataset:  
   ```bash
   bash setup_data_access.sh
