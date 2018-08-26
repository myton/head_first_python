def sanitize (time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return time_string
  (mins, secs) = time_string.split(splitter)
  return (mins + '.' +secs)

def pross_data(file_name, name):
  try:
    with open(file_name, 'r') as data:
      line = data.readline().strip().split(',')
      for item in line:
        name.append(sanitize(item))
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

print("==========sorted(data) default: 升序=======")
print("sorted(julie): ", sorted(julie))
print("sorted(james): ", sorted(james))
print('sorted(mikey): ', sorted(mikey))
print('sorted(sarah): ', sorted(sarah))

print("==========sorted(data, reverse = True) 降序=======")
print("sorted(julie): ", sorted(julie, reverse=True))
print("sorted(james): ", sorted(james, reverse=True))
print('sorted(mikey): ', sorted(mikey, reverse=True))
print('sorted(sarah): ', sorted(sarah, reverse=True))
