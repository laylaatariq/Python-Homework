# improting generic file path
import os

# improt for reading csv file
import csv


# Defining the path where the file is saved
csv_path = os.path.join('Resources', 'budget_data.csv')

#Declated variables
line_count = 0
Total = 0
prev = 0
change_list = []
initial_change = 0
max = 0
min = 2000000

# Reading the file and ouputting the contents on the command line
with open(csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)


    # Printing the contents of the file on the command line
    csv_header = next(csv_reader)

    #For loop to go over the rest of the file
    for row in csv_reader:
        
        #Counting the total number of months in the file
        line_count += 1

        #Reading in the Profit/Losses Column
        pl = row[1]

        #Calculating the Sum of Profit/Losses Column
        Total += int(pl)

        #Finding the change in the profit and losses and storing into a list
        #to further find the average
        change = int(pl) - int(prev)
        prev = row[1]
        #print(f"Change is {change}")
        #print(f"prev is  {prev}")
        if(int(change) != int(prev)):
            change_list = change_list + [change]
            

        #Finding the max increase
        if(change > int(max)):
            max = change
            gdate = row[0]

        #Finding the min decrease
        if(change < min):
            min = change
            d_date = row[0]


    #Calculating the average change of profit and losses
    average = round((sum(change_list) /len(change_list)), 2)

    #Printing data on to the command line
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total Months: {line_count}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {gdate} $({max})")
    print(f"Greatest Decrease in Profits: {d_date} $({min})")
    print("---------------------------------------------------")

    #Writing the result to a file
    output_path = "out.txt"

    with open(output_path, "w") as text_file:
       
        #filewriter = text_file.writelines(text_file, delimiter='')

        #Writing contents to the file
        text_file.writelines("Financial Analysis\n")
        text_file.writelines("---------------------------------------------------\n")
        text_file.write(f"Total Months: {line_count}\n")
        text_file.write(f"Total: ${Total}\n")
        text_file.write(f"Average Change: ${average}\n")
        text_file.write(f"Greatest Increase in Profits: {gdate} $({max})\n")
        text_file.write(f"Greatest Decrease in Profits: {d_date} $({min})\n")
        text_file.write("---------------------------------------------------")