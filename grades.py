def letter_grade(score):
  if score > 100:
    return 'X'
  if score >= 90:
    return 'A'
  if score >= 80:
    return 'B'
  if score >= 70:
    return 'C'
  if score >= 60:
    return 'D'
  if score >= 0:
    return 'E'
  return 'X'

def pass_or_fail(input):
  if(len(input) == 1):
    if input in 'ABCD':
      return "Pass"
    if input == 'E':
      return "Fail"
  return 'Error'

def point_grade(score, total_score):
  return round(score / total_score * 100, 2)

def get_grade_results(score, total_score):
  point_grade_result = point_grade(score, total_score)
  letter_grade_result = letter_grade(point_grade_result)
  pass_or_fail_result = pass_or_fail(letter_grade_result)
  return "Your grade is "+str(point_grade_result)+" ("+letter_grade_result+" - "+pass_or_fail_result+")"

# test letter_grade function
assert letter_grade(90) == "A"
assert letter_grade(80) == "B"
assert letter_grade(70) == "C"
assert letter_grade(60) == "D"
assert letter_grade(59) == "E"
assert letter_grade(-59) == "X"
assert letter_grade(110) == "X"

# test pass_or_fail function
assert pass_or_fail("B") == "Pass"
assert pass_or_fail("E") == "Fail"
assert pass_or_fail("ABCD") == "Error"

# test point_grade function
assert point_grade(0, 100) == 0.0
assert point_grade(100, 100) == 100.0
assert point_grade(45, 80) == 56.25
assert point_grade(37, 40) == 92.5
# test get_grade_results function
assert get_grade_results(0, 100) == "Your grade is 0.0 (E - Fail)"
assert get_grade_results(45, 80) == "Your grade is 56.25 (E - Fail)"
assert get_grade_results(37, 40) == "Your grade is 92.5 (A - Pass)"