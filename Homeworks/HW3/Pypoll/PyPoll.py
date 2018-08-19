import os
import csv

# import csvfile
csvpath = os.path.join("..", "resources", "election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# Analysis
    candidates = []
    votes = []
    counter = []
    count = 0
    total = 0
    percent = []
    perct = 0
    winc = 0
    max = 0
    # list with all votes/candidates
    for row in csvreader:
        votes.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
    # number of votes for each candidate
    for c in candidates:
        for v in votes:
            if c in v:
                count = count + 1
        counter.append(count)
        count = 0
    # total votes
    for num in counter:
        total = total +num
    # percentage
    for num in counter:
        perct = num/total
        percent.append(perct)
    # zip
    analysis = zip(candidates,counter,percent)
    #winner
    for row in analysis:
        if row[1] >= max:
            max = row[1]
            winner = row[0]

    # print
    print("Election Results\n-----------------------------")
    print("Total Votes: " + str(total))
    print("-----------------------------")
    for row in analysis:
        print(row)
    print("-----------------------------\nWinner: " + winner)
    print("-----------------------------")



# output
output_file = os.path.join("Python_solved.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["candidates", "counter", "percent"])
    writer.writerows(analysis)
