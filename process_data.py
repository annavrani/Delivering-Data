import pandas as pd
import numpy as np


def load_and_process(file_optimistic, file_most_likely, file_pessimistic, output_file_name ="computed_results.xlsx"):
    # Load Excel files into Pandas DataFrames
    df_opt = pd.read_excel(file_optimistic, index_col=0)
    df_most = pd.read_excel(file_most_likely, index_col=0)
    df_pess = pd.read_excel(file_pessimistic, index_col=0)

    # Ensure all dataframes have the same shape to avoid processing errors
    assert df_opt.shape == df_most.shape == df_pess.shape, "Mismatch in data dimensions!"

    # Function to compute statistical values based on optimistic, most likely, and pessimistic estimates
    def compute_statistics(a, m, b):
        mean_triangular = round((a + m + b) / 3, 2)  # Mean using a triangular distribution formula
        mean_beta = round((a + 4 * m + b) / 6, 2)  # Mean using a beta distribution (PERT) formula
        std_triangular = round((b - a) / np.sqrt(24), 2)  # Standard deviation for triangular distribution
        std_beta = round((b - a) / 6, 2)  # Standard deviation for beta distribution (PERT)
        return mean_triangular, std_triangular, mean_beta, std_beta

    # Create empty DataFrames to store computed results
    mean_triangular_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
    std_triangular_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
    mean_beta_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
    std_beta_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)

    # Iterate through each cell in the DataFrame to compute statistical values
    for i in df_opt.index:
        for j in df_opt.columns:
            a, m, b = df_opt.loc[i, j], df_most.loc[i, j], df_pess.loc[i, j]
            mean_tri, std_tri, mean_beta, std_beta = compute_statistics(a, m, b)

            # Store computed values in corresponding DataFrames
            mean_triangular_df.loc[i, j] = mean_tri
            std_triangular_df.loc[i, j] = std_tri
            mean_beta_df.loc[i, j] = mean_beta
            std_beta_df.loc[i, j] = std_beta

    # Save results into an Excel file with multiple sheets
    with pd.ExcelWriter(output_file_name) as writer:
        mean_triangular_df.to_excel(writer, sheet_name="Mean_Triangular")
        std_triangular_df.to_excel(writer, sheet_name="Std_Triangular")
        mean_beta_df.to_excel(writer, sheet_name="Mean_Beta")
        std_beta_df.to_excel(writer, sheet_name="Std_Beta")

    print(f"Computation complete! Results saved in '{output_file_name}'.")

    return df_opt, df_most, df_pess

if __name__ == "__main__":

    # Example of processing data for day 1 - You can update this part accordingly to process data in your desires way
    file_optimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_optimistic_1.xlsx"
    file_most_likely = "extracted_data/time_and_distance_matrices/day_1/time_matrix_mostlikely_1.xlsx"
    file_pessimistic = "extracted_data/time_and_distance_matrices/day_1/time_matrix_pessimistic_1.xlsx"

    load_and_process(file_optimistic, file_most_likely, file_pessimistic)
