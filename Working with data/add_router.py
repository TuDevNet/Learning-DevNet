import csv

print("Please enter a new router: ")
hostname = input("What is the hostname? ")
ip = input("What is the ip address? ")
location = input("What is the location? ")

router = [hostname, ip, location]

with open("router_list.csv","a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)