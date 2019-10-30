#Importing libraries
import os
import csv

#Defininf the path of the file
csv_path = os.path.join('Resources', 'employee_data.csv')

#Declared variables
emp_ID = []
first_name = []
last_name = []
date_of_birth = []
ssn = []
state_abbrev = []

#Got the dictionary from https://gist.github.com/rogerallen/1583593
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Opening the file to read contents
with open(csv_path, newline ='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    #Going through the whole file
    for row in csv_reader:

        #Getting employee ID's
        emp_ID.append(row[0])

        #Splitting employee name in first and last
        new_name = row[1].split(" ")
        first_name.append(new_name[0])
        last_name.append(new_name[1])

        #Changing date format
        date = row[2].split("-")
        new_date = date[2] + "/" + date[1] + "/" + date[0]
        date_of_birth.append(new_date)

        #Changing the ssn format
        social = row[3].split("-")
        new_ssn = "***-**-" + social[2]
        ssn.append(new_ssn)

        #Getting the state abbreviation
        #Got help from https://www.w3schools.com/python/python_dictionaries.asp
        #On how to work with dictionaries
        state = row[4]
        abbrev = us_state_abbrev[state]
        state_abbrev.append(abbrev)

#Adding all the cleaned data into a tupple through zip
cleaned_data = zip(emp_ID, first_name, last_name, date_of_birth, ssn, state_abbrev)
#Path for ouput file
output_file = os.path.join('converted_data.csv')

#Opening the file to output data
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Writing header to the file
    writer.writerow(["Emp ID", "First Name", "Last Name", 
    "DOB", "SSN", "State"])

    #Writing the cleaned data to the output file
    for i in cleaned_data:
        writer.writerows(cleaned_data)