import os
import csv

input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_analysis.txt")

total_votes = 0


with open(input_path) as infile:
    reader = csv.reader(infile)

    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1


output=(
    f"Election Results\n"
    f"-------------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------------------------\n"
)
print(output)

with open(output_path, "w") as outfile:
    outfile.write(output)


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
