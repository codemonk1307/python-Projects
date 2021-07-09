

# placce your csv file in the same folder location where code is written

# importing the required csv module
import csv 

with open("file.csv") as file:
    content = csv.reader(file)
    for row in content:
        print(row)


# Output format will be as follows
# ["index", "key", "value"]