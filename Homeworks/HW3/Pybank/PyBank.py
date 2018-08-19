import os
import csv

# inport csv files
csvpath = os.path.join("..", "resources","budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# Analysis
    months = 0
    total = 0
    max = 0
    min = 0
    max_count = 0
    min_count = 0
    for row in csvreader:
        months = months + 1
        total = total + int(row[1])
        avg = total/months
        avg_change = (int(row[1])-avg)/months
        if int(row[1]) >= max:
            max = int(row[1])
            max_count = row[0]
        if int(row[1]) <= min:
            min = int(row[1])
            min_count = row[0]

# make dictionary
    x = ["Total Months", "Total", "Average Change", "Greatest Increase", "Greatest Decrease"]
    y = [months, total, avg_change, [max_count, max], [min_count, min]]
    dic = dict(zip(x,y))
    print("Financial Analysis\n---------------------")
    for x,y in dic.items():
        print (x + ":", y)
#output csv files
output_file = os.path.join("Python_solved.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    for x, y in dic.items():
        writer.writerow([x,y])
