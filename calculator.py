3# ================================
#        Simple Calculator
# ================================7


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number.\n")


def show_menu():
    print("\n" + "=" * 35)
    print("        🧮  CALCULATEER")
    print("=" * 35)
    print("  1.  Addition        ( + )")
    print("  2.  Subtraction     ( - )")
    print("  3.  Multiplication  ( × )")
    print("  4.  Division        ( ÷ )")
    print("  5.  Power           ( ^ )")
    print("  6.  Modulus         ( % )")
    print("  7.  Exit")
    print("=" * 35)


def format_number(n):
    """Return int-looking output when possible (e.g. 4.0 → 4)."""
    if isinstance(n, float) and n == int(n):
        return int(n)
    return n


def main():
    print("\nWelcome to Calculateer! 🎉")

    operations = {
        "1": ("Addition",       "+",  add),
        "2": ("Subtraction",    "-",  subtract),
        "3": ("Multiplication", "×",  multiply),
        "4": ("Division",       "÷",  divide),
        "5": ("Power",          "^",  power),
        "6": ("Modulus",        "%",  modulus),
    }

    while True:
        show_menu()
        choice = input("\n  Enter your choice (1-7): ").strip()

        if choice == "7":
            print("\n  Thanks for using Calculateer! Goodbye 👋\n")
            break

        if choice not in operations:
            print("\n  ⚠  Invalid choice. Please pick a number from 1 to 7.")
            continue

        name, symbol, func = operations[choice]
        print(f"\n  --- {name} ---")
        a = get_number("  Enter first number : ")
        b = get_number("  Enter second number: ")

        result = func(a, b)

        if isinstance(result, str):          # error message
            print(f"\n  ❌  {result}")
        else:
            print(f"\n  ✅  {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()
