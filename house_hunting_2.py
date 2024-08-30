def calculate_months(salary, saved, cost, bonus):
    portion_down_payment = .25
    down_payment = portion_down_payment * cost
    current_savings = 0
    r=0.04
    raise_counter = 1
    months = 0
    monthly_salary = salary / 12
    ammount_saved = monthly_salary * saved
    while current_savings < down_payment:
      if raise_counter == 5:
        salary *= 1+bonus
        monthly_salary = salary / 12
        raise_counter = 0
        # Calculate ammount_saved based on the NEW salary
        ammount_saved = monthly_salary * saved
      else:
        raise_counter += 1
      current_savings += ammount_saved + (current_savings * r / 12)
      months += 1
    return months


def testcase1():
  annual_salary = 120000
  portion_saved = .05
  total_cost =  500000
  semi_annual_raise = .03
  total_months = calculate_months(annual_salary, portion_saved, total_cost, semi_annual_raise)
  print("Number of months:", total_months)

def testcase2():
  annual_salary =  80000
  portion_saved = .1
  total_cost =   800000
  semi_annual_raise = .03
  total_months = calculate_months(annual_salary, portion_saved, total_cost, semi_annual_raise)
  print("Number of months:", total_months)

def testcase3():
  annual_salary =   75000
  portion_saved = .05
  total_cost =    1500000
  semi_annual_raise = .05
  total_months = calculate_months(annual_salary, portion_saved, total_cost, semi_annual_raise)
  print("Number of months:", total_months)

testcase1()
testcase2()
testcase3()