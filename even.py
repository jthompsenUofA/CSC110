def is_even():
  number = int(input('Enter a number:'))
  return (not bool(number % 2))

def testcase():
  print("Enter 0:")
  print( is_even() ) # True 

  print("Enter 1:")
  print( is_even()) # False 

  print("Enter 2:")
  print( is_even()) # True 

  print("Enter -2:")
  print( is_even()) # True 

#testcase()