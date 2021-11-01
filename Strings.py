# Jewels and Stones

jewels = input()
stones = input()

count = 0

if len(jewels) < len(stones):
    for i in jewels:
       if i in stones:
           count += 1
else:
    for i in stones:
        if i in jewels:
            count += 1
print(count)




#  String power

s = input()
k = int(input())

if k >= 0:
    s = s * k
    print(s)

if k < 0:
    # for i in len(s)
    s_list = s.split()
    map_object = map(int, s_list)

    list_of_integers = list(map_object)
    print(list_of_integers)

    # Compare characters in the list from the first element. When elements are repeated, split first part and shorten
    # by k.
    # print(s)
else:
    print('undefined')