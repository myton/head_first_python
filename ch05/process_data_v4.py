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
def unique_three_times(times):
  fast_three_times = []
  for t in times:
    if t not in fast_three_times:
      fast_three_times.append(t)
  return fast_three_times[0:3]

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


print("=========原地排序========")
julie.sort()
james.sort()
mikey.sort()
sarah.sort()
print("julie: ", julie)
print("james: ", james)
print('mikey: ', mikey)
print('sarah: ',  sarah)

print("==========最快的前３不重复的时间=======")
print("julie: ", unique_three_times(julie))
print("james: ", unique_three_times(james))
print("mikey: ", unique_three_times(mikey))
print("sarah: ", unique_three_times(sarah))

