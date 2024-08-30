def calculate_months(salary, saved, cost):
  portion_down_payment = .25
  down_payment = portion_down_payment * cost
  current_savings = 0
  r=0.04
  months = 0
  monthly_salary = salary / 12
  ammount_saved = monthly_salary * saved
  while current_savings < down_payment:
    current_savings += ammount_saved + (current_savings * r / 12)
    months += 1
  return months
  

def testcase1():
  annual_salary = 120000
  portion_saved = .1
  total_cost = 1000000
  total_months = calculate_months(annual_salary, portion_saved, total_cost)
  print("Number of months:", total_months)

def testcase2():
  annual_salary = 80000
  portion_saved = .15
  total_cost = 500000
  total_months = calculate_months(annual_salary, portion_saved, total_cost)
  print("Number of months:", total_months)

testcase1()
testcase2()