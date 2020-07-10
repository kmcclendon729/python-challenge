## Dependencies

import os
from collections import Counter
import csv
import operator
import sys

## tell Python where to find the election_data.csv file

filepath = os.path.join('Resources', 'election_data.csv')

# tell python when to output the new text file containing the results
output_file = os.path.join("Analysis", "election_results.txt")
if os.path.exists(output_file):
  os.remove(output_file)

#open the csv file just long enough to get the information needed

with open(filepath) as csvfile, open(output_file, "a") as txtfile:

    # read the open CSV
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
 
    # create an empty list to hold the total number of votes
    total_votes = []
    
    # loop through rows in csv file and count the votes: in total and by candidate (candidate name, the percentage of total votes they received, and the number of votes they received) 
    print("Election Results")
    print("------------------------")
    txtfile.write(f"Election Results\n------------------------\n")
    for row in csvreader:
        total_votes.append(row[2])
    print("Total votes",len(total_votes))
    print("------------------------")
    txtfile.write(f"Total votes {len(total_votes)}\n------------------------\n")
    candidate_votes = {}
    for vote in total_votes:
      if vote in candidate_votes:
        candidate_votes[vote] += 1
      else:
        candidate_votes[vote] = 1  
    for candidate in candidate_votes:
      if candidate_votes[candidate] >= 1:
        vote_percentage = (candidate_votes[candidate] * 100/len(total_votes))
        winner = max(candidate_votes.items(), key=operator.itemgetter(1))[0]
        print(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})")
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})\n")
    print("------------------------")
    print(f"Winner: {winner} ")
    print("------------------------")
    txtfile.write(f"------------------------\nWinner: {winner}\n------------------------\n")


