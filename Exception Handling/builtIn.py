def division_example(x, y):
    try:
        result = x / y
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Unsupported operand type.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This block is always executed, regardless of exceptions.")

def index_error_example(my_list):
    try:
        element = my_list[5]
        print(f"Element at index 5: {element}")
    except IndexError:
        print("Error: Index out of range.")
    finally:
        print("This block is always executed, regardless of exceptions.")



if __name__ == "__main__":
    
    try:
        # Example 1: Division by zero
        division_example(10, 0)

        # Example 2: Unsupported operand type
        division_example("abc", 2)

        # Example 3: Index out of range
        my_list = [1, 2, 3, 4]
        index_error_example(my_list)
    except KeyError:
        print("Error: Key not found.")
    except RuntimeError:
        print("Error: Runtime error occurred.")
    except SyntaxError:
        print("Error: Syntax error in the code.")
    except KeyboardInterrupt:
        print("\nProgram was interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("All examples executed successfully!")



  





