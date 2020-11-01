# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
# By convention, 1 is included. Given a number n, the task is to find n’th Ugly number.
def nth_ugly_number(num):
    ugly_number = [0]*num
    ugly_number[0] = 1
    second_multiple = third_multiple = fifth_multiple = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, num):
        ugly_number[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        if ugly_number[i] == next_multiple_of_2:
            second_multiple += 1
            next_multiple_of_2 = ugly_number[second_multiple] * 2

        if ugly_number[i] == next_multiple_of_3:
            third_multiple += 1
            next_multiple_of_3 = ugly_number[third_multiple] * 3

        if ugly_number[i] == next_multiple_of_5:
            fifth_multiple += 1
            next_multiple_of_5 = ugly_number[fifth_multiple] * 5
    return ugly_number[-1]


n = int(input())
number = nth_ugly_number(n)
print(number)
