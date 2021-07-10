

import json
with open("file.json") as file:
    content = json.load(file)

# we can get the values of each json object by this query  -->  content.get("user-field")

# either generate a query manually
print(content.get("text-id"))

# or we can simply loop through each field of the huge json datasets containing javascript objects
for fields in content:
    print(content.get(fields))



# copy the JSON  Files and place it to the same directory where the code is written