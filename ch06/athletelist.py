class AthleteList(list):
  def __init__(self, a_name="", a_dob=None, a_times=[]):
    list.__init__([])
    self.name = a_name
    self.dob = a_dob
    self.extend(a_times)

  def top3(self, fast = 3):
    return (sorted(set([santize(t) for t in self]))[0:fast])
# global function
def santize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return time_string
  (mins, secs) = time_string.split(splitter)
  return (mins + '.' + secs)

def get_coach_data(file_name):
  try:
    with open(file_name, 'r') as file_data:
      data = file_data.readline().strip().split(',')
    (_name, _dob) = data.pop(0), data.pop(0)
    _times = [santize(t) for t in data]
    return AthleteList(_name, _dob, _times)
  except IOError as err:
    print ("file is missing " + str(err))
    return None


james = get_coach_data('james2.txt')
print("======print source data from file======")
print (james)
print('===========add times by append fuction and extend fuction====')
james.append('1.3')
james.extend(['1.34', '4.5'])
print(james)
print("=======fast 3 times======")
print(james.top3())

print("=======fast 2 times======")
print(james.top3(2))
