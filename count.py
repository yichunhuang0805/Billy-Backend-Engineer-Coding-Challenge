import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data():
    """Load CSV and JSON data into DataFrames and prepare initial count dictionary."""
    try:
        df = pd.read_csv('encodes.csv')
        df['key'] = df['domain'].astype(str) + '/' + df['hash'].astype(str)
        count_dict = {k: 0 for k in df['key']}

        df2 = pd.read_json('decodes.json')
        df2 = df2[['bitlink', 'timestamp']]
        logging.info("Data loaded successfully from CSV and JSON.")
        return df, df2, count_dict
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def clean_data(df2):
    """Remove rows with null values and those not matching criteria."""
    try:
        # Remove rows with null values
        original_rows = len(df2)
        df2 = df2.dropna()
        deleted_rows = original_rows - len(df2)
        logging.info(f"{deleted_rows} rows containing null values were found and deleted.")

        # Filter data for the year 2021 and ensure bitlinks start with "http://"
        df2['timestamp'] = pd.to_datetime(df2['timestamp'])
        df2 = df2[df2['timestamp'].dt.year == 2021]
        starts_with_http = df2['bitlink'].str.startswith('http://')
        original_count = len(df2)
        df2 = df2[starts_with_http]
        deleted_rows = original_count - len(df2)
        logging.info(f"{deleted_rows} rows not starting with 'http://' were found and deleted.")
        return df2
    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
        raise

def update_counts(df2, count_dict):
    """Update the click counts based on the filtered data."""
    try:
        for bitlink in df2['bitlink']:
            key = bitlink.replace('http://', '')
            if key in count_dict:
                count_dict[key] += 1
        logging.info("Click counts updated successfully.")
        return count_dict
    except Exception as e:
        logging.error(f"Error updating counts: {e}")
        raise

def generate_results(df, count_dict):
    """Map the counts from the dictionary back to the DataFrame and sort it."""
    try:
        df['count'] = df['key'].map(count_dict)
        df = df.sort_values(by='count', ascending=False)
        logging.info("Results generated and sorted successfully.")
        return df
    except Exception as e:
        logging.error(f"Error generating results: {e}")
        raise

def main():
    df, df2, count_dict = load_data()
    df2 = clean_data(df2)
    count_dict = update_counts(df2, count_dict)
    df = generate_results(df, count_dict)
    
    # Convert to JSON format and print
    result_json = [{row['long_url']: row['count']} for index, row in df.iterrows()]
    print(result_json)
    logging.info("Program completed successfully.")

if __name__ == "__main__":
    main()
