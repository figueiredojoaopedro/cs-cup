x = int(input())
y = int(input())
menor = 0
maior = 0
soma =0
if x < y:
    menor = x
    maior = y
else:
    menor = y
    maior = x
menor +=1 
while menor < maior:
    if menor % 2 != 0:
        soma+= menor
    menor += 1

print(soma)