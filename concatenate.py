def concatenate(input):
    index = 0
    if len(input) == 0:
        return ''
    output = input[index]
    while index < len(input) - 1:
        output += " "
        output += input[index+1]
        index += 1
    return output

def testcase():
  value = concatenate([])
  assert value == "", \
      f"expected return value was an empty string, but function returned {value}" 

  value = concatenate(["", "", ""])
  assert value == "  ", \
      f"expected return value was an \"  \", but function returned {value}" 

  value = concatenate(["Hi", "there"])
  assert value == "Hi there", \
      f"expected return value was an \"Hi There\", but function returned {value}"
  value = concatenate(["Test", "Set", "Three"])
  assert value == "Test Set Three", \
          f"expected return value was an \"Test Set Three\", but function returned {value}"


    

    

  print("All tests passed.")

#testcase()