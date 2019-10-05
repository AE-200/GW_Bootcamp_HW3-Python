# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:39:22 2019

@author: Andre
"""

import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])
    
        # Add amount of reviews
        reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        round(((float(row[6])/float(row[5]))*100),2)
        review_percent.append(round(((float(row[6])/float(row[5]))*100),2))
        
        charactercount=0
        # Get length of the course to just a number
        for character in row[9]:
            if character==" ":
                charactercount=0
            else:
                charactercount=charactercount+1
                
        length.append(charactercount)

# Zip lists together

zipTuple = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    for items in zipTuple:
        writer.writerow(items)
