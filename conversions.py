def kg_to_lbs():
  kilo = int(input('Input Kilograms:'))
  return round(kilo * 2.205,2)

def liters_to_gallons():
  liters = int(input('Input Liters:'))
  return round(liters / 3.785,2)

def testcase():
  print("Enter 1:")
  print( kg_to_lbs() ) # 2.21 

  print("Enter 6:")
  print( kg_to_lbs() ) # 13.23

  print("Enter 120:")
  print( kg_to_lbs() ) # 264.6 

  print("Enter 1:")
  print( liters_to_gallons() ) # 0.26 

  print("Enter 3:")
  print( liters_to_gallons() ) # 0.79

  print("Enter 6:")
  print( liters_to_gallons() ) # 1.59 

#testcase()