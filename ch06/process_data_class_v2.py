class Athlete:
  def __init__(self, a_name="", a_dob=None, a_times=[]):
    self.name = a_name
    self.dob = a_dob
    self.times = a_times

  def top3(self):
    return (sorted(set([santize(t) for t in self.times]))[0:3])

  def add_time(self, a_time):
    self.times.append(a_time)

  def add_times(self, list_of_times):
      self.times.extend(list_of_times)

def print_object(athlete):
  print (athlete.name + ", " + athlete.dob + "," + str(athlete.times))


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

james.add_time('12.3')
james.add_times(['11.3', '4.5'])
print_object(james)
julie.add_time('11.8')
print_object(julie)
mikey.add_time('8.7')
print_object(mikey)
sarah.add_time('7.9')
print_object(sarah)
