def max3(x,y,z):
  num=x
  if (num < y):
    num = y
  elif (num < z):
    num = z
  return num

def testcase():
  print( max3(1, 1, 1) ) # 1
  print( max3(1, 2, 1) ) # 2
  print( max3(-1, -1, 0) ) # 0
  print( max3(100, 0, 0) ) # 100
  print( max3(19, 19, 0) ) # 19
  print( max3(2, 0, 2) ) # 2
  print( max3(-100, 0, 0) ) # 0

#testcase()