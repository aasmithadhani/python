#Diamond
rows = int(input("Enter height"))
for i in range(1,rows+1):
    print(' '*(rows-i) + "* "*i)
for i in range(rows-1,0,-1):
    print(" "*(rows-i)+'* '*i)

#Triangle
# def triangle_pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(i):
#             number = chr(ord('A')+j)
#             print(f"{number}", end=" ")
#         print()

def triangle_pattern(rows):
        for i in range(1, rows + 1):
            char = chr(ord('A') + i - 1)
            line = char * i
            print(line)
# Example usage:
triangle_pattern(5)

# def pyramid_pattern(rows):
#     for i in range(1, rows + 1):
#         print(" " * (rows - i) + "* " * i)
        

# # Example usage:
# pyramid_pattern(5)

# def square_pattern(rows, columns):
#     for i in range(rows):
#         for j in range(columns):
#             print("*", end=" ")
#         print()

# # Example usage:
# square_pattern(5, 5)



