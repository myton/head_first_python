def sanitize (time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return time_string
  (mins, secs) = time_string.split(splitter)
  return (mins + '.' +secs)

def pross_data(file_name):
  try:
    with open(file_name, 'r') as data:
      _data = (data.readline().strip().split(','))
      (name, dob) = _data.pop(0), _data.pop(0)
      return (name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in _data]))[0:3]))
  except IOError as err:
    print("file is missing :" + err)
    return (None)

print(pross_data('james2.txt'))
print(pross_data('julie2.txt'))
print(pross_data('mikey2.txt'))
print(pross_data('sarah2.txt'))


