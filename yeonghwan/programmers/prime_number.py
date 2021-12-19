from itertools import combinations


def is_prime(a, b, c):
    total = a+b+c
    for i in range(2, total):
        if total % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combination_list = list(combinations(nums, 3))
    for combination in combination_list:
        if is_prime(combination[0], combination[1], combination[2]):
            answer += 1
    return answer
