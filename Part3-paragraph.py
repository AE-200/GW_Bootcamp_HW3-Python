# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:26:13 2019

@author: Andre
"""

# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os
from statistics import mean

# Files to load and output (Remember to change these)
file_to_load = os.path.join("paragraph_1.txt")
file_to_output = os.path.join("paragraph_analysis.txt")

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")

# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
print(word_split)
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
for sentence in sentence_split:

    # Calculate the number of words in each sentence and add to the list
    substring=" "
    count=sentence.count(substring)
    words_per_sentence[].append(count+1)

# Calculate the avg word count (per sentence)
average_words_per_sentence= mean(words_per_sentence)
    
# Generate Paragraph Analysis Output
print(f'Paragraph Analysis')
print(f'Approximate Word Count' {word_count})
print(f'Approximate Sentence Count' {sentence_count})
print(f'Average Letter Count' {avg_letter_count})
print(f'Average Sentence Length' {average_words_per_sentence})

# Print all of the results (to terminal)
#YOUR CODE HERE
    
# Save the results to analysis text file
ith open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Approximate Word Count", "Approximate Sentence Count", "Average Letter Count", "Average Sentence Length"])
                      
    #output_rows=['{total_months}', '{total_net}, {net_monthly_avg}, {greatest_increase[0]} (${greatest_increase[1]}),{greatest_decrease[0]} (${greatest_decrease[1]})]

    # writing the items to the output file
    
    writer.writerow([{word_count}, {sentence_count}, {average_letter_count}, {average_words_per_sentence}])
