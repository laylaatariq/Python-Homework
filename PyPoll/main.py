#Importing generic file path and for reading csv file
import os
import csv

#Defininf the path where the file is located
csv_path = os.path.join('Resources','election_data.csv')

#Declaring variables
totalVotes = 0
all_names = []
can1_total_votes = 0
can2_total_votes = 0
can3_total_votes = 0
can4_total_votes = 0
all_votes = []

#Reading the file
with open(csv_path, newline='') as csvfile:
   
   #Reading the file header
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)

    #Loop to go over the file
    for row in csv_reader:

        #Counting the total number of votes
        totalVotes +=1

        #Getting the names
        name = row[2]

        #Checking to see if the previous name matches the next one
        #Got this code from :https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/
        if((any(name in sublist for sublist in all_names)) == False):
            all_names = all_names + [name]

        #Calculating total votes for each player
        if(name == all_names[0]):
            can1_total_votes += 1
            can1 = all_names[0]
        elif(name == all_names[1]):
            can2_total_votes += 1
            can2 = all_names[1]
        elif(name == all_names[2]):
            can3_total_votes += 1
            can3 = all_names[2]
        else:
            can4_total_votes += 1
            can4 = all_names[3]
    
    #Adding all votes to a list for further calculations
    all_votes = all_votes + [can1_total_votes]
    all_votes = all_votes + [can2_total_votes]
    all_votes = all_votes + [can3_total_votes]
    all_votes = all_votes + [can4_total_votes]

    #Finding the max in the list
    #Got this code from: https://www.geeksforgeeks.org/python-maximum-minimum-elements-position-list/
    Max = max(all_votes)
    maxpos = all_votes.index(Max)

    #Getting the name of the candidate with max votes
    winner = all_names[maxpos]

    #Calculating the total percentage for each candidate
    perc_can1 = round((can1_total_votes/totalVotes)*100, 4)
    perc_can2 = round((can2_total_votes/totalVotes)*100, 4)
    perc_can3 = round((can3_total_votes/totalVotes)*100, 4)
    perc_can4 = round((can4_total_votes/totalVotes)*100, 4)



print(f"Total number of votes {totalVotes}")
print(f"Names are {all_names}")
print(f"All votes are {all_votes}")
print(f"Can 1 is {can1} with total votes:{perc_can1} ({can1_total_votes})")
print(f"Can 2 is {can2} with total votes: {perc_can2} ({can2_total_votes})")
print(f"Can 3 is {can3} with total votes: {perc_can3} ({can3_total_votes})")
print(f"Can 4 is {can4} with total votes: {perc_can4} ({can4_total_votes})")
print(f"max at {maxpos}")
print(f"Winner is {winner}")
