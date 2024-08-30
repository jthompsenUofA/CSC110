def calculate_tax(input):
  if input >200000:
    rate = 30
  elif input > 75000:
    rate = 25
  elif input > 15000:
    rate = 20
  elif input > 0:
    rate = 10
  else:
    return None
  return input * (rate /100.0)

def calc(annual, rent, bills, food, travel):
  print('------------------------------------------------------------------')
  print('See the  financial breakdown below, based on a salary of $'+str(annual))
  print('------------------------------------------------------------------')

calc(500,0,0,0,0)