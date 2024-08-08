from UserInput.input import *

def sum_of_range(start,end):
  Sum = 0
  for i in range(start,end+1):
    Sum += i
  return Sum

print(sum_of_range(1,5))


  