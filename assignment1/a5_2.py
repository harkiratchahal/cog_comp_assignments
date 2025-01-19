def sum_divisible_by_7_and_9(n):
    return sum(i for i in range(1, n + 1) if i % 7 == 0 and i % 9 == 0)

n = int(input("Enter a number: "))
print("Sum of all numbers divisible by 7 and 9:", sum_divisible_by_7_and_9(n))
