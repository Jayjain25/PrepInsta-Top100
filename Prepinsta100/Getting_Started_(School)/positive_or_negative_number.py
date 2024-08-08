def checkNumber(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    try:
        num = float(input("Enter a Number to check: "))
        result = checkNumber(num)
        print(f"Given number is a {result} Number")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()

    
    