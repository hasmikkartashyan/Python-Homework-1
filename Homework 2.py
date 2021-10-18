# Digit product
n = int(input())

digit = 1
if digit > 0:
    while n > 0:
        digit = digit * (n % 10)
        n = n // 10
print(digit)


# Power of three
def foo(n):
    if n <= 3:
        return n
    else:
        curr = 3
        while 3 * curr < n:
            curr = curr * 3
        return curr
print(foo(n))



# The root of the number
def foo(num):
    print(num)
    if num <= 0:
        return 0
    sum = 0
    while num > 0:
        sum += (num % 10)
        num = num // 10
    if sum > 10:
        return foo(sum)
    else:
        return sum


# Number of divisors
num = int(input())

count = 0

print("Number of divisors:")

for i in range(1, num + 1):
    count += 1

    if(num % i == 0):
        print(count)