num_real_divisor = int(input())
real_divisors = sorted([int(x) for x in input().split()])

N = real_divisors[0] * real_divisors[-1]

print(N)