from UserInput.input import *

def sum_of(n):
  return (n * (n+1)) // 2

def main():
  try:
    while True:
      num = int_input()
      if num <= 0:
        print("Numbers Should Be Greater then Zero")
      else:
        res = sum_of(num)
        print(res)
        break
  except Exception as e:
    print("Error : ",e)

if __name__ == "__main__": 
  main()