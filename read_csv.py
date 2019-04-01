# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
count = -1
count1 = -1
count2 = -1
count3 = -1
# Module for reading CSV files
import csv

csvpath = os.path.join('..','homework#3', 'PyPoll', 'Resources', 'election_data.csv')


f = open(csvpath, "r")

# # Method 1: Plain Reading of CSV files
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	
	candidate = ['Khan', 'Correy', 'Li', 'O'Tooley']

	
	
	
	for row in csvreader:
		

		candidate.append(row[2])
		count = candidate.count('Khan')
		count1 = candidate.count('Correy')
		count2 = candidate.count('Li')
		count3 = candidate.count('O'Tooley')
		total = candidate.count('Khan') + candidate.count('Correy') + candidate.count('Li')
		khan = count/ total * 100
		correy = count1/ total * 100
		li = count2/ total * 100
		
		
		
	print (count1)
	print (count)
	print (count2)
	print (count3)
		
	print (khan)
	print (li)
	print (correy)
	

	
