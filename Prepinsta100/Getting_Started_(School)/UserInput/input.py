def int_input():
  try:
    num = int(input("Enter a number : "))
    return num
  except Exception:
    print("Error : Please enter digits only")
    return int_input()
    
def string_input():
  try:
    Str = input("Enter a text : ")
    return Str
  except Exception as e:
    return string_input()
    print("Error", e)