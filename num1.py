a = int(input("Первое число: "))
b = int(input("Второе число: "))
while b:
    a, b = b, a % b
print(f"НОД: {a}")