def sum_all(input):
  index = 0
  output = 0
  while index < len(input):
    output += input[index]
    index += 1
  return output

def testcase():
  value = sum_all([])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([0, 0, 0, 0, 0])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([1, -1, 2, -2, 3, -3])
  assert value == 0, f"expected return value was 0, but function returned {value}" 

  value = sum_all([1, 2, 3, 4, 5])
  assert value == 15, f"expected return value was 15, but function returned {value}" 

  print("All tests passed.")

#testcase()