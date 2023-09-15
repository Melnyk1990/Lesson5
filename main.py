import random


print('\t' * 3, '*'* 10, 'Task 1', 10 * '*')

NUMS_SIZE = 10
numbers = []
negativ = 0
parni = 0
neparni = 0
kratnye3 = 1
dobutok_min_max = 1

poz1 =0
poz2 =0


random.randint(-5, 5)
for i in range(NUMS_SIZE):
    numbers.append(random.randint(-5, 5))
    if numbers[i] < 0:
        negativ += numbers[i]

    if numbers[i] % 2 == 0:
        # print(numbers[i], end=' ')
        parni += numbers[i]
    elif numbers[i] % 2 == 1:
        # print(numbers[i], end=' ')
        neparni += numbers[i]

print(f'List created: {numbers}')
print()
print(f'The sum of negative numbers is: {negativ}')

print(f'The sum of even numbers is: {parni}')

print(f'The sum of odd numbers is: {neparni}')

for i in numbers:
    if i==0:
        continue
    elif i%3 ==0:
        # print(i, end=' ')
        kratnye3 *=i
print(f'The product of numbers that are multiples of "3" is equal to: {kratnye3}')


min_numb = numbers.index(min(numbers))
max_numb = numbers.index(max(numbers))
for i in numbers[min_numb + 1:max_numb]:
    if i ==0:
        continue
    else:
        dobutok_min_max *=i

print(f'The product of the elements between min and max is: {dobutok_min_max}')

for i in numbers:
    if i >0:
        poz1 +=i
        # print(i, end=' ')
print()
for i in reversed(numbers):
    if i > 0:
        poz2 +=i
        # print(i, end=' ')
if poz1 == poz2:
    print(f'The sum of the elements that are between the first and last positive element: {poz1}')
else:
    print('Error')

print()
print()



print('\t' * 3, '*'* 10, 'Task 2', 10 * '*')
NUMS_SIZE = 10
parni = []
neparni =[]
negotiv = []
pozitiv = []
numbers = []

for i in range(NUMS_SIZE):
    numbers.append(random.randint(-5, 5))
new = numbers.copy()
print()
for i in new:
    if i ==0:
        continue
    elif i%2 == 0:
        parni.append(i)

    elif i%2 == 1:
        neparni.append(i)

    if new[i] < 0:
        negotiv.append(new[i])

    elif new[i] > 0:
        pozitiv.append(new[i])

print(f'Создан новый список: {new}')
print(f'List с четными числами: {parni}')
print(f'List с нечетными числами: {neparni}')
print(f'List с отрицательными числами: {negotiv}')
print(f'List с положительными числами: {pozitiv}')


