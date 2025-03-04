import pandas as pd
import numpy as np

# Load Excel files (update filenames as needed)
file_optimistic = "C:/Users/annav/OneDrive/Υπολογιστής/time and distance matrices/day_1/time_matrix_optimistic_1.xlsx"
file_most_likely = "C:/Users/annav/OneDrive/Υπολογιστής/time and distance matrices/day_1/time_matrix_mostlikely_1.xlsx"
file_pessimistic = "C:/Users/annav/OneDrive/Υπολογιστής/time and distance matrices/day_1/time_matrix_pessimistic_1.xlsx"

df_opt = pd.read_excel(file_optimistic, index_col=0)
df_most = pd.read_excel(file_most_likely, index_col=0)
df_pess = pd.read_excel(file_pessimistic, index_col=0)

# Ensure all dataframes have the same shape
assert df_opt.shape == df_most.shape == df_pess.shape, "Mismatch in data dimensions!"

# Compute Mean and Standard Deviation for Triangular and Beta (PERT) Distributions
def compute_statistics(a, m, b):
    # Mean Calculation
    mean_triangular = round((a + m + b) / 3, 2)
    mean_beta = round((a + 4*m + b) / 6, 2)  # PERT gives more weight to most likely

    # Standard Deviation Calculation
    std_triangular = round((b - a) / np.sqrt(24), 2)
    std_beta = round((b - a) / 6, 2)

    return mean_triangular, std_triangular, mean_beta, std_beta

# Create a new DataFrame to store results
results = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)

# Compute statistics for each route
mean_triangular_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
std_triangular_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
mean_beta_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)
std_beta_df = pd.DataFrame(index=df_opt.index, columns=df_opt.columns)

for i in df_opt.index:
    for j in df_opt.columns:
        a, m, b = df_opt.loc[i, j], df_most.loc[i, j], df_pess.loc[i, j]
        mean_tri, std_tri, mean_beta, std_beta = compute_statistics(a, m, b)

        mean_triangular_df.loc[i, j] = mean_tri
        std_triangular_df.loc[i, j] = std_tri
        mean_beta_df.loc[i, j] = mean_beta
        std_beta_df.loc[i, j] = std_beta

# Save results to an Excel file
with pd.ExcelWriter("computed_results.xlsx") as writer:
    mean_triangular_df.to_excel(writer, sheet_name="Mean_Triangular")
    std_triangular_df.to_excel(writer, sheet_name="Std_Triangular")
    mean_beta_df.to_excel(writer, sheet_name="Mean_Beta")
    std_beta_df.to_excel(writer, sheet_name="Std_Beta")

print("Computation complete! Results saved in 'computed_results.xlsx'.")
