N = int(input("Enter the number of numbers to be generated:"))
def fibonacci(N):
    prev1 = 0
    prev2 = 1
    print(prev1)
    print(prev2)
    for item in range(N):
        fibo = prev1+prev2
        print(fibo)
        prev2 = prev1
        prev1 = fibo
        
        

fibonacci(N)