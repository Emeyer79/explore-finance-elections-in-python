import os
import csv


poll_csv = os.path.join("election_data.csv")


#create empty list for the candidate column
can_col=[]

# Create empty dictionary to record only candidate names
candidates={}

highest=0

# Open file and assign to csvfile object name
with open(poll_csv, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    print(f'Header: {header}')

    for row in csvreader:
        can_col.append(row[2])
        
    # Convert candidates list into dictionary 
    for row in can_col:
        name_key=row
        if name_key not in candidates:
           # insert name_key into dictionary and initialize to 0
            candidates[name_key]=0
        # count the name key inside dictionary
        candidates[name_key]+=1
    print(candidates)
  
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    total_polls=len(can_col)
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {total_polls}")
    print("------------------------------")
    for name in candidates: 
        percent=round((candidates[name]/total_polls)*100)
        print(str(name)+": "+str(percent)+"% "+"("+str(candidates[name])+")")

        if highest < candidates[name]:
            highest=candidates[name]
            winner= name
        #Output to console
    print("------------------------------")
    print(f"Winner: {winner}")

with open('output.txt','w') as text:
    text.write("Election Results\n")
    text.write("------------------------------\n")
    text.write(f"Total Votes: {total_polls}\n")
    text.write("------------------------------\n")
    for name in candidates: 
        percent=round((candidates[name]/total_polls)*100)
        text.write(str(name)+": "+str(percent)+"% "+"("+str(candidates[name])+")\n")

        if highest < candidates[name]:
            highest=candidates[name]
            winner= name
    text.write("------------------------------\n")
    text.write(f"Winner: {winner} + \n")

    
        
   