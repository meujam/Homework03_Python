# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
totalrev = 0
count = 0
csvpath = os.path.join('..', 'Homework#3', 'Resources', 'budget_data.csv')





f = open(csvpath, "r")

#bring in file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)

	
#create lists 	
	revenue = []
	date = []
	rev_change = []
	
#create loop of csv file and retrieve total months and total revenue
	for row in csvreader:

		revenue.append(float(row[1]))
		date.append(row[0])
		len(date)
		sum(revenue)
	print("Financial Analysis")
	print("-----------------------------------")
	print("Total Months:", len(date))
	print("Total Revenue: $", round(sum(revenue),))


 #create addtioanl loop to calculate the average change, greatest increase and greatest decrease 
	for i in range(1,len(revenue)):
		rev_change.append(revenue[i] - revenue[i-1])   
		avg_rev_change = float(sum(rev_change)/len(rev_change))

		max_rev_change = round(max(rev_change))
		min_rev_change = round(min(rev_change))

		max_rev_change_date = str(date[rev_change.index(max(rev_change))])
		min_rev_change_date = str(date[rev_change.index(min(rev_change))])


	print("Avereage Change: $", round(avg_rev_change,2))
	print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
	print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
	
output_path = os.path.join('..', 'Homework#3', 'Resources', 'new.csv')	
	
	
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
	csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
	csvwriter.writerow("Financial Analysis")
	csvwriter.writerow("-----------------------------------")
	csvwriter.writerow("Total Months:", len(date))
	csvwriter.writerow("Total Revenue: $", round(sum(revenue),))
	csvwriter.writerow("Avereage Change: $", round(avg_rev_change,2))
	csvwriter.writerow("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
	csvwriter.writerow("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
	
	

	




