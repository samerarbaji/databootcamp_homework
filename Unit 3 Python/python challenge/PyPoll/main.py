import os
import csv

totalvote=0
litotal= 0
khantotal=0
correytotal=0
otooleytotal=0
winningvote=0

pypolldata= os.path.join("Resources","PyPollelectiondata.csv")

with open(pypolldata, 'r') as input_file:
    csvreader= csv.reader(input_file, delimiter=',')
    header=next(csvreader)
    
    for row in csvreader:
        #print(row)
        totalvote +=1
        #print(totalvote)
        if row[2]== "Khan":
            khantotal +=1
        elif row[2]== "Correy":
            correytotal +=1
        elif row[2]== "Li":
            litotal +=1
        elif row[2]== "O'Tooley":
            otooleytotal +=1

candidates = ["Khan", "Correy", "Li","O'tooley"]
votes= [khantotal,correytotal,litotal,otooleytotal]

khanpercent= (khantotal/totalvote) *100
correypercent= (correytotal/totalvote) *100
lipercent= (litotal/totalvote) *100
otooleypercent= (otooleytotal/totalvote) *100

candidates_and_votes = dict(zip(candidates,votes))
winner = max(candidates_and_votes, key=candidates_and_votes.get)


print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {totalvote}")
print(f"----------------------")
print(f"Khan: {khanpercent:.3f}% ({khantotal})")
print(f"Correy: {correypercent:.3f}% ({correytotal})")
print(f"Li: {lipercent:.3f}% ({litotal})")
print(f"Correy: {otooleypercent:.3f}% ({otooleytotal})")
print(f"----------------------")
print(f"WINNER: {winner}")
print(f"----------------------")

file= open("PyPollresults.txt","w") 
file.write(f"Election Results\n")
file.write(f"---------------------\n")
file.write(f"Total Votes: {totalvote}\n")
file.write(f"----------------------\n")
file.write(f"Khan: {khanpercent:.3f}% ({khantotal})\n")
file.write(f"Correy: {correypercent:.3f}% ({correytotal})\n")
file.write(f"Li: {lipercent:.3f}% ({litotal})\n")
file.write(f"Correy: {otooleypercent:.3f}% ({otooleytotal})\n")
file.write(f"----------------------\n")
file.write(f"WINNER: {winner}\n")
file.write(f"----------------------\n")
