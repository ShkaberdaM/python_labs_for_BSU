N=int(input())
dict1={ num: sum(1 for i in range(1, num + 1) if num % i == 0)
        for num in range(1, N + 1)}
print(dict1)

