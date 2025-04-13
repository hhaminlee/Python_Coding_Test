input = 20

# 주어진 수보다 작은 수의 소수만 리턴
# 에라토스테네스의 체 이용
# 0과 1은 소수 제외
# i의 배수들은 소수가 아니므로 제외

def find_prime_list_under_number(number):
    isPrime = [True] * (number+1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(number**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, number+1, i):
                isPrime[j] = False

    return [i for i in range(number) if isPrime[i]]


result = find_prime_list_under_number(input)
print(result)