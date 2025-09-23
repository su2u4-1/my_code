from typing import TextIO

link = "python\\data\\"
print("正在讀取質數")
with open(link + "質數.txt", "r") as f:
    prime_list = list(map(int, f.readlines()))
print("質數讀取完畢")
print(prime_list[-1])


def isPrime(b: int):
    for i in prime_list:
        if b % i == 0:
            return False
    return True


def calculate_new_primes(start: int, end: int, file: TextIO):
    for i in range(start - (start % 6), end + (6 - end % 6), 6):
        if isPrime(i + 1):
            prime_list.append(i + 1)
            file.write(str(i + 1) + "\n")
        if isPrime(i + 5):
            prime_list.append(i + 5)
            file.write(str(i + 5) + "\n")


try:
    n = int(input("要計算的數:"))
except:
    print("error: 須為正整數")
    exit()
if n <= 0:
    print("error: 須為正整數")
if n == 1:
    print(1)
    exit()
if n > prime_list[-1]:
    print("正在計算新質數")
    with open(link + "質數.txt", "a+") as f:
        calculate_new_primes(prime_list[-1] + 1, n + 1, f)
    print("新質數記錄完畢")
if n in prime_list:
    print("是質數")
factor_counts: dict[int, int] = {}
while n > 1:
    for i in prime_list:
        if i > n:
            break
        if n % i == 0:
            if i in factor_counts:
                factor_counts[i] += 1
            else:
                factor_counts[i] = 1
            n /= i
l: list[str] = []
for i in factor_counts:
    if factor_counts[i] == 1:
        l.append(str(i))
    else:
        l.append(str(i) + "^" + str(factor_counts[i]))
print("*".join(l))
