num=int(input("Число: "))
numbers=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
rym_numbers=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
num_transform=''
i=12
num_for_out=num
while num>0:
    if num//numbers[i]>0:
        num_transform+=rym_numbers[i]
        num-=numbers[i]
    else:
        i-=1

print(f"Было:{num_for_out} Стало:{num_transform}")