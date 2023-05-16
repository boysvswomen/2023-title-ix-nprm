import csv
import random

# Select sample size
n = 1000

# Specify the input and output filenames
input_filename = "lho-qdbp-rvml.csv"
output_filename = "lho-qdbp-rvml_{}_random_rows.csv".format(n)

# Add a column before the first column called "Row Number"
with open(input_filename, 'r') as file:
    csv_reader = csv.reader(file)
    header_row = next(csv_reader)  # Read the header row
    rows = [[i] + row for i, row in enumerate(csv_reader, start=1)]

# New columns need to be added before the Comment column to label the comments
new_columns = ["Supports/Not Far Enough", "Opposes Rule", "Unknown"]
comment_col_index = header_row.index("Comment")

# Insert new header columns
for new_column in reversed(new_columns):
    header_row.insert(comment_col_index, new_column)

# Insert new columns to the other rows
for row in rows[1:]:
    for col in reversed(new_columns):
        row.insert(comment_col_index, "")

# Select n rows at random using 0 as a seed
random.seed(0)
random_rows = random.sample(rows, n)

# Write the selected rows to a new CSV file
with open(output_filename, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Row Number'] + header_row)  # Write the header row, adding the new Row Number column
    csv_writer.writerows(random_rows)