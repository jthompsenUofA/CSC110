def validate_age(age):
  string_valid =  age.isnumeric()
  
  if (string_valid == True):
    age_int = int(age)
    if (age_int >= 0) and (age_int <= 110):
      return True
  return False
    
def check_eligibility(age):
  if (age >= 18):
    return True
  return False

def testcase():
  print( validate_age("20") ) # True
  print( validate_age("20.5") ) # False
  print( validate_age("20a") ) # False
  print( validate_age("300") ) # False
  print( check_eligibility(20) ) # True
  print( check_eligibility(15) ) # False

#testcase()