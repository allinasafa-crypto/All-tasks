a = [1, 3, 4, 5, 2]

# your code
# output should be [1,2,3,4,5]
#  while loop
i = 0
while (i < len(a)-1):
    if (a[i] > a[i + 1]):

        a[i], a[i + 1] = a[i + 1], a[i]

        i = 0
    else:
        i += 1

print(a)


# Forloop

# for i in range(1, len(a)):
#     current = a[i]     
#     n = i - 1

#     while (n >= 0 and a[n] > current):
#         a[n + 1] = a[n]   
#         n -= 1

#     a[n + 1] = current    

# print(a)

