# multiplication_table.py
# Generate and print multiplication table for a given number

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
