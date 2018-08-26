man = []
other = []

try:
  with open('sketch.txt') as data:
    for each_line in data:
      try:
        (role, line_spoken) = each_line.split(':', 1)
        line_spoken = line_spoken.strip()
        if role == 'Man':
          man.append(line_spoken)
        elif role == 'Other Man':
          other.append(line_spoken)
      except ValueError:
        pass
except IOError as err:
  print('File error: ' + str(err))

try:
  with open('man_data_with.txt', 'w') as man_file:
    print(man, file=man_file)
  with open('other_data_with.txt', 'w') as other_file:
    print(other, file=other_file)
except IOError as err:
  print('File error: ' + str(err))
