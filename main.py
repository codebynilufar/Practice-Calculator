from calculator import(
    add, substruct, multiply, divide
)
def main():
    expression = input("Calculation: ")
    op1, op, op2 = expression.split()

    op1 = float(op1)
    op2 = float(op2)

    result = None
    if op == "+":
        result = add(op1,op2)
    elif op == "-":
        result = substruct(op1,op2)
    elif op == "*":
        result = multiply(op1,op2)
    elif op == "/":
        result = divide(op1,op2)
    print("Natija:", result)
    
if __name__ == "__main__":
    main()