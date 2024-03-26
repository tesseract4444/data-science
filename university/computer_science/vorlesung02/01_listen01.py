empty = []

one = [1]

squares = [1, 'vier', 9.0, 16, 16 + 9, 72 / 2]

primes = [2, 3, 5, 7, 11, 13, 17, 19]

print('Beispiele zur Liste primes:', primes)
print(f'\nErstes Element der Liste:',primes[0])

primes[2] = 7
print(f'Drittes Element auf 7 setzen:', primes)

print('\nZugriff auf letztes Element der Liste:')
last1 = primes[7]
last2 = primes[-1]
last3 = primes[len(primes)-1]
print(last1, last2, last3)

primes[len(primes)-1] = 0
print(f'\nLetztes Element auf 0:', primes)

print('\n************************************************\n')

print('Hausaufgabe:')
liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
liste[0] = 0**2
liste[1] = 1**2
liste[2] = 2**2
liste[3] = 3**2
liste[4] = 4**2
liste[5] = 5**2
liste[6] = 6**2
liste[7] = 7**2
liste[8] = 8**2
liste[9] = 9**2
liste[10] = 10**2

print(liste)