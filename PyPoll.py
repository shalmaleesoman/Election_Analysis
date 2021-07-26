# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module
import datetime
# Use the now() attribute on the datetime class to get present time. 
now = datetime.datetime.now()
# Print the present time
print("The time right now is " , now)

import csv
import os 

# Assign a variable for the file to load and the path. 
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file. 
with open(file_to_load) as election_data:

    #To do: perform analysis
    print(election_data)
# Close the file.
election_data.close()

import csv
import os
# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file. 
with open(file_to_load) as election_data:

    print(election_data)
#Close the file. 
election_data.close()

# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "wow" mode we will write the data to the file.
open(file_to_save, "w") 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
# write three counties to the file
    txt_file.write("Counties in the election\n-----------------\nArapahoe\nDenver\nJefferson")


import csv
import os
# Assign a vatriable for the file to load and the path. 
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. initialize a total vote counter.
total_votes = 0

# Candidate options
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next (file_reader)

    #Print each row in the CVS file.
    for row in file_reader:
        #2. Add the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row [2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
# Print the candidate list
print(candidate_options)

# Close the file
election_data.close()

#3.5.3
#add our dependencies
import csv
import os 
#Assign a varable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initiialize a total vote counter
total_votes = 0 


# candidate options and candidate votes
candidate_options = []
# 1 . declare the empty dictionary.
candidate_votes = {}

# open the election results and read the file.
# Winning candidate and winning count tracker 
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file. 
    for row in file_reader:
        # Add the total vote count
        total_votes += 1

        #Print the candidate name for each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2. begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1

 # Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # . Retreive vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. print the candidate name and percentage of votes. 
    
    # to do. print out each candidates name, vote count, and % of 
    # votes to the terminal

    #Determine winning vote count and candidate 
    #Determine if the votes is greater and the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count : {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    
        # of true then set winning_count = votes and winning_percentage = 
        # vote_percentage.
winning_count = votes
winning_percentage = vote_percentage
        # and, set the winning_candidate equal to candidate's name.
winning_candidate = candidate_name

# To do: print out the winning candidate, vote count and percentage to
# votes  to the terminal
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")





#Close the file 
election_data.close()


# Print the candidate vote dictionary
print(candidate_votes)
