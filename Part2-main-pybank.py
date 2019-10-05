# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:16:34 2019

@author: Andre
"""

# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os
import pandas as pd
from statistics import mean

# Files to load and output (Remember to change these)
#file_to_load = os.path.join("budget_data.csv")
#file_to_output = os.path.join("budget_analysis.txt")

file_to_load = ("budget_data.csv")
df=pd.read_csv("budget_data.csv", encoding='UTF-8')


# Track various financial parameters

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

def file_length(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    # Read the header row
    header = next(reader)
       
    #number_lines = sum(1 for row in reader)
    # Extract first row to avoid appending to net_change_list
    # YOUR CODE HERE
    first_row = next(reader)
    total_months=total_months+1
    total_net = total_net + int(first_row[1])
    prev_net=int(first_row[1])




    for row in reader:

        # Track the total
        total_months=total_months+1
        total_net = total_net+int(row[1])
        netchange=int(row[1]) - prev_net
        prev_net=int(row[1])
        net_change_list.append(netchange)
        month_of_change=month_of_change+[row[0]]
 
    
        # Calculate the greatest increase
    
    greatest_increase[1]=max(net_change_list)
    month_increase=net_change_list.index(max(net_change_list))
    greatest_increase[0]=month_of_change[month_increase]
            
        # Calculate the greatest decrease
    greatest_decrease[1]=min(net_change_list)
    month_decrease=net_change_list.index(min(net_change_list))
    greatest_decrease[0]=month_of_change[month_decrease]
            
# Calculate the Average Net Change
    net_monthly_avg=mean(net_change_list)
    
#average_net_change = df["Profits/Losses"].apply(lambda x: x.diff().mean())
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(f'{output}')

# Export the results to text file
file_to_output =("budget_analysis.txt")

#  Open the output file
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits",
                      "Greatest Decrease in Profits"])
    #output_rows=['{total_months}', '{total_net}, {net_monthly_avg}, {greatest_increase[0]} (${greatest_increase[1]}),{greatest_decrease[0]} (${greatest_decrease[1]})]

    # writing the items to the output file
    
    writer.writerow('{total_months}' '{total_net}' '{net_monthly_avg}' '{greatest_increase[0]}' '(${greatest_increase[1]})' '{greatest_decrease[0]}' '(${greatest_decrease[1]})')
