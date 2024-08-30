def stop_ascending(input):
  output = 0
  index = 0
  if len(input) == 0:
    return None
  while index < len(input) - 1:
    if input[index] > input[index + 1]:
      return input[index]
    index += 1
  return input[len(input) - 1]
  
  

def testcase():
  print( stop_ascending([]) ) # None
  print( stop_ascending([1, 2, 3]) ) # 3
  print( stop_ascending([1, 2, 3, 1, 5]) ) # 3

#testcase()