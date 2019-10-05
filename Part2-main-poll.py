# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:25:40 2019

@author: Andre
"""

#coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    votecount=0
    # For each row...
    for row in reader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]
        votecount=0
        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)           

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name]=0
                
        # Then add a vote to that candidate's count
        votecount=votecount+1
        if candidate_name in candidate_options:
            candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    print('ELECTION RESULTS        ')
    print('------------------------')
    print(f'Total Votes   {total_votes}')
    

    # Save the final vote count to the text file
    # YOUR CODE HERE
                
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        winning_count=max(candidate_votes.values())
        winning_candidate=[candidate for candidate, vote in candidate_votes.items() if vote ==winning_count]
        
        # Print each candidate's voter count and percentage (to terminal)
        print(f'{candidate}  {vote_percentage} ({votes})')
                
        file_to_output =("budget_analysis.txt")

#  Open the output file
        with open(file_to_output, "w", newline="") as datafile:
            writer = csv.writer(datafile)

    # Write the header row
            writer.writerow(["Candidates", "Vote Percentage", "Votes"])
    #write the vote perecentages of each candidate to the text file    
            writer.writerow({candidate}, {vote_percentage} {votes})
    

          

    # Print the winning candidate (to terminal)
    print(f'WINNER {winning_candidate}')

    # Save the winning candidate's name to the text file
    writer.writerow("The winning candidate is" {winning_candidate})
