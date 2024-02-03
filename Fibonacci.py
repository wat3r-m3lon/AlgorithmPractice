# Time and space complexity is O(n)
def getNthFib(n):
    # Write your code here.
    fib=[0,1]

    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
         
    return fib[n-1]

#Time complexity O(n),space complexity O(1)
def getNthFib(n):
    # Write your code here.
    last=[0,1]
    counter=3
    while counter<=n:
        next=last[0]+last[1]
        last[0]=last[1]
        last[1]=next
        counter+=1
    if n>1:
        return last[1]
    else:
        return last[0]