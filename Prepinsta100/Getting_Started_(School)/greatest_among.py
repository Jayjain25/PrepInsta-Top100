def gretest_among_two(num1,num2):
  return max(num1,num2)


def main():
  try:
    num1 = int(input("Enter a Number 1st :- "))
    num2 = int(input("Enter a Number 2nd :- "))
    
    res = gretest_among_two(num1,num2)
    
    print(res,"is gretest")
  
  except Exception as e:
    print(e)
    

if __name__ == "__main__":
  main()