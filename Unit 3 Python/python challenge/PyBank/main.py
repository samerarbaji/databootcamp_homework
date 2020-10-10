import csv
import os

budgetdata= os.path.join("Resources","PyBankdata.csv")

dataset= []
totalmonths=[]
totalrev=[]

with open(budgetdata,'r') as input_file:
    csv_reader = csv.reader(input_file, delimiter = ",")
    row= next(csv_reader)
       
    for row in csv_reader:
        #print(row)
        dataset.append(row)
        totalmonths.append(row[0])
        totalrev.append(int(row[1]))

total_months= len(totalmonths)

nettotal=0
for row in dataset:
    nettotal += int(row[1])

changeamount = 0                                              
monthlychange = []                                           
for amount in range(1,len(totalrev)):         
  
    monthlychange.append(totalrev[amount] - totalrev[amount-1])

changeamount = round(sum(monthlychange) / len(monthlychange),2) 

for amount in range(1,len(totalrev)):
    maxincrease= max(monthlychange)
    maxindex= monthlychange.index(maxincrease)
    maxdecrease= min(monthlychange)
    maxdecreaseindex= monthlychange.index(maxdecrease)

monthlymaxincrease= totalmonths[maxindex + 1]
monthlymaxdecrease= totalmonths[maxdecreaseindex + 1]


    

print("Financial Analysis")
print("-----------------------")
print(f"Total months: {total_months}")
print(f"Net Total: ${nettotal}")
print(f"Average Change: ${changeamount}")
print(f"Greatest Increase in Profits: {monthlymaxincrease} (${maxincrease})")
print(f"Greatest Decrease in Profits: {monthlymaxdecrease} (${maxdecrease})")

outputfile = open("pyBankdata.txt", 'w')
outputfile.write("Financial Analysis\n")
outputfile.write(f"------------------------\n") 
outputfile.write(f"Total Months: {total_months}\n")
outputfile.write(f"Total: ${nettotal}\n")
outputfile.write(f"Average Change: ${changeamount}\n")
outputfile.write(f"Greatest Increase in Profits: {monthlymaxincrease} (${maxincrease})\n")
outputfile.write(f"Greatest Decrease in Profits: {monthlymaxdecrease} (${maxdecrease})\n")