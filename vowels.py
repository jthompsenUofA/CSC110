def count_vowels(input):
  count = 0
  ticker = 0
  while ticker < len(input):
    if input[ticker] in "aeiouAEIOU":
      count += 1
    ticker += 1
  return count

def testcase():
  print( count_vowels("") ) # 0
  print( count_vowels("aaa") ) # 3
  print( count_vowels("AEIOU") ) # 5
  print( count_vowels("cysts") ) # 0

#testcase()