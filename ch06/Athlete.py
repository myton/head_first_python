class Athlete:
  def __init__(self, a_name, a_dob=None, a_times=[]):
    self.name = a_name
    self.dob = a_dob
    self.times = a_times

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:28', '2.58', '1.56'])
james = Athlete('James Jones')
print ('type(sarah)')
print (type(sarah))
print (">>> sarah ")
print (sarah)
print ('type(james)')
print (type(james))
print (">>>  james ")
print (james)

print (">>> sarah.name")
print (sarah.name)
print ('>>> james.name')
print (james.name)
print ('>>> sarah.dob')
print (sarah.dob)
print ('>>> james.dob')
print (james.dob)
print ('>>> sarah.times')
print (sarah.times)
print ('>>> james.times')
print (james.times)
