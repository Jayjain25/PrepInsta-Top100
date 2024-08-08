def Greater_among_two(num1,num2):
  return max(num1,num2)

def Greater_among_three(num1,num2,num3):
  res = Greater_among_two(num1,num2)
  return max(res,num3)

def Greater_among_four(num1,num2,num3,num4):
  res = Greater_among_three(num1,num2,num3)
  return max(res,num4)

def Greater_among_five(num1,num2,num3,num4,num5):
  res = Greater_among_four(num1,num2,num3,num4)
  return max(res,num5)

print(Greater_among_four(2,10,1,20))