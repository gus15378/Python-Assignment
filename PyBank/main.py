import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    month = []
    profit = []
    change = []
    
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change.append(profit[i])
        
increase = max(change)
decrease = min(change)

month_increase = change.index(max(change))+1
month_decrease = change.index(min(change))+1

print("Financial Analysis")
print(f"Total Months:{len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})")
print(f"Greatest Increase in Profits: {month[month_decrease]} (${(str(decrease))})")
