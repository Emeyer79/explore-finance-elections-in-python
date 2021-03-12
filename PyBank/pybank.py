

# Directions-------------------------------------------------------------------

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# 1: import the os and csv
import os
import csv

# 2: Create the csv path and view columns
pybnk_csv = os.path.join('budget_data.csv')
with open(pybnk_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    print(f"Header: {header}")

    # 3: Create placeholders for each element in empty list
    date = []
    profit = []
    profit_change = []
                     
    # 4: Create loop and go through 
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
    
                      
#Create the MAX and MIN add formatting for USD
max_inc = max(profit_change)
min_dec = min(profit_change)
max_inc_f = "${:,.2f}".format(max_inc)
min_dec_f = "${:,.2f}".format(min_dec)
print(max_inc_f)
print(min_dec_f)

#profit formatting and total
sum_profit = sum(profit)
tot_prof_f = "${:,.2f}".format(sum_profit)

#profit change average and  formatting
avg_prof = round(sum(profit_change)/len(profit_change),2)
avg_prof_f = "${:,.2f}".format(avg_prof)


#Index for month increase and decrease
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1


#print the results and format the profit, increases and decreases. MAX and MIN set to strings

print("-----------------------------------------------------------")
print("Financial Analysis Summary")
print("-----------------------------------------------------------")
print(f"Total Months:{len(date)}")
print(f"Total: {tot_prof_f}")
print(f"Average Change: {avg_prof_f}")
print(f"Greatest Increase in Profits: {date[month_increase]} {max_inc_f}")
print(f"Greatest Decrease in Profits: {date[month_decrease]} {min_dec_f}") 
   

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("----------------------------------------------------")
    new.write("\n")
    new.write("Financial Analysis")
    new.write("\n")
    new.write("---------------------------------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(date)}")
    new.write("\n")
    new.write(f"Total: {tot_prof_f}")
    new.write("\n")
    new.write(f"Average Change: {avg_prof_f}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {date[month_increase]} {max_inc_f}")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {date[month_decrease]} {min_dec_f}")