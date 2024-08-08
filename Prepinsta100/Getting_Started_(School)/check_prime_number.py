def check_prime(num):
  if num < 0:
    return False
  
  elif  num == 0 or num == 1:
    return True
  
  for i in range(2,(num//2)+1):
    if num % i == 0:
      return False
  
  return True

def main():
  num = int(input("Enter the number (should be positive) : "))
  res = check_prime(num)
  if res == True:
    print("It's a Prime Number")
  
  else:
    print("No, It's not prime number")
    

if __name__ == "__main__":
  main()