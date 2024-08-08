def single_digit(num):
  res = 0
  while num != 0:
    res = num % 10 + res
    num //= 10
    
    if res > 9:
      temp = res
      res = 0
      
      while temp != 0:
        res += temp%10
        temp //= 10
        
  return res

def main():
  num = int(input("Enter the number (should be positive) : "))
  res = single_digit(num)
  print(res)
  
    

if __name__ == "__main__":
  main()