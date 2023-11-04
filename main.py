# N
n = int(input('цифре:'))
count = 0
for a in range(1, int(n**0.5) + 1):
    if n % a == 0:
        b = n // a
        if a < b and a * b <= n:
            etoda = True
            for i in range(2, min(a, b) + 1):
             if a % i == 0 and b % i == 0:
                    etoda = False
                    break
            if etoda:
                count += 1

print(count)