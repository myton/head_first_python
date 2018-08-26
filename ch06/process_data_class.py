class Athlete:
  def __init__(self, a_name="", a_dob=None, a_times=[]):
    self.name = a_name
    self.dob = a_dob
    self.times = a_times
  def top3(self):
    return (sorted(set([santize(t) for t in self.times]))[0:3])

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
    return Athlete(_name, _dob, _times)
  except IOError as err:
    print ("file is missing " + str(err))
    return None


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print (james.name + "'s fastest times are: " + str(james.top3()))
print (julie.name + "'s fastest times are: " + str(julie.top3()))
print (mikey.name + "'s fastest times are: " + str(mikey.top3()))
print (sarah.name + "'s fastest times are: " + str(sarah.top3()))
