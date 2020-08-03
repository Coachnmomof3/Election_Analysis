#Add our depencdencies.
#import csv
#import os

#Assign a variable for the file to load and the path. 
#file_to_load = "C:\Users\coach\Desktop\School\MyRepo\work\Election_Analysis\Resources\election_results.csv"
#file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file.
#Election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:

    #To do: perform analysis.
    #print(election_data) 

#Close the file.
#election_data.close()

        #Print the file object.
        #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Assign a variable to save the file to a path.
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# not Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
#Using the with statement open the file as a text file.
# Open the election results and read the file.
#with open(file_to_load) as election_data:
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #outfile.write("Hello World")
    #txt_file.write("Hello World")
    #Write three counties to the file
    #txt_file.write("Arapahoe,")
    #txt_file.write("Denver,")
    #txt_file.write("Jefferson")
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #Write three counties to the file on different lines.
    #txt_file.write("Arapahoe\nDenver\nJeferson")
    #Write header and three counties on different lines.
    #txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJeferson")
    #txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJeferson")
    # To do: read and analyze the data here
    # Read the file object with the reader function.
#    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
    #Read the header row.
  #  headers = next(file_reader)
    #for row in file_reader:
               #print(row)
         # Print the header row.
    

    #Print each row in the CSV file.
 #        print(row)

    #print(headers)
# Close the file
#outfile.close()

# Add our dependencies.
import csv
import os
 # Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes +=1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate namer to the candidate list.
            candidate_options.append(candidate_name)
            
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    
#  To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = (votes) / (total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")    
    # Print the candidate list.
    #print(candidate_votes)
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if votes > winning_count and vote_percentage > winning_percentage:
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")    
        # Print the candidate list.
        #print(candidate_votes)
    #  To do: print out the winning candidate, vote count and percentage to
    # votes to terminal.
    #winning_candidate_summary = -------------------------\nWinner: = winning_candidate \nWinning Vote Count: = winning_count:,\nWinning Percentage: = winning_percentage %\n-------------------------\n"
        winning_candidate_summary = (f"-------------------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}%\n-------------------------\n")
print(winning_candidate_summary)

 
