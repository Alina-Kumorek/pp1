# In any text editor, create a text file students.txt containing the following data in CSV format:

#     first_name,last_name,age,gender,email
#     Decca,Blackstone,52,Male,dblackstone0@time.com
#     Elena,Rechert,27,Female,erechert1@ucoz.com
#     Bibbye,Norree,26,Female,bnorree2@reddit.com
#     Alasdair,McCoole,53,Male,amccoole3@foxnews.com
#     Hogan,Hatrey,26,Male,hhatrey4@zimbio.com

# Then create a program that reads data from the CSV file and displays the first name,
# last name and email address of students under 30. Format the data as below. Sample result:

#     Elena   Rechert  erechert1@ucoz.com
#     Bibbye  Norree   bnorree2@reddit.com
#     Hogan   Hatrey   hhatrey4@zimbio.com

# Tip: import and use csv module. 

import csv

with open("students.txt", newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        if int(row["age"]) < 30:
            print(row["first_name"], row["last_name"], row["email"], sep="\t")