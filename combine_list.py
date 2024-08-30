def combine(list1, list2):
  if len(list1) == 0:
    return list2
  if len(list2) == 0:
    return list1
  index = 0
  output = list1
  while index < len(list2):
    output.append(list2[index])
    index += 1
  return output

def testcase():
  test_list = []
  combine(test_list, []) 
  print(test_list) # []

  test_list = [1, 2, 3]
  combine(test_list, [1, 1]) 
  print(test_list) # [1, 2, 3, 1, 1]

  test_list = [1, 2, 3, 1, 5]
  combine(test_list, [])
  print(test_list) # [1, 2, 3, 1, 5]

#testcase()