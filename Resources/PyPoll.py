# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for the file to load and the path
# Add our dependencies
import csv
import os
#print(dir(os.path))
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Resources", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Write some data to the file.
# Use the open statement to open the file as a text file.
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the election\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: perform analysis
    file_reader = csv.reader(election_data)
    print(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Close the file
election_data.close()

