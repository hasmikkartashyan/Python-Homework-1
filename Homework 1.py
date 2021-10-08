# 1.1
x = int(input())
a = x % 10 + x // 10 % 10 + x // 100
print(a)


# 1.2
a = int(input())
b = int(input())
print((a*b)/2)

# 1.3
a_1 = int(input())
a_2 = int(input())
n = int(input())

a_n = a_2 * (n - 1) - a_1 * (n - 2)
print(a_n)


# 1.4
year = int(input())
x = (year - 1) // 100 + 1
print(int(x))


# 1.5
x = int(input())
y = int(input())
a = x + y

print(a - x - 1)
print(a - y - 1)

# 1.6
x = int(input())
y = int(input())

print(x-2, y-1)
print(x-2, y+1)
print(x-1, y-2)
print(x-1, y+2)
print(x+2, y-1)
print(x+2, y+1)
print(x+1, y-2)
print(x+1, y+2)

