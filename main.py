class SimpleCalculator:
    def __init__(self):
        self.history = []

    def calculate(self):
        print("-------Simple Calculator-------")
        print("Enter an operation (i.e., 3 * 3 or 1 + 1, etc.)")
        print('Enter "e" to exit.')

        while True:
            equation = input("- ").strip()

            if equation == 'e'  and equation == 'E':
                print("Exiting program...")
                break

            sliced = equation.split()
            try:
                first_num = float(equation[0])
                operation = equation[1]
                second_num = float(equation[2])
            except ValueError:
                print("\nError: Invalid input. Please enter valid numbers.")
                continue