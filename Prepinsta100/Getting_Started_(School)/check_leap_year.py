def check_leaf_year(days):
  return (days == 366)

def main():
  try:
    days = int(input("Enter the days in a year : "))
    res = check_leaf_year(days)
    if res == True:
      print("It's a leap year")
    
    else:
      print("No it's not leap year")
      
  except Exception as e:
    print(str(e))
    
    
if __name__ == "__main__":
  main()