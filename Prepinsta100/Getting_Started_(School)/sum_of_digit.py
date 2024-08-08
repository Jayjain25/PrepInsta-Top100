def sum_of_digit(num):
  res = 0
  while num != 0:
    rem = num % 10
    res += rem
    num = num//10
  
  return res


def main():
  num = int(input("Enter the number (should be positive) : "))
  res = sum_of_digit(num)
  print("Sum of given Number is :",res)
    

if __name__ == "__main__":
  main()
  
  