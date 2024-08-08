from UserInput.input import *

def check_even_odd(num):
  
  if num % 2 == 0:
    return True
  else:
    return False


try:
  while True:
    num = int_input()
    if num <= 0:
      print("Number should be positive")
    else:
      res = check_even_odd(num)
      
      if res == True:
        print("Given Number is Even Number")
      else:
        print("Given Number is Odd Number")
      
      break
  
except Exception as e:
  print(e)
