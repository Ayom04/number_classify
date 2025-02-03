def is_perfect(number: int) -> int:
    if number <= 1:
        return False

    sum_divisors = 1
    for i in range(2, number//2+1):
        if number % i == 0:
            sum_divisors += i

    return sum_divisors == number


print(is_perfect(6))  # True
print(is_perfect(10))  # False
print(is_perfect(1))  # False
print(is_perfect(0))  # False
