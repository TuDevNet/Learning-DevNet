import csv

with open("d:\Cyber Security\Programming\Python program\Working with data\\router_list.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        ip = row[1]
        location = row[2]
        
    print(f"{device} is in {location.rstrip()} and has IP{ip}.")
        
