# division.py
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    print("Division of 20 by 5 is:", divide(20, 5))
