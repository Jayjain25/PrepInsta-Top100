def generat_prime_series(num1,num2):
  res = []
  
  for i in range(num1,num2+1):
    flag = True
    for j in range(2,(i//2) + 1):
      if i % j == 0:
        flag = False
        break
    
    if flag:
      res.append(i)
      
  return res

def main():
  num1 = int(input("Enter Start number (should be positive) : "))
  num2 = int(input("Enter Ending number (should be positive) : "))
  res = generat_prime_series(num1,num2)
  print(res)
    

if __name__ == "__main__":
  main()