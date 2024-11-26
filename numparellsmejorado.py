num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
paresSum = 0
imparesSum = 0

for i in num:
    if i % 2 == 0:
        paresSum += i
    else:
        imparesSum += i

print(f"Suma de numeros pares: {paresSum}")
print(f"Suma de numeros impares: {imparesSum}")