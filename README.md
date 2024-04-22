# Bitly Backend Coding Challenge

## Overview
This program processes data from CSV and JSON files to calculate the number of clicks on bitlinks from the year 2021.

## Installation
1. Ensure Python 3 is installed on your machine.
2. Install required Python packages:
   ```bash
   make install

## Running the Application
To run the application, follow these steps:
1. Open your terminal or command prompt
2. Naviage to the folder containing the scripts(count.py, test.py), encodes.csv and decodes.json
3. Run the script:
    ```bash
    make run

## Test the Application
To run unit tests for each function, follow these steps:
1. Open your terminal or command prompt
2. Naviage to the folder containing the scripts(count.py, test.py), encodes.csv and decodes.json
3. Run the test:
    ```bash
    make test

## Design Decisions
### Use of Dictionary for Encodes.csv Data
The decision to use a dictionary to store data from encodes.csv was driven by the need for efficient lookup and manipulation of key-value pairs. Dictionaries offer constant-time lookup, making them ideal for quickly retrieving information based on a unique identifier. In this case, combining the domain and hash columns into a composite key provides a unique identifier for each record.
### Handling Null Values and Data Cleaning
The script checks for null values in the bitlink and timestamp columns of the decodes.json file to ensure data integrity and consistency throughout the analysis process.
Also, it checks for appropriate prefix in bitlink, supposing it starts with "http://", to avoid confusion when decomposing the link.
### Error Handling and Logging
Logging is used to signal successful data loading from both the CSV and JSON files. This provides operational transparency and reassures users that the initial data loading step was completed without errors.