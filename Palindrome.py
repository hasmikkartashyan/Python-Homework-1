# Palindrome numbers

a = int(input())
b = int(input())

def palindrome(n):

    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10

    return (n == rev)


def countPal(a: int, b: int):
    for i in range(a, b + 1):
        if palindrome(i):
            print(i, end=" ")

#
# # Driver Code
if __name__ == "__main__":
    countPal(a, b)



# Cyclic shift

def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, -1):
        arr[i] = arr[i - 1]

    arr[0] = x


arr = []
a = int(input())

for i in range(0, a):
    e = [input(), int(input())]
    arr.append(e)


n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i])




