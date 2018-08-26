def pross_data(file_name, name):
  try:
    with open(file_name, 'r') as data:
      line = data.readline().strip().split(',')
      for item in line:
        name.append(item)
  except IOError as err:
    print("file is missing :" + err)

julie = []
james = []
mikey = []
sarah = []

pross_data("julie.txt", julie)
pross_data("james.txt", james)
pross_data("mikey.txt", mikey)
pross_data("sarah.txt", sarah)

print("==========source data========")
print("julie: ", julie)
print("james: ", james)
print('mikey: ', mikey)
print('sarah: ',  sarah)

print("==========sorted(data)=======")
print("sorted(julie): ", sorted(julie))
print("sorted(james): ", sorted(james))
print('sorted(mikey): ', sorted(mikey))
print('sorted(sarah): ', sorted(sarah))
