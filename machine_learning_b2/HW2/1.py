class FormulaError(Exception):
    pass

def calculate_formula(input_formula):
    try:
        elements = input_formula.split()

        # Kiểm tra xem có đúng 3 phần tử không
        if len(elements) != 3:
            raise FormulaError("Invalid input. Please provide a formula in the format: operand1 operator operand2")

        operand1 = float(elements[0])
        operand2 = float(elements[2])

        operator = elements[1]
        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Please use only '+' or '-'")

        result = operand1 + operand2 if operator == '+' else operand1 - operand2

        print(f"Result: {result}")

    except ValueError:
        raise FormulaError("Invalid input. Please provide valid numeric values for operands")

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter a formula (e.g., 1 + 1), or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                break

            calculate_formula(user_input)

        except FormulaError as e:
            print(f"Error: {e}")
