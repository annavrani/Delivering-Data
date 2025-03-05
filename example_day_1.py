import download_and_extract_data
import process_data

if __name__ == "__main__":
    # Download and extract dataset
    zip_file_name, zip_file_url = download_and_extract_data.get_zip_file_url()
    zip_file_path = download_and_extract_data.download_zip(zip_file_name, zip_file_url)
    download_and_extract_data.extract_zip(zip_file_path)

    # Example of processing data for day 1 - You can update this part accordingly to process data in your desires way
    file_optimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_optimistic_1.xlsx"
    file_most_likely = "extracted_data/time_and_distance_matrices/day_1/time_matrix_mostlikely_1.xlsx"
    file_pessimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_pessimistic_1.xlsx"

    output_file_name = "computed_results_day_1.xlsx"

    process_data.load_and_process(file_optimistic, file_most_likely, file_pessimistic, output_file_name)