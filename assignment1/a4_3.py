def sum_of_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Enter a number: "))
print("Sum of all numbers from 1 to", n, "is:", sum_of_numbers(n))
