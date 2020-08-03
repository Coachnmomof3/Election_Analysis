#Add our depencdencies.
import csv
import os

#Assign a variable for the file to load and the path. 
#file_to_load = "C:\Users\coach\Desktop\School\MyRepo\work\Election_Analysis\Resources\election_results.csv"
file_to_load = os.path.join("Resources","election_results.csv")
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
file_to_save = os.path.join("analysis", "election_analysis.txt")

# not Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
#Using the with statement open the file as a text file.
# Open the election results and read the file.
with open(file_to_load) as election_data:
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
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
    #for row in file_reader:
               #print(row)
         # Print the header row.
    headers = next(file_reader)
    print(headers)
# Close the file
#outfile.close()