def reverse_string(input):
  ticker = len(input)
  output = ''
  
  while ticker > 0:
    output += input[ticker - 1]
    ticker -= 1
  return output

def remove_spaces(input):
  ticker = 0
  output = ''
  while ticker < len(input):
    if input[ticker] != ' ':
      output += input[ticker]
    ticker += 1
  return output

def is_palindrome(input):
  fixed_input = remove_spaces(input)
  return (fixed_input == reverse_string(fixed_input))
def testcase():
  print( reverse_string("aeiou") ) # uoiea
  print( remove_spaces("ae io ua") ) # aeioua

  print( is_palindrome("noon") ) # True
  print( is_palindrome("deified") ) # True
  print( is_palindrome("go deliver a dare vile dog") ) # True

#testcase()