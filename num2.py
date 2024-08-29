def transform(a,b_hex):
    if a==0 :
        return 0
    else:
        negative=0
        if a<0:
            negative=1
            a=-a
        hex_a=''
        while a>0:
            quotient=a%16
            hex_a=b_hex[quotient]+hex_a
            a//=16
        if negative:
                hex_a='-'+hex_a
        return hex_a

num = int(input("Число: "))
alphabet = '0123456789ABCDEF'
by_hand=transform(num,alphabet)
by_hex='%X'%num
if by_hand==by_hex:
    print(f"Перевод совпал с hex, вручную: {by_hand} через hex: {hex(num)}")
else:
    print(f"Перевод не совпал с hex, вручную: {by_hand} через hex: {hex(num)}")

