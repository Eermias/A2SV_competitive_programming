n = int(input())
prices = [int(x) for x in input().split()]
prices.sort()
q = int(input())
for i in range(q):
    money = int(input()) 
    options = 0
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if prices[m] <= money:
            options = max(options, m + 1)
            l = m + 1
        else:
            r = m - 1
    
    print(options)