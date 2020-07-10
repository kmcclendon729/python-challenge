
# import os (for the filepath) and csv (to open and read the resource file)
import os
import csv

# define variables for items I need to count:
total_months = 0
total_profit = 0
prior_month = []
mo_change = []
months = []

# open budget_data.csv
budget_data = os.path.join('Resources', 'budget_data.csv')
with open(budget_data) as csvfile:
    budgetData = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    # loop through the rows in the csv file and count:
    for row in budgetData:

        #count rows of the Date column in the budget)data csv file
        total_months += 1
        
        #sum profit/losses in the budget_data file
        total_profit = total_profit + int(row[1])

        #calculate the monthly change
        if total_months > 1:
            mo_change.append(int(row[1])-int(prior_month[1]))
            months.append(row[0])

        #save information into variable
        prior_month = row

#find average of monthly change calculated above (need to round to two decimals)
avg_mo_change = round(sum(mo_change)/len(mo_change),2)

 #need to know which row min/max were found in so we can find the date for that row
max_incr = max(mo_change)
max_mo = months[mo_change.index(max_incr)]

max_decr = min(mo_change)
min_mo = months[mo_change.index(max_decr)]      


#print analysis to the terminal
print(total_months)
print(total_profit)
print(avg_mo_change)
print(max_incr)
print(max_mo)
print(max_decr)
print(min_mo)

# specify where to output a new text file containing the results
output_file = os.path.join("Analysis", "budget_analysis.txt")

# Open a text file using "write" mode
with open(output_file, "w") as txtfile:
    
    # Write the results from the above analysis
   
    txtfile.write(f"Financial Analysis\n------------------\nTotal Months: {total_months}\nTotal Profit: ${total_profit}\nAverage Change: ${avg_mo_change}\nGreatest Increase in Profits: {max_mo} (${max_incr})\nGreatest Decrease in Profits: {min_mo} (${max_decr})")
   
 # print results to terminal  
print(f"Financial Analysis\n------------------\nTotal Months: {total_months}\nTotal Profit: ${total_profit}\nAverage Change: ${avg_mo_change}\nGreatest Increase in Profits: {max_mo} (${max_incr})\nGreatest Decrease in Profits: {min_mo} (${max_decr})")
