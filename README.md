# README: Time and Distance Matrices for VRP and Statistical Analysis

## Overview

This repository contains time and distance matrices in Excel format, which were used for a Vehicle Routing Problem (VRP) study. The dataset can also be useful for statistical analysis, such as modeling travel time distributions. The data were used in an article submitted to *Data in Brief* and are available in the Zenodo repository.

## Dataset Description

The dataset represents approximately one month of routing operations for a pharmaceutical delivery company. Since deliveries occur twice per week, the dataset includes nine (9) distinct daily instances, covering around four to five weeks of real-world operations. Each instance accounts for operational constraints, such as order demands, time windows, distances, and travel times under different traffic conditions.

## Folder Structure

The repository contains two main folders:

### 1. **Time and Distance Matrices**

This folder contains travel distances and estimated travel times between delivery locations for each of the nine daily instances. To ensure confidentiality, exact node locations are not included.

#### Files in this folder:

Each dataset version (1-9) consists of four corresponding Excel files:

- `distance_matrix_X.xlsx` – Pairwise distances (in kilometers) between delivery locations.
- `time_matrix_mostlikely_X.xlsx` – Expected travel time (minutes) under typical traffic conditions.
- `time_matrix_optimistic_X.xlsx` – Best-case travel time (minutes) with minimal traffic.
- `time_matrix_pessimistic_X.xlsx` – Worst-case travel time (minutes) with heavy traffic delays.

Where **X** represents the dataset number (1-9).

### 2. **Order Characteristics**

This folder contains an Excel file (`orders.xlsx`) with nine sheets, each corresponding to a specific day's delivery requests. The file includes the following columns:

| Column Name   | Description                                          |
| ------------- | ---------------------------------------------------- |
| NODE\_ID      | Unique identifier for each delivery request          |
| WEIGHT        | Weight of the shipment (kg)                          |
| VOLUME        | Volume of the shipment (cubic meters)                |
| SERVICE\_TIME | Time required to complete the delivery (minutes)     |
| EAT           | Earliest arrival time allowed for delivery           |
| LAT           | Latest arrival time allowed for delivery             |
| TIME\_WINDOW  | Allowed delivery time window, defined by EAT and LAT |

## Example Code

A Python script (usage_example.py) is provided to demonstrate how to read the Excel files and parse the data for further analysis. While the dataset is primarily used for Vehicle Routing Problem (VRP), this script illustrates how to extract and process travel time data from the uploaded Excel files, using the three different time matrices for each instance to calculate the mean and standard deviation of travel time between all node combinations for both triangular and beta distributions. 


