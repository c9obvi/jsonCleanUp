import json

rawData = []
with open("____.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

id = jsonObject['rows']

print(type(id))
print(type(id[1]))
print((id[1]))

#for x in id:
#  print(x)
#this writes out the entire list of dictionaries
#with open('organized.csv', 'w') as f:
#  for x in id:
#    str_x = repr(x)
#    f.write(str_x + "\n")

#this get the ID key value only & adds comma/moves to next row
with open('ID_only_.csv', 'w') as f:
 for x in id:
  f.write(x['id'] + ", \n")


# code above works now I need to
# parse the CSV
# seperate ID and Date?
# CSV of ID, Date \n ?


#print(id.keys)

# for i in id write ammend to a file .csv
