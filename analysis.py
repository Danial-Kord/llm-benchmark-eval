import pandas as pd

import matplotlib.pyplot as plt



# Load the CSV data
file_path = 'mbpp_0_2025-01-01_07-12-22.csv'


def get_true_means(file_path):
    data = pd.read_csv(file_path)

    # Create new columns for the differences
    data['Cyclomatic Complexity Difference'] = data['Average Cyclomatic Complexity (Mutated)'] - data[
        'Average Cyclomatic Complexity (Original)']
    data['Function Length Difference'] = data['Average Function Length (Mutated)'] - data[
        'Average Function Length (Original)']
    data['Comment Ratio Difference'] = data['Average Comment Ratio (Mutated)'] - data[
        'Average Comment Ratio (Original)']
    data['Naming Compliance Difference'] = data['Average Naming Compliance (Mutated)'] - data[
        'Average Naming Compliance (Original)']

    # Remove the old columns
    columns_to_remove = [
        'Average Cyclomatic Complexity (Mutated)', 'Average Cyclomatic Complexity (Original)',
        'Average Function Length (Mutated)', 'Average Function Length (Original)',
        'Average Comment Ratio (Mutated)', 'Average Comment Ratio (Original)',
        'Average Naming Compliance (Mutated)', 'Average Naming Compliance (Original)',
        'Total Mutants', 'Passed Mutants', 'Pass Percentage'
    ]
    data = data.drop(columns=columns_to_remove)

    # Display the updated DataFrame
    print("Data with Difference Columns (Old Columns Removed):")
    print(data.head())

    # Filter rows where "Failed Patch" is True
    true_rows = data[data['Failed Patch'] == False]

    # Calculate the mean of each numeric column for these rows
    true_means = true_rows.mean(numeric_only=True)

    # Display the results
    print("Mean of numeric columns where 'Failed Patch' is True:")
    print(true_means)
    return true_means


mbpp_means = get_true_means(file_path)



file_path = 'humaneval_0_2025-01-01_06-47-17.csv'
human_eval_means = get_true_means(file_path)


# Function to create a transposed table plot with 2 decimal point precision
def create_transposed_means_table_rounded(mbpp_means, human_eval_means):
    # Combine the means into a single DataFrame for visualization
    combined_means = pd.DataFrame({
        'MBPP': mbpp_means.round(2),
        'HumanEval': human_eval_means.round(2)
    })

    # Transpose the DataFrame for reversed rows and columns
    transposed_means = combined_means.transpose()
    transposed_means.columns.name = "Metric"  # Set column name for clarity

    # Reset the index for a clean display in the table
    transposed_means.reset_index(inplace=True)
    transposed_means.rename(columns={'index': 'Dataset'}, inplace=True)

    # Create a table plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=transposed_means.values,
                     colLabels=transposed_means.columns,
                     cellLoc='center',
                     loc='center',
                     colLoc='center')

    # Adjust table formatting
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.auto_set_column_width(col=list(range(len(transposed_means.columns))))

    # Show the plot
    plt.title("Benchmark Mutation Testing Evaluation", fontsize=14, weight='bold')
    plt.savefig("./statistics_table.png")
    plt.show()

# Assuming mbpp_means and human_eval_means are already calculated
create_transposed_means_table_rounded(mbpp_means, human_eval_means)

