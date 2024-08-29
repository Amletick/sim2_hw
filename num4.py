from fractions import Fraction
frac1=input("Введите первую дробь в формате a/b: ")
frac2=input("Введите вторую дробь в формате a/b: ")
numerator1,denominator1=map(int, frac1.split('/'))
numerator2,denominator2=map(int, frac2.split('/'))
f1=Fraction(numerator1,denominator1)
f2=Fraction(numerator2,denominator2)
sum_fraction=f1+f2
multiplication_fraction=f1*f2
print(f"Сумма: {sum_fraction}, Произведение: {multiplication_fraction}")
