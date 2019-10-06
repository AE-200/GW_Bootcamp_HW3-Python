# -*- coding: utf-8 -*-

import os
import csv

filepath = os.path.join("employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name=row['first_name']
        last_name=row['last_name']
        emailaddr=f"{first_name}.{last_name}@example.com"
        
        
        new_employee_data.append(
        {
                "first_name" : row['first_name'],
                "last_name": row['last_name'],
                "email": emailaddr,
                "ssn" : row['ssn']        
        }
        
        )
print(new_employee_data)
# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csvfile
csvpath = os.path.join("updatedfile.csv")
with open(csvpath, "w") as csvfile:
     column_names=['first_name','last_name','email', 'ssn']
     writer = csvDictWriter(csvfile,column_names=column_names)
     writer.writeheader('First Name', 'Last Name', 'Email', 'SSN')
     for row in writer:
         writer.writerow(new_employee_data[row])
         
