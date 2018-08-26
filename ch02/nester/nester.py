""" This is the nester.py model which provides print_lol function. The function is used to print list including nest list.
"""

def print_lol(the_list, level):
  """ The parameter is the_list, each item output to screen.
  """

  for each_item in the_list:
    if isinstance(each_item, list):
      print_lol(each_item, level+1)
    else:
      for tab_stop in range(level):
        print("\t", end='')
      print(each_item)
