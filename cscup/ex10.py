a = 0    
maior = a
for linha in range(0,9):
    a = int(input())
    if a > maior and linha != 8:
        maior = a

print(maior)