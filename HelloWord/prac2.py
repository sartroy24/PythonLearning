# # Space padding
# print("{:>5}".format(23444))  # Output: '   42'
# s = "2222"
# print(s[2:])
N = int(input("Enter the number:"))

for item in range(1, N+1):
    print("{0:>{M}d} {0:>{M}o} {0:>{M}X} {0:>{M}b}".format(item, M = len("{0:>b}".format(N))))
