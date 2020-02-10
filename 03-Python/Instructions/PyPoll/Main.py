import csv
import os

# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resources', 'election-data.csv')

#Calculate total number of votes cast
election_data = election_csv
print(len(election_data)) - 1


#Calculate percentage of votes for each candidate
def print_percentages(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    voter_id = str(election_data[0])
    County = str(election_data[1])
    Candidate = str(election_data[2])

    # Total votes can be found by counting voter_id
    total_votes = len(voter_id)

    #List of Candidates who received votes


    





