print('Instanzierung und Listen:\n')
even_squares1 = [0, 4, 16, 36, 64, 100]
#print(even_squares1)

even_squares2 = []
for i in range(11):
    if i%2 == 0:
        even_squares2.append(i*i)
#print(even_squares2)

even_squares3 = [i*i for i in range(11) if i%2 == 0]
#print(even_squares3)

print('***********************************')

evens = [2 * i for i in range(10)]
print(evens)

unevens = [i for i in range(20) if i%2 == 1]
print(unevens)

print('***********************************')

print('Weitere Beispiele zur Instanzierung von Listen:\n')
unevens2 = [2 * i +1 for i in range(51)]
print(unevens2)

evens2 = [i for i in range(101) if i % 2 == 0]
print(evens2)

squares = [i * i for i in range(101) if i%3 == 0]

#primes = [i for i in range(101) if isPrime(i)]


print('***********************************')

print('Listen und Type hints:\n')

from typing import List, Any

squares: List[int] = [i * i for i in range(10)]
names: List[str] = ['Jack', 'James', 'Jason']

print(squares)
print(names)

#langschreibweise zu 'squares' oben
#squares2 = []
#for k in range(10):
    #k *=k
    #squares2.append(k)
#print(squares2)

#langschreibweise zu 'names' oben
#names2 = ['Jack', 'James', 'Jason']
#print(names2)

matrix: List[List[int]] = [[1,0,0], [0,1,0], [0,0,1]]
print(matrix)

mixed_list: List[Any] = [1, 'Zwei', 3.0, 4] #Any steht für irgendwelche Datentypen
print(mixed_list)

print('***********************************')

print('Hausaufgabe:\n')

def sum_of_elements(numbers: List[int]) -> int:
    if len(numbers) == 0:
        return 'Fehler!'
    sum = 0
    for element in numbers:
        sum += element
    return sum

print(sum_of_elements([]))
print(sum_of_elements([i for i in range(11)]))
print(sum_of_elements([j*j for j in range(8) if j % 2 == 0]))

print('***********************************')

print('Slicing - Beispiele1:')
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

all_primes = primes[:]
print(all_primes)

first_three_primes = primes[0:3]
print(first_three_primes)

last_two_primes = primes[-2:]
print(last_two_primes)

primes_with_even_indexes = primes[::2]
print(primes_with_even_indexes)

primes_reversed = primes[::-1]
print(primes_reversed)

print('***********************************')

print('Slicing - Beispiele2:\n')

nums = [i for i in range(10)]
print(nums)

print(nums[:])
print(nums[:3])
print(nums[0:3])
print(nums[5:])
print(nums[-5:-3])
print(nums[::2])
print(nums[::-1])
print(nums[-2:])
print(nums[:-2])